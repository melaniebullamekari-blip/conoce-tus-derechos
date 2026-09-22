# ⚖️🤖 Proyecto Final — Derecho e Inteligencia Artificial
**Pontificia Universidad Javeriana · 2026-II · Docente: Pedro Ardila**
> **Estudiantes:** Melanie Bulla & Valeria Suarez  
> **Nombre del proyecto:** Conoce tus derechos  
> **Lema:** *"Tu orientador jurídico ciudadano: claridad y respaldo legal al alcance de todos"*  
> **Fecha de inicio:** 2026-08-18  
---
Bienvenido/a a tu repositorio de proyecto. **Este archivo es tu tablero de mando**: aquí describes tu proyecto, planificas su desarrollo y dejas evidencia del avance.
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
- [x] [**Constitución Política de Colombia de 1991:** Artículos 15, 23, 74 y 86](./constitucion_politica_1991.md)
- [x] [**Ley Estatutaria 1755 de 2015:** Derecho Fundamental de Petición](./ley_1755_2015_derecho_peticion.md)
- [x] [**Ley 1480 de 2011:** Estatuto del Consumidor](./ley_1480_2011_consumidor.md)
- [x] [**Ley 820 de 2003:** Arrendamiento de Vivienda Urbana](./ley_820_2003_arrendamiento.md)
- [x] [**Ley 1801 de 2016:** Código Nacional de Policía y Convivencia](./ley_1801_2016_codigo_policia.md)
- [x] [**Sentencia C-055 de 2022:** Interrupción Voluntaria del Embarazo](./sentencia_c055_2022_ive.md)
### 1.5 Nombre y lema
* **Nombre:** Conoce tus derechos
* **Lema:** *"Tu orientador jurídico ciudadano: claridad y respaldo legal al alcance de todos"*
---
## 🗺️ Parte 2 — Plan de desarrollo
Marca cada hito cuando lo termines. Los hitos siguen las sesiones del curso:
- [x] **M0 — Descripción y plan** *(Sesión 1)*: Partes 1 y 2 de este README completas.
- [x] **M1 — Asistente con instrucciones v1** *(Sesión 1–2)*: Redactaste las instrucciones (prompt de sistema) de tu asistente (guardadas en [`system_prompt.md`](./system_prompt.md)).
- [x] **M2 — Casos de prueba documentados** *(Sesión 2)*: Tienes 6 casos de prueba documentados con resultados y pruebas anti-alucinación guardados en [`casos-de-prueba.md`](./casos-de-prueba.md).
- [x] **M3 — Corpus conectado (RAG)** *(Sesión 3)*: Tu asistente **cita la fuente** normativa colombiana que usa y no inventa.
- [x] **M4 — Interfaz web desplegada** *(Sesión 4)*: Tu herramienta tiene interfaz interactiva construida en [`app.py`](./app.py) con Streamlit y **URL pública** con evidencia de prueba.
- [x] **M5 — Análisis crítico y demo** *(Sesión 5)*: Parte 7 completada + evidencia con usuario real guardada en [`evidencia-usuario.md`](./evidencia-usuario.md).
### Bitácora de avance semanal
| Semana | Qué hice | Evidencia / Entregable | Dudas para la clase |
| :---: | :--- | :--- | :--- |
| **1** | Definición del problema jurídico, usuarios, delimitación de alcance y lema (Hito M0). | [README.md](./README.md) (Parte 1 y 2) | Delimitación del corpus normativo básico. |
| **2** | Diseño del prompt de sistema (v1 a v3) y estructuración de 6 casos de prueba (Hitos M1 y M2). | Archivos [`system_prompt.md`](./system_prompt.md) y [`casos-de-prueba.md`](./casos-de-prueba.md) | Calibración de instrucciones anti-alucinaciones. |
| **3** | Recopilación y estructuración del corpus legal en Markdown con normas colombianas (Hito M3). | Archivos de leyes en el repositorio | Citas normativas exactas por artículos. |
| **4** | Desarrollo de la interfaz web en Streamlit ([`app.py`](./app.py)) con banner visible obligatorio (Hito M4). | Archivo [`app.py`](./app.py) desplegado en Streamlit Cloud | Parámetros de personalización visual. |
| **5** | Prueba con usuario real externo, recolección de testimonios y análisis crítico final (Hito M5). | Archivo [`evidencia-usuario.md`](./evidencia-usuario.md) y Parte 7 del README | Preparación de la sustentación oral de 5 minutos. |
---
## 🛠️ Parte 3 — Stack técnico recomendado
```text
[Usuario] → [Interfaz Web (Streamlit)] → [Prompt + Corpus Normativo] → [Modelo LLM]
                                               ↕
                                   [Corpus Legal en Markdown]
Pieza	Herramienta	Función
Interfaz web	Streamlit (
app.py
)	Interfaz interactiva, amigable y responsiva con banner legal visible.
Orquestación & Prompting	Python + LangChain	Conexión con el corpus y estructuración de respuestas.
Corpus normativo	Leyes y Sentencias en Markdown	Base de conocimiento pública, verificable y libre de alucinaciones.
Skill de desarrollo	Antigravity Custom Skill	Asistente de IA especializado en el marco jurídico colombiano y los hitos del proyecto.
🚀 Parte 4 — Ruta de despliegue
Despliegue en Streamlit Community Cloud ⭐
Sube este repositorio a GitHub.
Ingresa a share.streamlit.io con tu cuenta de GitHub.
Haz clic en "New app" → selecciona este repositorio → app.py → Deploy.
Checklist de despliegue ✅
 Interfaz interactiva en 
app.py
 lista para ejecución y despliegue.
 La advertencia de la Parte 6/7 es visible en el encabezado de la aplicación.
 No hay API keys ni secretos en el código fuente.
⚖️ Parte 6 — Ética, datos y responsabilidad
Advertencia visible obligatoria. Implementada en el encabezado de la aplicación y en cada respuesta:
"Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un profesional del derecho."

 Implementada y visible en la interfaz 
app.py
.
Protección de datos (Ley 1581 de 2012). La herramienta no recolecta ni almacena datos personales reales.
 Verificado: sin bases de datos personales.
Corpus público. Solo fuentes públicas y oficiales colombianas.
 Verificado con leyes oficiales cargadas en el repositorio.
Anti-alucinaciones. Cita de normas y reconocimiento explícito cuando no hay información.
 Verificado en los casos de prueba 
casos-de-prueba.md
.
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
✅ Parte 8 — Entregables finales (Definition of Done)
 🔗 Solución funcionando: 
app.py
 funcional con advertencia visible y marco normativo.
 👤 Usuario real: evidencia documentada en 
evidencia-usuario.md
.
 📦 Repositorio estructurado: historial, corpus, prompts, casos de prueba y skill configurada.
 🧠 Análisis crítico: Parte 7 completada y fundamentada.
 📋 Partes 1–8 de este README completas y al día.
