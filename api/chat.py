"""Funcion serverless de Vercel: /api/chat

Recibe {"query": "...", "historial": [{"role","content"}...]} y responde
{"respuesta": "..."} usando un modelo de IA con el corpus normativo del
repositorio como contexto.

La API key vive en las variables de entorno de Vercel (nunca en el navegador).
Si no hay key configurada responde 503 y el sitio usa su motor local.
"""

import json
import os
import re
import unicodedata
from http.server import BaseHTTPRequestHandler

import urllib.error
import urllib.request

from corpus import CORPUS, SYSTEM_PROMPT

MAX_DOCS = 4
MAX_HISTORIAL = 6
TIMEOUT = 55

VACIAS = {
    "para", "como", "esta", "este", "esto", "sobre", "cuando", "donde",
    "porque", "pero", "tiene", "tengo", "hace", "hacer", "puede", "puedo",
    "quiero", "necesito", "derecho", "derechos", "caso", "ley", "articulo",
    "que", "cual", "cuales", "quien", "todo", "toda", "muy", "mas", "menos",
    "sin", "con", "los", "las", "del", "una", "unos", "unas", "por", "ese",
    "esa", "esos", "esas", "nos", "les", "mis", "sus", "fue", "son", "han",
    "hay", "ver", "sido", "ser", "estar",
}


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return texto.lower()


def terminos(texto):
    return {p for p in re.findall(r"[a-zñ]{4,}", normalizar(texto)) if p not in VACIAS}


def contexto(pregunta):
    terminos_busqueda = terminos(pregunta)
    puntajes = []
    for nombre, texto in CORPUS.items():
        normalizado = normalizar(texto)
        puntaje = sum(
            normalizado.count(t) * (1 + len(t) / 10) for t in terminos_busqueda
        )
        if puntaje:
            puntajes.append((puntaje, nombre, texto))

    puntajes.sort(key=lambda x: x[0], reverse=True)
    elegidos = puntajes[:MAX_DOCS] or [
        (0, n, CORPUS[n])
        for n in ("constitucion_politica_colombia_completa.md",
                  "compendio_codigos_nacionales_colombia.md")
        if n in CORPUS
    ]
    return "\n\n".join("### Fuente: {}\n{}".format(n, t) for _, n, t in elegidos)


def instrucciones(fuentes):
    return """Eres el orientador juridico ciudadano de "Conoce tus Derechos" (Colombia).

Reglas obligatorias:
1. Habla en espanol claro, sin tecnicismos innecesarios, como para alguien sin formacion juridica.
2. Cita la norma concreta (ley, articulo, sentencia) solo si aparece en las FUENTES o en las INSTRUCCIONES DEL PROYECTO. Si no la encuentras, dilo y remite a SUIN-JURISCOL.
3. Nunca inventes articulos, numeros de ley, terminos ni entidades.
4. Empieza siempre con esta advertencia en cursiva: "Esta herramienta es un ejercicio academico pedagogico y no constituye asesoria juridica formal."
5. Estructura: derechos que te amparan, normas aplicables, pasos a seguir (con plazos si existen) y canales oficiales gratuitos.
6. No redactes demandas ni prometas resultados. Si el caso es urgente (violencia, salud, riesgo de vida), remite de inmediato a la entidad competente.
7. Si la consulta no es juridica, dilo brevemente.
8. Maximo 400 palabras. Usa vinetas y titulos cortos.

FUENTES:
{fuentes}

INSTRUCCIONES DEL PROYECTO:
{sistema}
""".format(fuentes=fuentes or "(sin fuentes)", sistema=SYSTEM_PROMPT[:3000]).strip()


MODELO_OPENROUTER = os.getenv("OPENROUTER_MODEL", "nvidia/nemotron-3-ultra-550b-a55b:free")
RESPALDOS_OPENROUTER = [
    "google/gemma-4-31b-it:free",
    "nvidia/nemotron-3.5-lightning:free",
]


def proveedor():
    if os.getenv("OPENROUTER_API_KEY"):
        return {
            "tipo": "openrouter",
            "proveedor": "OpenRouter",
            "key": os.getenv("OPENROUTER_API_KEY"),
            "modelo": MODELO_OPENROUTER,
            "respaldo": RESPALDOS_OPENROUTER,
            "url": "https://openrouter.ai/api/v1",
        }
    if os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"):
        return {
            "tipo": "gemini",
            "proveedor": "Google Gemini",
            "key": os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"),
            "modelo": os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        }
    if os.getenv("OPENAI_API_KEY"):
        return {
            "tipo": "openai",
            "proveedor": "OpenAI",
            "key": os.getenv("OPENAI_API_KEY"),
            "modelo": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            "url": os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/"),
        }
    if os.getenv("GROQ_API_KEY"):
        return {
            "tipo": "openai",
            "proveedor": "Groq",
            "key": os.getenv("GROQ_API_KEY"),
            "modelo": os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            "url": "https://api.groq.com/openai/v1",
        }
    return None


def historial_limpio(historial):
    limpio = []
    for msg in (historial or [])[-MAX_HISTORIAL:]:
        contenido = (msg.get("content") or "").strip()
        if contenido:
            rol = "assistant" if msg.get("role") == "assistant" else "user"
            limpio.append({"role": rol, "content": contenido[:1500]})
    return limpio


def _post_json(url, payload, cabeceras):
    """POST con la libreria estandar (sin dependencias externas)."""
    datos = json.dumps(payload).encode("utf-8")
    peticion = urllib.request.Request(url, data=datos, headers=cabeceras, method="POST")
    try:
        with urllib.request.urlopen(peticion, timeout=TIMEOUT) as resp:
            return resp.status, resp.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "ignore")


def _compatible(cfg, sistema, historial, pregunta, modelo):
    mensajes = [{"role": "system", "content": sistema}]
    mensajes.extend(historial_limpio(historial))
    mensajes.append({"role": "user", "content": pregunta})

    cabeceras = {
        "Authorization": "Bearer " + cfg["key"],
        "Content-Type": "application/json",
    }
    if cfg["tipo"] == "openrouter":
        cabeceras["HTTP-Referer"] = os.getenv(
            "SITE_URL", "https://conoce-tus-derechos-neon.vercel.app"
        )
        cabeceras["X-Title"] = "Conoce tus Derechos"

    estado, cuerpo = _post_json(
        cfg["url"] + "/chat/completions",
        {"model": modelo, "messages": mensajes, "temperature": 0.2, "max_tokens": 1200},
        cabeceras,
    )
    if estado != 200:
        raise RuntimeError("{} {}: {}".format(cfg["proveedor"], estado, cuerpo[:160]))
    opciones = (json.loads(cuerpo).get("choices") or [])
    return (opciones[0]["message"].get("content") or "").strip() if opciones else ""


def generar(pregunta, historial=None):
    cfg = proveedor()
    if not cfg:
        raise RuntimeError("sin_key")

    sistema = instrucciones(contexto(pregunta))

    if cfg["tipo"] == "gemini":
        contenidos = [
            {
                "role": "model" if m["role"] == "assistant" else "user",
                "parts": [{"text": m["content"]}],
            }
            for m in historial_limpio(historial)
        ]
        contenidos.append({"role": "user", "parts": [{"text": pregunta}]})
        estado, cuerpo = _post_json(
            "https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent".format(cfg["modelo"]),
            {
                "system_instruction": {"parts": [{"text": sistema}]},
                "contents": contenidos,
                "generationConfig": {"temperature": 0.2, "maxOutputTokens": 1200},
            },
            {"x-goog-api-key": cfg["key"], "Content-Type": "application/json"},
        )
        if estado != 200:
            raise RuntimeError("Gemini {}".format(estado))
        datos = json.loads(cuerpo)
        candidatos = datos.get("candidates") or []
        partes = candidatos[0].get("content", {}).get("parts", []) if candidatos else []
        return "".join(p.get("text", "") for p in partes).strip()

    # OpenRouter / OpenAI / Groq comparten el formato de OpenAI.
    errores = []
    for modelo in [cfg["modelo"]] + cfg.get("respaldo", []):
        try:
            return _compatible(cfg, sistema, historial, pregunta, modelo)
        except RuntimeError as exc:
            errores.append("{}: {}".format(modelo, exc))
            continue
    raise RuntimeError(" | ".join(errores)[:300])


class handler(BaseHTTPRequestHandler):
    def _json(self, estado, datos):
        cuerpo = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        self.send_response(estado)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_OPTIONS(self):
        self._json(204, {})

    def do_GET(self):
        cfg = proveedor()
        self._json(200, {
            "estado": "ok" if cfg else "sin_key",
            "proveedor": cfg["proveedor"] if cfg else None,
            "modelo": cfg["modelo"] if cfg else None,
        })

    def do_POST(self):
        try:
            largo = int(self.headers.get("Content-Length") or 0)
            if largo > 20000:
                self._json(413, {"error": "consulta demasiado larga"})
                return
            datos = json.loads(self.rfile.read(largo) or b"{}")
            pregunta = (datos.get("query") or "").strip()
            if not pregunta:
                self._json(400, {"error": "falta la consulta"})
                return
            respuesta = generar(pregunta, datos.get("historial"))
            if not respuesta:
                raise RuntimeError("respuesta vacia")
            self._json(200, {"respuesta": respuesta})
        except RuntimeError as exc:
            if str(exc) == "sin_key":
                self._json(503, {"error": "IA no configurada en el servidor"})
            else:
                self._json(502, {"error": str(exc)[:200]})
        except Exception as exc:
            self._json(500, {"error": str(exc)[:200]})
