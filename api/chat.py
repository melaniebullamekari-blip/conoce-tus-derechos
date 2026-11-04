"""Funcion serverless de Vercel: /api/chat

Recibe {"query": "...", "historial": [{"role","content"}...]} y responde
{"respuesta": "..."} usando un modelo de IA con el corpus normativo del
repositorio como contexto.

El corpus (.md) se descarga del propio repositorio publico y se guarda en
memoria mientras la funcion esta caliente, para no tener que subir archivos
extra al despliegue.

La API key vive en las variables de entorno de Vercel (nunca en el navegador).
Si no hay key configurada responde 503 y el sitio usa su motor local.
"""

import json
import os
import re
import unicodedata
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler

MAX_DOCS = 4
MAX_HISTORIAL = 6
TIMEOUT = 55

REPO_RAW = os.getenv(
    "CORPUS_BASE_URL",
    "https://raw.githubusercontent.com/melaniebullamekari-blip/conoce-tus-derechos/main/",
)

DOCUMENTOS = [
    "constitucion_politica_colombia_completa.md",
    "constitucion_politica_1991.md",
    "compendio_codigos_nacionales_colombia.md",
    "codigo_penal_delitos_vida_patrimonio.md",
    "codigo_sustantivo_trabajo.md",
    "codigo_infancia_adolescencia_familia.md",
    "ley_1755_2015_derecho_peticion.md",
    "ley_1751_2015_estatutaria_salud.md",
    "ley_1480_2011_consumidor.md",
    "ley_820_2003_arrendamiento.md",
    "ley_769_2002_transito_fotomultas_accidentes.md",
    "ley_906_2004_procedimiento_penal_denuncia.md",
    "ley_1257_2008_violencia_genero_intrafamiliar.md",
    "ley_1266_2008_habeas_data_financiero.md",
    "ley_142_1994_servicios_publicos.md",
    "ley_1801_2016_codigo_policia.md",
    "ley_2300_2023_dejen_de_fregar.md",
    "ley_43_1993_nacionalidad_colombiana.md",
    "sentencias_hito_corte_constitucional.md",
    "sentencia_c055_2022_ive.md",
    "guia_suin_juriscol_fuentes_oficiales.md",
]

VACIAS = {
    "para", "como", "esta", "este", "esto", "sobre", "cuando", "donde",
    "porque", "pero", "tiene", "tengo", "hace", "hacer", "puede", "puedo",
    "quiero", "necesito", "derecho", "derechos", "caso", "ley", "articulo",
    "que", "cual", "cuales", "quien", "todo", "toda", "muy", "mas", "menos",
    "sin", "con", "los", "las", "del", "una", "unos", "unas", "por", "ese",
    "esa", "esos", "esas", "nos", "les", "mis", "sus", "fue", "son", "han",
    "hay", "ver", "sido", "ser", "estar",
}

# Respaldo minimo si la descarga del corpus falla.
CORPUS_MINIMO = {
    "resumen_constitucional.md": (
        "### Constitucion Politica de 1991 (resumen)\n"
        "Art. 1 Estado social de derecho; Art. 11 vida; Art. 13 igualdad; "
        "Art. 15 intimidad y habeas data; Art. 23 derecho de peticion; "
        "Art. 29 debido proceso; Art. 86 accion de tutela (10 dias, sin abogado); "
        "Art. 93 bloque de constitucionalidad.\n"
        "### Codigo Penal (Ley 599 de 2000)\n"
        "Art. 239 hurto simple; Art. 240 hurto calificado (violencia, armas, "
        "indefension); Art. 241 hurto agravado.\n"
        "### Arrendamiento (Ley 820 de 2003)\n"
        "Canon, incrementos, terminacion y restitucion de inmueble urbano.\n"
        "### Consumidor (Ley 1480 de 2011)\n"
        "Garantia legal, retracto y reverso del pago.\n"
        "### Trabajo (CST)\n"
        "Despido sin justa causa, indemnizacion y liquidacion.\n"
    ),
}

_cache = None


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return texto.lower()


def terminos(texto):
    return {p for p in re.findall(r"[a-zñ]{4,}", normalizar(texto)) if p not in VACIAS}


# El ciudadano escribe "me robaron", no "hurto": estas pistas conectan sus
# palabras con los terminos que realmente usan las normas.
SINONIMOS = {
    "hurto": ["robo", "roba", "robe", "hurt", "atrac", "asalt", "rater", "despoj", "sustra"],
    "homicidio": ["matar", "mataron", "mato", "asesin", "homicid", "feminicid", "sicari"],
    "arrendamiento": ["arriend", "arrend", "canon", "inquilin", "inmueble", "desalojo"],
    "despido": ["despid", "desped", "liquidaci", "salario", "sueldo", "prestacion", "trabaj"],
    "salud": ["eps", "medicament", "cirugia", "enfermedad", "cita medic", "incapacidad"],
    "peticion": ["peticion", "solicitud", "responder", "radicad"],
    "consumidor": ["garantia", "devolucion", "retracto", "compra", "producto"],
    "alimentos": ["cuota alimentaria", "pension alimenticia", "hijos", "manutencion"],
    "violencia intrafamiliar": ["violencia", "agresion", "golpiza", "maltrato", "amenaza"],
    "familia": ["divorcio", "custodia", "union marital", "herencia", "sucesion"],
    "transito": ["comparendo", "fotomulta", "accidente", "vehiculo", "moto", "carro"],
    "penal": ["denuncia", "fiscalia", "captura", "flagrancia", "abogado"],
}


def ampliar(terminos_busqueda):
    """Agrega el termino normativo cuando la consulta usa una palabra coloquial."""
    ampliados = set(terminos_busqueda)
    for canonico, pistas in SINONIMOS.items():
        for pista in pistas:
            if any(t.startswith(pista[:5]) for t in terminos_busqueda):
                ampliados.update(canonico.split())
                ampliados.add(canonico.split()[0])
                break
    return ampliados


def _descargar(nombre):
    peticion = urllib.request.Request(
        REPO_RAW + nombre, headers={"User-Agent": "conoce-tus-derechos"}
    )
    with urllib.request.urlopen(peticion, timeout=10) as resp:
        return resp.read().decode("utf-8", "ignore").strip()


def documentos():
    """Descarga (una sola vez) el corpus normativo del repositorio."""
    global _cache
    if _cache is not None:
        return _cache

    def bajar(nombre):
        try:
            return nombre, _descargar(nombre)
        except Exception:
            return nombre, ""

    try:
        with ThreadPoolExecutor(max_workers=8) as pool:
            cargados = {
                nombre: texto for nombre, texto in pool.map(bajar, DOCUMENTOS) if texto
            }
    except Exception:
        cargados = {}

    _cache = cargados or dict(CORPUS_MINIMO)
    return _cache


def contexto(pregunta):
    corpus = documentos()

    # El system_prompt.md del repositorio manda las reglas del proyecto.
    try:
        sistema = _descargar("system_prompt.md")[:3000]
    except Exception:
        sistema = ""

    terminos_busqueda = ampliar(terminos(pregunta))
    puntajes = []
    for nombre, texto in corpus.items():
        normalizado = normalizar(texto)
        puntaje = sum(
            normalizado.count(t) * (1 + len(t) / 10) for t in terminos_busqueda
        )
        if puntaje:
            puntajes.append((puntaje, nombre, texto))

    puntajes.sort(key=lambda x: x[0], reverse=True)

    # La Constitucion siempre va como base, aunque no tenga coincidencias.
    elegidos = [
        (0, n, corpus[n])
        for n in ("constitucion_politica_colombia_completa.md",)
        if n in corpus
    ]
    for candidato in puntajes:
        if len(elegidos) >= MAX_DOCS:
            break
        if candidato[1] not in {n for _, n, _ in elegidos}:
            elegidos.append(candidato)

    fuentes = "\n\n".join("### Fuente: {}\n{}".format(n, t[:6000]) for _, n, t in elegidos)
    return fuentes, sistema


def instrucciones(fuentes, sistema):
    return """Eres el orientador juridico ciudadano de "Conoce tus Derechos" (Colombia).

Reglas obligatorias:
1. Habla en espanol claro, sin tecnicismos innecesarios, como para alguien sin formacion juridica.
2. Responde a CUALQUIER consulta juridica, sin importar como este escrita (coloquial, con errores, regionalismos, una sola palabra o un relato largo).
3. Cita la norma concreta (ley, articulo, sentencia) solo si aparece en las FUENTES o en las INSTRUCCIONES DEL PROYECTO. Si no la encuentras, dilo y remite a SUIN-JURISCOL.
4. Nunca inventes articulos, numeros de ley, terminos ni entidades.
5. Empieza siempre con esta advertencia en cursiva: "Esta herramienta es un ejercicio academico pedagogico y no constituye asesoria juridica formal."
6. Estructura: derechos que te amparan, normas aplicables, pasos a seguir (con plazos si existen) y canales oficiales gratuitos.
7. No redactes demandas ni prometas resultados. Si el caso es urgente (violencia, salud, riesgo de vida), remite de inmediato a la entidad competente.
8. Si la consulta no es juridica, dilo brevemente.
9. Maximo 400 palabras. Usa vinetas y titulos cortos.

FUENTES:
{fuentes}

INSTRUCCIONES DEL PROYECTO:
{sistema}
""".format(fuentes=fuentes or "(sin fuentes)", sistema=sistema or "(no disponible)").strip()


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


def _mensajes(sistema, historial, pregunta):
    mensajes = [{"role": "system", "content": sistema}]
    mensajes.extend(historial_limpio(historial))
    mensajes.append({"role": "user", "content": pregunta})
    return mensajes


def _cabeceras(cfg):
    cabeceras = {
        "Authorization": "Bearer " + cfg["key"],
        "Content-Type": "application/json",
    }
    if cfg["tipo"] == "openrouter":
        cabeceras["HTTP-Referer"] = os.getenv(
            "SITE_URL", "https://conoce-tus-derechos-neon.vercel.app"
        )
        cabeceras["X-Title"] = "Conoce tus Derechos"
    return cabeceras


def _compatible(cfg, sistema, historial, pregunta, modelo):
    mensajes = _mensajes(sistema, historial, pregunta)
    cabeceras = _cabeceras(cfg)

    estado, cuerpo = _post_json(
        cfg["url"] + "/chat/completions",
        {"model": modelo, "messages": mensajes, "temperature": 0.2, "max_tokens": 1200},
        cabeceras,
    )
    if estado != 200:
        raise RuntimeError("{} {}: {}".format(cfg["proveedor"], estado, cuerpo[:160]))
    opciones = json.loads(cuerpo).get("choices") or []
    return (opciones[0]["message"].get("content") or "").strip() if opciones else ""


def generar(pregunta, historial=None):
    cfg = proveedor()
    if not cfg:
        raise RuntimeError("sin_key")

    fuentes, sistema_proyecto = contexto(pregunta)
    sistema = instrucciones(fuentes, sistema_proyecto)

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
        candidatos = json.loads(cuerpo).get("candidates") or []
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


def _compatible_stream(cfg, sistema, historial, pregunta, modelo):
    """Pide al proveedor la respuesta en streaming y va entregando los trozos."""
    payload = {
        "model": modelo,
        "messages": _mensajes(sistema, historial, pregunta),
        "temperature": 0.2,
        "max_tokens": 1200,
        "stream": True,
    }
    peticion = urllib.request.Request(
        cfg["url"] + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers=_cabeceras(cfg),
        method="POST",
    )

    try:
        respuesta = urllib.request.urlopen(peticion, timeout=TIMEOUT)
    except urllib.error.HTTPError as exc:
        detalle = exc.read().decode("utf-8", "ignore")[:200]
        raise RuntimeError("{} {}: {}".format(cfg["proveedor"], exc.code, detalle))
    except urllib.error.URLError as exc:
        raise RuntimeError("{} sin conexion: {}".format(cfg["proveedor"], exc.reason))

    with respuesta:
        for crudo in respuesta:
            linea = crudo.decode("utf-8", "ignore").strip()
            if not linea or not linea.startswith("data:"):
                continue
            carga = linea[5:].strip()
            if not carga:
                continue
            if carga == "[DONE]":
                break
            try:
                evento = json.loads(carga)
            except ValueError:
                continue
            if evento.get("error"):
                raise RuntimeError(str(evento["error"])[:200])
            opciones = evento.get("choices") or []
            if not opciones:
                continue
            trozo = (opciones[0].get("delta") or {}).get("content")
            if trozo:
                yield trozo


def generar_stream(pregunta, historial=None):
    """Generador que entrega la respuesta por partes (texto plano)."""
    cfg = proveedor()
    if not cfg:
        raise RuntimeError("sin_key")

    fuentes, sistema_proyecto = contexto(pregunta)
    sistema = instrucciones(fuentes, sistema_proyecto)

    if cfg["tipo"] == "gemini":
        texto = generar(pregunta, historial)
        if texto:
            yield texto
        return

    errores = []
    for modelo in [cfg["modelo"]] + cfg.get("respaldo", []):
        generador = _compatible_stream(cfg, sistema, historial, pregunta, modelo)
        try:
            primero = next(generador)
        except StopIteration:
            errores.append("{}: respuesta vacia".format(modelo))
            continue
        except RuntimeError as exc:
            errores.append("{}: {}".format(modelo, exc))
            continue

        yield primero
        try:
            for trozo in generador:
                yield trozo
        except Exception as exc:
            # Ya se envio texto: no conviene reiniciar con otro modelo.
            raise RuntimeError(str(exc)[:200])
        return

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

    def _evento(self, datos):
        cuerpo = "data: " + json.dumps(datos, ensure_ascii=False) + "\n\n"
        self.wfile.write(cuerpo.encode("utf-8"))
        self.wfile.flush()

    def _stream(self, generador):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache, no-transform")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Connection", "close")
        self.send_header("X-Accel-Buffering", "no")
        self.end_headers()

        enviado = False
        try:
            for trozo in generador:
                if not trozo:
                    continue
                enviado = True
                self._evento({"delta": trozo})
            self._evento({"fin": True})
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception as exc:
            if not enviado:
                self._evento({"error": str(exc)[:200]})
        finally:
            try:
                self.wfile.flush()
            except Exception:
                pass

    def do_GET(self):
        cfg = proveedor()
        self._json(200, {
            "estado": "ok" if cfg else "sin_key",
            "proveedor": cfg["proveedor"] if cfg else None,
            "modelo": cfg["modelo"] if cfg else None,
            "streaming": True,
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
            if datos.get("stream"):
                if not proveedor():
                    self._json(503, {"error": "IA no configurada en el servidor"})
                    return
                self._stream(generar_stream(pregunta, datos.get("historial")))
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
