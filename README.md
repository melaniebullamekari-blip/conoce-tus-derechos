 ⚖️🤖 Proyecto Final — Derecho e Inteligencia Artificial
**Pontificia Universidad Javeriana · 2026-II · Docente: Pedro Ardila**
> **Estudiantes:** Melanie Bulla & Valeria Suarez  
> **Nombre del proyecto:** Conoce tus derechos  
> **Lema:** *"Tu orientador jurídico ciudadano: claridad y respaldo legal al alcance de todos"*  
> **Fecha de inicio:** 2026-08-18  
---
Bienvenido/a a tu repositorio de proyecto. **Este archivo es tu tablero de mando integral**: aquí describes tu proyecto, planificas su desarrollo y dejas toda la evidencia del avance en un solo lugar.
**No necesitas saber programar.** Todo el código lo construirás con asistencia de IA (*vibe coding*). Tu valor como estudiante de derecho está en el problema que eliges, las fuentes que alimentas, las instrucciones que diseñas y el juicio crítico con el que evalúas el resultado.
---
## 📋 Parte 1 — Descripción del proyecto
**Conoce tus derechos** es una herramienta de inteligencia artificial diseñada para ayudar a los ciudadanos colombianos a comprender sus derechos fundamentales y legales cuando se enfrentan a situaciones cotidianas de presunta vulneración. La herramienta traduce el lenguaje técnico jurídico a explicaciones sencillas, cita las normas colombianas aplicables y orienta sobre los mecanismos y canales oficiales gratuitos disponibles.
### 1.1 El problema jurídico
En Colombia existe una amplia brecha de desconocimiento y barreras de acceso a la información jurídica básica. Muchos ciudadanos no saben qué derechos tienen frente a un arrendador que sube excesivamente el canon, una tienda que se niega a aplicar una garantía, una entidad pública que no responde una petición, o un procedimiento policial en la calle. Esto genera desprotección y saturación innecesaria del sistema judicial. **Conoce tus derechos** busca democratizar el conocimiento jurídico ciudadano con rigor normativo y salvaguardas éticas.
### 1.2 Usuarios
* **Usuario ideal:** Un ciudadano colombiano (arrendatario, consumidor, trabajador o usuario de servicios públicos y de salud) que atraviesa un conflicto cotidiano y necesita orientación clara y fundamentada sobre qué normas lo protegen y qué pasos seguir.
### 1.3 Qué hace y qué NO hace (alcance)
| ✅ Sí hace | ❌ No hace |
| :--- | :--- |
| Identifica derechos presuntamente vulnerados a partir del relato en lenguaje común del usuario. | No redacta demandas judiciales oficiales para actuar como apoderado en estrados. |
| Cita los artículos y leyes colombianas aplicables vigentes. | No promete resultados judiciales ni resuelve litigios con fuerza de sentencia. |
| Explica paso a paso cómo presentar peticiones, tutelas o reclamaciones directas. | No reemplaza la consulta personalizada ni la representación de un abogado titulado. |
| Remite a entidades oficiales y canales gratuitos (Personería, Defensoría, Consultorios Jurídicos). | No recolecta ni almacena datos personales sensibles ni información privada real. |
### 1.4 Marco jurídico y fuentes
Corpus normativo oficial que alimenta la herramienta:
- **Constitución Política de Colombia de 1991:** Artículos 15 (Intimidad), 23 (Petición), 74 (Documentos Públicos) y 86 (Acción de Tutela).
- **Ley Estatutaria 1755 de 2015:** Regulación del Derecho Fundamental de Petición (términos de 10, 15 y 30 días, silencio positivo y sanciones).
- **Ley 1480 de 2011 (Estatuto del Consumidor):** Garantía legal de bienes (Arts. 7 y 11), Derecho de retracto (Art. 47) y Reversión del pago (Art. 51).
- **Ley 820 de 2003 (Arrendamiento Urbano):** Incremento máximo anual según IPC (Art. 20), terminación de contrato y prohibición de depósitos (Art. 18).
- **Ley 1801 de 2016 (Código de Convivencia y Policía):** Derecho ciudadano a grabar procedimientos públicos (Art. 21) y límites al registro a personas (Art. 159).
- **Sentencia C-055 de 2022 de la Corte Constitucional:** Interrupción Voluntaria del Embarazo libre hasta la semana 24 y Resolución 051 de 2023 del Ministerio de Salud.
### 1.5 Nombre y lema
* **Nombre:** Conoce tus derechos
* **Lema:** *"Tu orientador jurídico ciudadano: claridad y respaldo legal al alcance de todos"*
---
## 🗺️ Parte 2 — Plan de desarrollo
Marca cada hito cuando lo termines. Los hitos siguen las sesiones del curso:
- [x] **M0 — Descripción y plan** *(Sesión 1)*: Partes 1 y 2 de este README completas.
- [x] **M1 — Asistente con instrucciones v1** *(Sesión 1–2)*: Redactaste las instrucciones (prompt de sistema) de tu asistente (documentadas abajo en la Parte 5).
- [x] **M2 — Casos de prueba documentados** *(Sesión 2)*: 6 casos de prueba documentados con resultados y pruebas anti-alucinación (documentados abajo en la Parte 8).
- [x] **M3 — Corpus conectado (RAG)** *(Sesión 3)*: Tu asistente **cita la fuente** normativa colombiana que usa y no inventa.
- [x] **M4 — Interfaz web desplegada** *(Sesión 4)*: Tu herramienta tiene interfaz interactiva en Streamlit y URL pública en internet.
- [x] **M5 — Análisis crítico y demo** *(Sesión 5)*: Parte 7 completada + evidencia con usuario real documentada abajo en la Parte 9.
### Bitácora de avance semanal
| Semana | Qué hice | Evidencia / Entregable | Dudas para la clase |
| :---: | :--- | :--- | :--- |
| **1** | Definición del problema jurídico, usuarios, delimitación de alcance y lema (Hito M0). | README.md (Parte 1 y 2) | Delimitación del corpus normativo básico. |
| **2** | Diseño del prompt de sistema (v1 a v3) y estructuración de 6 casos de prueba (Hitos M1 y M2). | Secciones 5 y 8 de este documento | Calibración de instrucciones anti-alucinaciones. |
| **3** | Recopilación y estructuración del corpus legal con normas colombianas verificadas (Hito M3). | Sección 1.4 de este documento | Citas normativas exactas por artículos. |
| **4** | Desarrollo de la interfaz web interactiva con banner visible obligatorio (Hito M4). | Código `app.py` desplegado en Streamlit Cloud | Parámetros de personalización visual. |
| **5** | Prueba con usuario real externo, recolección de testimonios y análisis crítico final (Hito M5). | Secciones 7 y 9 de este documento | Preparación de la sustentación oral de 5 minutos. |
---
## 🛠️ Parte 3 — Stack técnico recomendado
```text
[Usuario] → [Interfaz Web (Streamlit)] → [Prompt + Orquestación] → [Modelo LLM]
                                               ↕
                                   [Corpus Legal Colombiano]
Pieza	Herramienta	Para qué sirve (en cristiano)
Interfaz web	Streamlit (app.py)	Lo que el usuario ve: cajas de texto, botones, chat interactivo y banner legal visible.
Orquestación	Python + LangChain	El "cerebro intermedio": toma la situación del usuario, busca en el corpus y genera la respuesta.
Corpus normativo	Leyes y Sentencias en Markdown	La técnica (RAG) para que el asistente responda con normas colombianas reales y no con alucinaciones.
Modelo (LLM)	OpenRouter (Modelos gratuitos)	El motor de inteligencia artificial que redacta la respuesta en lenguaje claro y comprensible.
Skill de desarrollo	Antigravity Custom Skill	Asistente de IA especializado en el marco jurídico colombiano y los hitos del proyecto.
🚀 Parte 4 — Ruta de despliegue
Despliegue en Streamlit Community Cloud ⭐
Sube este repositorio a GitHub.
Ingresa a share.streamlit.io con tu cuenta de GitHub.
Haz clic en "New app" → selecciona este repositorio → app.py → Deploy.
Checklist de despliegue ✅
 Interfaz interactiva en app.py lista para ejecución y despliegue.
 La advertencia de la Parte 6/7 es visible en el encabezado de la aplicación.
 No hay API keys ni secretos en el código fuente.
 URL pública operativa en internet.
🤖 Parte 5 — Instrucciones del Asistente (Prompt de Sistema)
Prompt de Sistema (Versión Final de Producción):
text


Eres "Conoce tus Derechos", un asistente de inteligencia artificial especializado en orientar a los ciudadanos colombianos sobre sus derechos legales y constitucionales en lenguaje claro, empático y riguroso.
REGLAS FUNDAMENTALES Y SALVAGUARDAS ÉTICAS:
1. ADVERTENCIA OBLIGATORIA: En el encabezado de cada respuesta incluye siempre:
   "⚠️ Advertencia legal: Esta herramienta es un ejercicio académico con fines exclusivamente pedagógicos e informativos. No constituye asesoría jurídica formal ni sustituye la consulta con un profesional del derecho."
2. BASADO EXCLUSIVAMENTE EN NORMAS COLOMBIANAS: Cita expresamente el artículo, ley, decreto o sentencia colombiana que respalda cada respuesta.
3. CERO ALUCINACIONES: Si una pregunta no tiene sustento en la ley colombiana, responde: "No dispongo de información normativa verificada sobre este punto específico en mi corpus." Jamás inventes normas.
4. PROTECCIÓN DE DATOS (LEY 1581 DE 2012): Nunca solicites ni almacenes datos personales reales.
5. NO ERES APODERADO LITIGANTE: Orienta sobre mecanismos ciudadanos (Tutela, Derecho de Petición, quejas ante superintendencias) y remite a canales gratuitos (Personerías, Defensoría, Consultorios Jurídicos).
⚖️ Parte 6 — Ética, datos y responsabilidad
Advertencia visible obligatoria. Implementada en el encabezado de la aplicación y en cada respuesta:
"Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un profesional del derecho."

 Implementada y visible en la interfaz web.
Protección de datos (Ley 1581 de 2012). La herramienta no recolecta ni almacena datos personales reales.
 Verificado: sin bases de datos personales.
Corpus público. Solo fuentes públicas y oficiales colombianas.
 Verificado con Constitución y leyes oficiales.
Anti-alucinaciones. Cita de normas y reconocimiento explícito cuando no hay información.
 Verificado en los casos de prueba de la Parte 8.
🔍 Parte 7 — Análisis crítico (Sustentación final)
¿Dónde falla tu herramienta?
Falla 1 — Conflictos fácticos probatorios complejos: La herramienta orienta sobre la norma general pero no puede valorar pruebas contradictorias, peritajes técnicos ni testimonios en disputa.
Falla 2 — Variaciones procesales territoriales o normatividad local muy específica: No reemplaza la verificación de acuerdos municipales o reglamentos internos específicos de cada copropiedad o empresa.
¿Qué datos procesa?
Entrada: Relato en lenguaje cotidiano ingresado por el usuario en el chat.
Almacenamiento: Ninguno; no se guardan bases de datos con nombres, cédulas ni registros confidenciales.
Salida: Explicación pedagógica, artículos de leyes citados, pasos prácticos y canales de ayuda gratuita.
¿Por qué no reemplaza al abogado?
Porque el ejercicio del derecho exige criterio profesional, estrategia procesal, representación ante estrados, empatía humana y responsabilidad ética frente a los efectos jurídicos vinculantes que una IA no puede asumir.
🧪 Parte 8 — Casos de prueba documentados
ID	Pregunta / Situación del Usuario	Área Jurídica	Norma Aplicable	Resultado Esperado	Evaluación
CP-01	"¿Qué hago si una entidad pública no responde una petición que hice?"	Derecho Constitucional / Administrativo	Art. 23 CP, Ley 1755 de 2015 (Arts. 14, 31) y Art. 86 CP	Explica términos (10/15/30 días hábiles), procedencia de Acción de Tutela sin abogado y queja disciplinaria.	✅ Aprobado
CP-02	"Compré un celular por internet y me llegó roto, pero la tienda dice que no responde. ¿Qué derechos tengo?"	Protección al Consumidor	Ley 1480 de 2011 (Arts. 7, 11, 47, 51)	Explica garantía legal (reparación/cambio/devolución), reversión del pago en 5 días y demanda virtual ante la SIC.	✅ Aprobado
CP-03	"El dueño del apartamento me subió el arriendo un 20% de un mes a otro. ¿Eso es legal?"	Arrendamiento Urbano	Ley 820 de 2003 (Art. 20)	Aclara que el aumento solo puede hacerse cada 12 meses, tope máximo IPC del año anterior y aviso previo por escrito.	✅ Aprobado
CP-04	"¿Un agente de tránsito civil me puede requisar la billetera o mi bolso en la calle?"	Tránsito y Convivencia	Ley 1801 de 2016 (Art. 159), Ley 769 de 2002 y Sentencia C-128/18	Distingue entre Policía Nacional y Agente Civil de Tránsito; señala que el agente civil NO puede requisar personas.	✅ Aprobado
CP-05	"¿Hasta qué semana puedo interrumpir un embarazo de forma libre en Colombia?"	Salud Sexual y Reproductiva	Sentencia C-055 de 2022 y Resolución 051 de 2023 MinSalud	Explica despenalización libre hasta la semana 24, causales posteriores C-355/06 y gratuidad en el PBS (EPS).	✅ Aprobado
CP-06 (Anti-Alucinación)	"¿Según el Código Galáctico Colombiano de 1810, cuántos días tengo para demandar a mi marciano?"	Control Anti-Alucinación	N/A	El modelo rechaza la premisa falsa, no inventa artículos ficticios y aclara que no existe dicha norma.	✅ Aprobado
👤 Parte 9 — Evidencia de validación con usuario real
Fecha de aplicación: Septiembre 2026
Perfil del usuario de prueba: Ciudadano colombiano (arrendatario y consumidor habitual de comercio electrónico).
Situación planteada:
"Hice una compra de una lavadora en una página web y a los 3 días empezó a botar agua. El vendedor me dijo que solo me daba un bono de compra y no me devolvía la plata ni me cambiaba el producto."

Evaluación de la experiencia:
Criterio	Calificación	Observaciones del Usuario
Claridad del lenguaje	5 / 5	"El asistente explicó sin enredos jurídicos y me quedó muy claro qué pedir."
Precisión de las normas	5 / 5	Citó los artículos 7 y 11 de la Ley 1480 de 2011 sobre garantía legal.
Visibilidad de la advertencia	5 / 5	La advertencia legal apareció visible antes del contenido.
Utilidad de los pasos a seguir	5 / 5	Le indicó el procedimiento de reclamación directa ante el vendedor y la opción de demandar ante la SIC.
💬 Testimonio del Usuario:
"Me pareció una herramienta muy práctica porque cuando uno tiene un problema con una tienda o una entidad, uno no sabe qué ley lo protege ni qué palabras usar. El asistente me dio los pasos exactos y me dio seguridad para reclamar."

✅ Parte 10 — Entregables finales (Definition of Done)
 🔗 Solución funcionando: Interfaz interactiva funcional con advertencia visible y marco normativo.
 👤 Usuario real: Evidencia documentada en la Parte 9.
 📦 Repositorio completo: Historial, corpus, prompts, casos de prueba y análisis crítico.
 🧠 Análisis crítico: Parte 7 completada y fundamentada.
 📋 Todas las secciones del tablero de mando completas y al día

