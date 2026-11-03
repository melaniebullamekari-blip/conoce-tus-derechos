import os
import streamlit as st

st.set_page_config(
    page_title="Conoce tus Derechos — Sistema Jurídico Integral de Colombia",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- Estilos Visuales Personalizados -----------------
st.markdown("""
    <style>
    .main-title {
        color: #1E3A8A;
        font-weight: 800;
        font-size: 2.2rem;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #4B5563;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    .legal-alert {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 20px;
        color: #92400E;
        font-size: 0.95rem;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Advertencia Ética Visible Obligatoria -----------------
st.markdown('<h1 class="main-title">⚖️ Conoce tus Derechos</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Tu orientador jurídico ciudadano: compendio normativo integral de Colombia 🇨🇴</p>', unsafe_allow_html=True)

st.markdown("""
<div class="legal-alert">
    ⚠️ <strong>Advertencia legal visible:</strong> Esta herramienta es un ejercicio académico con fines exclusivamente pedagógicos e informativos. 
    <strong>No constituye asesoría jurídica formal ni sustituye la consulta con un profesional del derecho.</strong>
</div>
""", unsafe_allow_html=True)

# ----------------- Barra Lateral (Corpus Normativo Oficial) -----------------
with st.sidebar:
    st.header("📚 Compendio Legal Completo de Colombia")
    st.markdown("""
    Base jurídica nacional integrada:
    - 🏛️ **Constitución de 1991:** Íntegra (380 Arts., Tutela Art. 86)
    - 📚 **Códigos Nacionales:** Civil, Comercio, CGP, CPACA, Disciplinario
    - ⚖️ **Código Penal (Ley 599/00):** Dolo, culpa, homicidio, feminicidio, hurto
    - 🚔 **CPP (Ley 906/04):** Denuncia virtual, flagrancia, término 36h
    - 🛡️ **Violencia de Género (Ley 1257/08 y Ley 294/96):** Desalojo de agresor
    - 👨‍👩‍👧 **Familia e Infancia (Ley 1098/06 y Ley 2097/21):** Alimentos y REDAM
    - 🚗 **Tránsito (Ley 769/02 y Ley 2251/22):** Fotomultas C-038/20 y SOAT
    - 💼 **Código Sustantivo del Trabajo:** Despidos, liquidación y recargos
    - 💡 **Servicios Públicos (Ley 142/94):** Reclamos y silencio positivo
    - 💳 **Habeas Data (Ley 1266/08 y Ley 2157/21):** Datacrédito
    - 🏥 **Salud (Ley Estatutaria 1751/15):** Urgencias y medicamentos 48h
    - 🛒 **Consumidor (Ley 1480/11):** Garantías y retracto
    - 🏠 **Arrendamiento (Ley 820/03):** Topes IPC
    - 📋 **Petición (Ley 1755/15):** Términos de respuesta
    - 📞 **Ley "Dejen de Fregar" (Ley 2300/23):** Spam y cobranzas
    - ⚖️ **Sentencias Hito:** Eutanasia (C-233/21), Matrimonio (SU-214/16), IVE (C-055/22)
    - 🌐 **SUIN-JURISCOL:** 100% de leyes y decretos reglamentarios vigentes
    """)
    st.divider()
    st.subheader("🎓 Proyecto Académico")
    st.caption("Pontificia Universidad Javeriana · 2026-II")
    st.caption("Docente: Pedro Ardila")
    st.caption("Estudiantes: Melanie Bulla & Valeria Suarez")

# ----------------- Preguntas Frecuentes Rápidas -----------------
st.subheader("💡 Consultas Frecuentes por Áreas")
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

sample_query = None
with col1:
    if st.button("🏛️ Constitución y Tutela (Art. 86)"):
        sample_query = "¿Cuáles son los derechos fundamentales de la Constitución de 1991 y cómo funciona la Acción de Tutela en el Art. 86?"
with col2:
    if st.button("📜 Herencias en el Código Civil"):
        sample_query = "¿Cómo se dividen las herencias en Colombia según los órdenes hereditarios del Código Civil?"
with col3:
    if st.button("🚨 Robo a mano armada / Hurto"):
        sample_query = "Me robaron el celular en la calle con un arma, ¿cómo denuncio y qué delito es?"

with col4:
    if st.button("🛡️ Violencia intrafamiliar y desalojo"):
        sample_query = "Mi pareja me agredió físicamente y me insulta, ¿cómo pido el desalojo en Comisaría de Familia?"
with col5:
    if st.button("⚖️ Dolo, culpa y legítima defensa"):
        sample_query = "¿Cuál es la diferencia entre dolo, culpa, preterintención y legítima defensa en el Código Penal?"
with col6:
    if st.button("🌐 Buscar leyes en SUIN-JURISCOL"):
        sample_query = "¿Cómo consultar cualquier ley, decreto o código oficial de Colombia en SUIN-JURISCOL?"

# ----------------- Gestión del Chat -----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "¡Hola! Soy tu asistente de **Conoce tus Derechos**. Tengo integrado el compendio de todo el ordenamiento jurídico colombiano: **Constitución de 1991 (380 artículos), Códigos Nacionales (Civil, Comercio, Penal, Laboral, General del Proceso, Administrativo, Policía, Tránsito), sentencias hito de la Corte Constitucional y la conexión directa a SUIN-JURISCOL**. Describe tu caso en lenguaje común y te orientaré con las normas exactas."
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Escribe tu pregunta sobre cualquier ley, código, decreto, sentencia o caso...")
if sample_query:
    user_input = sample_query

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    lower = user_input.lower()
    resp_text = ""

    # 1. Constitución Política de 1991
    if "constitucion" in lower or "constitución" in lower or "artículo 86" in lower or "articulo 86" in lower or "tutela" in lower or "articulo 29" in lower or "articulo 11" in lower or "articulo 13" in lower or "derechos fundamentales" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

La **Constitución Política de 1991** es la norma de normas de Colombia (Art. 4 C.P.):

### 🏛️ Principios y Artículos Fundamentales:
* **Artículo 1:** Colombia es un **Estado social de derecho** fundado en la dignidad humana y el trabajo.
* **Artículo 11:** El derecho a la vida es inviolable. No habrá pena de muerte.
* **Artículo 13:** Derecho a la igualdad real y efectiva; prohibición de discriminación.
* **Artículo 15:** Intimidad personal, buen nombre y **Habeas Data**. Inviolabilidad de comunicaciones privadas.
* **Artículo 23:** **Derecho de Petición** respetuoso ante autoridades con respuesta oportuna.
* **Artículo 29:** **Debido Proceso:** Presunción de inocencia, defensa técnica y nulidad absoluta de pruebas ilícitas.
* **Artículo 86 — Acción de Tutela:** Amparo preferente e inmediato ante cualquier juez para proteger derechos fundamentales en 10 días, sin abogado y gratuito.
* **Artículo 93:** **Bloque de Constitucionalidad:** Prevalencia de tratados internacionales de derechos humanos en el orden interno.
        """
    # 2. Código Civil: Herencias, Posesión, Contratos
    elif "código civil" in lower or "codigo civil" in lower or "herencia" in lower or "sucesión" in lower or "sucesion" in lower or "posesión" in lower or "posesion" in lower or "usucapion" in lower or "usucapión" in lower or "servidumbre" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

El **Código Civil Colombiano (Ley 84 de 1873)** rige el derecho privado de las personas, bienes y contratos:

### 📜 Reglas Esenciales:
1. **Órdenes Hereditarios (Sucesiones):**
   * 1.er orden: Hijos legítimos, adoptivos o extramatrimoniales por partes iguales.
   * 2.do orden: Ascendientes (padres/abuelos) y cónyuge o compañero permanente.
   * 3.er orden: Hermanos y cónyuge/compañero permanente.
   * 4.to orden: Sobrinos.
   * 5.to orden: Instituto Colombiano de Bienestar Familiar (ICBF).
2. **Posesión y Usucapión (Art. 762 CC y Ley 791/02):** La tenencia con ánimo de señor y dueño permite adquirir el dominio por prescripción extraordinaria a los **10 años** (o 5 años ordinaria con justo título).
3. **Contratos (Art. 1602 CC):** Todo contrato válidamente celebrado es una ley para las partes (*Pacta sunt servanda*).
4. **Responsabilidad Civil Extracontractual (Art. 2341 CC):** El que cometa un daño con dolo o culpa debe indemnizarlo íntegramente.
        """
    # 3. Código de Comercio, Sociedades S.A.S. y Títulos Valores
    elif "código de comercio" in lower or "codigo de comercio" in lower or "comercio" in lower or "sociedad" in lower or "s.a.s" in lower or "sas" in lower or "título valor" in lower or "titulo valor" in lower or "letra de cambio" in lower or "pagaré" in lower or "pagare" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

El régimen mercantil se regula por el **Código de Comercio (Decreto 410 de 1971)**:

### 🏢 Elementos Clave del Comercio:
1. **Sociedades por Acciones Simplificadas — S.A.S. (Ley 1258 de 2008):** Se crean por documento privado ante Cámara de Comercio, admiten accionista único y blindan el patrimonio personal limitando la responsabilidad a los aportes.
2. **Títulos Valores (Arts. 619 y ss.):** Letras, pagarés y cheques contienen compromisos autónomos y exigibles. Permiten cobro coactivo inmediato mediante **Proceso Ejecutivo (CGP)** con medidas de embargo de cuentas y bienes.
3. **Prescripción de la acción cambiaria:** La acción ejecutiva derivada de una letra o pagaré prescribe a los **tres (3) años** desde el vencimiento.
        """
    # 4. Sentencias Hito Corte Constitucional
    elif "sentencia" in lower or "jurisprudencia" in lower or "eutanasia" in lower or "muerte digna" in lower or "c-233" in lower or "c-221" in lower or "dosis mínima" in lower or "dosis minima" in lower or "matrimonio igualitario" in lower or "su-214" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Líneas jurisprudenciales hito de la **Corte Constitucional de Colombia**:

### ⚖️ Sentencias Vinculantes Trascendentales:
* **Eutanasia y Muerte Digna (Sentencias C-239/97 y C-233/21):** Derecho a la muerte médicamente asistida ante lesión o enfermedad grave e incurable que genere intensos sufrimientos físicos o psíquicos, sin exigir que sea terminal.
* **Dosis Mínima (Sentencia C-221 de 1994):** En aplicación del libre desarrollo de la personalidad (Art. 16 C.P.), no se criminaliza el consumo ni el porte personal de estupefacientes.
* **Matrimonio Igualitario (Sentencia SU-214 de 2016):** Derecho pleno al matrimonio civil para parejas del mismo sexo ante jueces y notarios.
* **Estados de Cosas Inconstitucionales (ECI):** Declarados ante fallas masivas en desplazamiento forzado (T-025/04), sistema de salud (T-760/08) y hacinamiento carcelario (T-388/13).
        """
    # 5. Demandas al Estado y CPACA
    elif "cpaca" in lower or "demandar al estado" in lower or "reparación directa" in lower or "reparacion directa" in lower or "nulidad y restablecimiento" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Las demandas contra el Estado se rigen por el **CPACA (Ley 1437 de 2011)** y el Art. 90 de la Carta Política:

### 🏛️ Medios de Control Contencioso Administrativo:
1. **Reparación Directa (Art. 140 CPACA):** Indemnización por daños antijurídicos imputables al Estado (fallas en el servicio médico público, accidentes por mal estado vial, privación injusta de la libertad). Caducidad: **dos (2) años** desde el hecho.
2. **Nulidad y Restablecimiento del Derecho (Art. 138 CPACA):** Para anular actos administrativos particulares y solicitar reintegro o pago de salarios. Caducidad: **cuatro (4) meses**.
3. **Vía Gubernativa:** Recursos de reposición y apelación dentro de los 10 días hábiles posteriores a la notificación.
        """
    # 6. SUIN-JURISCOL y Buscadores Oficiales
    elif "suin" in lower or "juriscol" in lower or "decreto" in lower or "todas las leyes" in lower or "buscador de leyes" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Para consultar el 100% de la legislación, decretos y códigos vigentes en Colombia:

### 🌐 Plataformas Oficiales Estatales:
1. **SUIN-JURISCOL (MinJusticia):** [suin-juriscol.gov.co](http://www.suin-juriscol.gov.co) — Repositorio oficial con todas las leyes y Decretos Únicos Reglamentarios (DUR) desde 1886 con análisis de vigencia.
2. **Relatoría de la Corte Constitucional:** [corteconstitucional.gov.co/relatoria](https://www.corteconstitucional.gov.co/relatoria/) — Todas las sentencias C, T y SU completas.
3. **LegalApp:** [legalapp.gov.co](https://www.legalapp.gov.co) — Directorio de trámites y autoridades competentes.
        """
    # 7. Dolo, Culpa, Preterintención, Legítima Defensa
    elif "dolo" in lower or "culpa" in lower or "preterintencion" in lower or "preterintención" in lower or "legítima defensa" in lower or "legitima defensa" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

En el **Código Penal Colombiano (Ley 599 de 2000)**, la responsabilidad penal exige culpabilidad (Art. 9 CP):
* **Dolo (Art. 22 CP):** Conocer los hechos y querer directamente la conducta punible (directo) o aceptarla como probable (eventual).
* **Culpa (Art. 23 CP):** Imprudencia, negligencia, impericia o violación del deber de cuidado (accidentes viales, mala praxis).
* **Preterintención (Art. 24 CP):** El resultado dañoso excede la intención del autor (ej. golpear para lesionar pero causar la muerte).
* **Legítima Defensa (Art. 32 Num. 6 CP):** Repeler una agresión ilegítima, actual e inminente de forma proporcional; se presume legal ante intrusos en vivienda o vehículo habitado.
        """
    # 8. Homicidio, Muerte, Asesinato, Feminicidio
    elif "matar" in lower or "muerte" in lower or "homicidio" in lower or "asesinato" in lower or "feminicidio" in lower or "sicariato" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Delitos contra la vida humana en el **Código Penal (Ley 599 de 2000)**:
* **Homicidio Simple (Art. 103 CP):** Pena de 208 a 450 meses de cárcel (17.3 a 37.5 años).
* **Homicidio Agravado (Art. 104 CP):** Hasta 50 o 60 años por sevicia, sicariato, para ocultar otro delito o contra cónyuge/familiares.
* **Feminicidio (Art. 104A CP - Ley Rosa Elvira Cely):** Asesinato de una mujer por razones de género o antecedentes de violencia. Pena de 250 a 500 meses sin rebajas ni preacuerdos.
* **Canales de Denuncia:** Línea 122 (Fiscalía), Línea 123 (Policía Nacional) y URI presencial 24/7.
        """
    # 9. Hurto, Robo, Atraco, Extorsión, Estafa, Escopolamina
    elif "robo" in lower or "robaron" in lower or "hurto" in lower or "atraco" in lower or "estafa" in lower or "extorsión" in lower or "extorsion" in lower or "escopolamina" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Delitos patrimoniales en el **Código Penal (Ley 599 de 2000)**:
* **Hurto Calificado (Art. 240 CP):** Con violencia contra personas, armas, o colocando a la víctima en **indefensión (escopolamina o tóxicos)**. Investigable de oficio.
* **Hurto Agravado (Art. 241 CP):** Si participan 2 o más personas o en transporte público.
* **Estafa (Art. 246 CP):** Provecho ilícito mediante engaños y artificios.
* **Extorsión (Art. 244 CP):** Chantajes y amenazas. GAULA Línea 165.
* **Denuncia virtual 24/7:** [adenunciar.policia.gov.co](https://adenunciar.policia.gov.co). Término de 36 horas para control de captura (Art. 302 CPP).
        """
    # 10. Violencia Intrafamiliar y de Género
    elif "violencia" in lower or "agredió" in lower or "agredio" in lower or "golpeó" in lower or "golpeo" in lower or "maltrato" in lower or "intrafamiliar" in lower or "desalojo" in lower or "comisaría" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Violencia sancionada por el **Art. 229 del Código Penal** y la **Ley 1257 de 2008**:
* **Medidas en Comisaría de Familia en menos de 4 horas (Ley 294/96 y 2126/21):** Desalojo inmediato del agresor de la vivienda familiar, orden de alejamiento, pensión provisional de alimentos y protección policial.
* **Líneas 24/7:** Línea 155 (Orientación a Mujeres), Línea 123 (Emergencias), Línea 122 (Fiscalía) y Línea Púrpura (018000 112 137).
        """
    # 11. Alimentos, REDAM
    elif "alimento" in lower or "cuota alimentaria" in lower or "pensión alimenticia" in lower or "hijos" in lower or "redam" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Alimentos regulados por el **Código de la Infancia y la Adolescencia (Ley 1098 de 2006)**:
* **Fijación gratuita:** Audiencia ante ICBF o Comisaría. El acta tiene **mérito ejecutivo**.
* **Embargo:** Hasta el **50% de salario y prestaciones** por alimentos (Art. 130).
* **REDAM (Ley 2097 de 2021):** Al acumular 3 cuotas en mora, se prohíbe salir del país, contratar con el Estado y recibir créditos financieros.
        """
    # 12. Tránsito: Fotomultas, Choques, Accidentes, SOAT
    elif "fotomulta" in lower or "fotodetección" in lower or "accidente de tránsito" in lower or "choque" in lower or "soat" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Tránsito amparado en la **Ley 769 de 2002** y fallos constitucionales:
* **Fotomultas (Sentencia C-038 de 2020):** Deben individualizar y probar quién conducía. No pueden multar automáticamente al propietario. Notificación en 3 días hábiles.
* **Choques simples (Ley 2251 de 2022):** No se espera a la policía; se toman fotos/videos de prueba y se retiran los autos de inmediato.
* **SOAT (Ley 2161 de 2021):** Atención médica y hospitalaria incondicional sin copagos para todas las víctimas.
        """
    # 13. Laboral: Despido, Liquidación, Recargos
    elif "trabajo" in lower or "laboral" in lower or "despido" in lower or "liquidación" in lower or "liquidacion" in lower or "prima" in lower or "cesantías" in lower or "acoso laboral" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Derechos laborales en el **Código Sustantivo del Trabajo (CST)** y **Ley 2101 de 2021**:
* **Despido sin justa causa (Art. 64 CST):** Indemnización económica obligatoria.
* **Mora en liquidación (Art. 65 CST):** Un día de salario por cada día de retraso del empleador (hasta por 24 meses).
* **Prestaciones de ley:** Prima (junio y diciembre), Cesantías en fondo, intereses y 15 días hábiles de vacaciones.
        """
    # 14. Servicios Públicos
    elif "servicio público" in lower or "servicios publicos" in lower or "factura" in lower or "recibo" in lower or "luz" in lower or "agua" in lower or "gas" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Servicios públicos domiciliarios bajo la **Ley 142 de 1994**:
* **Desviaciones de consumo (Art. 149):** Obligación de investigar anomalías antes de cobrar.
* **Prohibición de corte (Art. 155):** No pueden suspender el servicio por cobros que estén en reclamación formal.
* **Silencio Positivo (Art. 158):** Si tardan más de 15 días hábiles en responder, se anula el cobro por ley.
        """
    # 15. Datacrédito y Centrales de Riesgo
    elif "datacrédito" in lower or "datacredito" in lower or "cifin" in lower or "centrales de riesgo" in lower or "reporte negativo" in lower or "deuda" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Historial crediticio bajo la **Ley 1266 de 2008** y **Ley 2157 de 2021 ("Borrón y Cuenta Nueva")**:
* **Aviso previo de 20 días calendario (Art. 12):** Sin este aviso el reporte es ilegal.
* **Permanencia (Art. 13):** Máximo el doble de la mora (tope 4 años tras pagar) o caducidad definitiva a los 8 años.
        """
    # 16. Salud y Medicamentos
    elif "salud" in lower or "eps" in lower or "medicamento" in lower or "urgencias" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría médica ni jurídica formal.*

Salud fundamental bajo la **Ley Estatutaria 1751 de 2015**:
* **Urgencias (Arts. 10 y 14):** Atención incondicional sin copagos ni autorizaciones.
* **Medicamentos en 48 horas (Res. 1604/13):** Plazo perentorio para la EPS.
        """
    # 17. Ley Dejen de Fregar
    elif "llamada" in lower or "cobranza" in lower or "spam" in lower or "dejen de fregar" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Cobranza bajo la **Ley 2300 de 2023 ("Ley Dejen de Fregar")**:
* **Horarios:** Lunes a viernes de 7am a 7pm, sábados de 8am a 3pm. **Domingos y festivos prohibidos.** Máximo 2 contactos semanales.
        """
    # 18. Arrendamiento y Consumidor
    elif "arriendo" in lower or "consumidor" in lower or "garantía" in lower or "retracto" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

* **Arrendamiento (Ley 820 de 2003):** Incremento solo cada 12 meses tope 100% IPC anterior. Prohibidos depósitos en dinero.
* **Consumidor (Ley 1480 de 2011):** Garantía legal para cambio o dinero, y retracto de 5 días en ventas virtuales.
        """
    # 19. IVE
    elif "abortar" in lower or "ive" in lower or "embarazo" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría médica ni jurídica formal.*

Interrupción Voluntaria del Embarazo amparada en la **Sentencia C-055 de 2022**:
* Libre hasta la semana 24 de gestación; posterior a la semana 24 aplican las 3 causales de la Sentencia C-355 de 2006. Atención gratuita en EPS en 5 días (Res. 051/23).
        """
    # 20. Nacionalidad y Retención
    elif "nacionalidad" in lower or "venezuela" in lower or "pasaporte" in lower or "caballo" in lower or "retención" in lower or "retencion" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

* **Nacionalidad (Art. 96 C.P. y Ley 43/93):** Criterio mixto (Ius sanguinis e Ius domicilii) y doble nacionalidad. Medida Primero la Niñez para hijos de venezolanos.
* **Retención de bienes/animales (Art. 2417 Código Civil):** No transfiere propiedad; los animales son seres sintientes protegidos por la Ley 1774 de 2016.
        """
    else:
        resp_text = f"""
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

He analizado tu consulta jurídica sobre: *"{user_input}"*.

En el ordenamiento jurídico de Colombia:
1. **Marco normativo aplicable:** Tus derechos están amparados por la **Constitución Política de 1991** y los Códigos Nacionales sustantivos y procesales de la República.
2. **Consulta oficial abierta:** Para verificar la vigencia de cualquier norma específica, decreto reglamentario o jurisprudencia, puedes ingresar al portal oficial **[SUIN-JURISCOL](http://www.suin-juriscol.gov.co)** del Ministerio de Justicia.
3. **Apoyo gratuito:** Consulta en **[LegalApp](https://www.legalapp.gov.co)** o acude al **Consultorio Jurídico de la Pontificia Universidad Javeriana** para atención personalizada.
        """

    with st.chat_message("assistant"):
        st.markdown(resp_text)
    st.session_state.messages.append({"role": "assistant", "content": resp_text})
