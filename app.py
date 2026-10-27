import os
import streamlit as st

st.set_page_config(
    page_title="Conoce tus Derechos — Asistente Jurídico Integral",
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
st.markdown('<p class="sub-title">Tu orientador jurídico ciudadano: claridad y respaldo legal integral (Colombia 🇨🇴)</p>', unsafe_allow_html=True)

st.markdown("""
<div class="legal-alert">
    ⚠️ <strong>Advertencia legal visible:</strong> Esta herramienta es un ejercicio académico con fines exclusivamente pedagógicos e informativos. 
    <strong>No constituye asesoría jurídica formal ni sustituye la consulta con un profesional del derecho.</strong>
</div>
""", unsafe_allow_html=True)

# ----------------- Barra Lateral (Corpus Normativo Oficial) -----------------
with st.sidebar:
    st.header("📚 Corpus Normativo Oficial (17 Fuentes)")
    st.markdown("""
    Base jurídica colombiana verificada:
    - 🏛️ **Constitución Política de 1991** (Arts. 15, 23, 74, 86, 96)
    - ⚖️ **Código Penal (Ley 599/00):** Dolo, culpa, homicidio, feminicidio, hurto, estafa
    - 🚔 **Código de Procedimiento Penal (Ley 906/04):** Denuncia, flagrancia, término 36h
    - 🛡️ **Ley 1257 de 2008 y Ley 294/96:** Violencia intrafamiliar y medidas de protección
    - 👨‍👩‍👧 **Ley 1098 de 2006 y Ley 2097/21:** Alimentos, inasistencia y REDAM
    - 🚗 **Ley 769 de 2002 y Ley 2251/22:** Fotomultas, accidentes y SOAT
    - 💼 **Código Sustantivo del Trabajo:** Despidos, liquidación, recargos y acoso
    - 💡 **Ley 142 de 1994:** Servicios públicos y reclamos
    - 💳 **Ley 1266/08 y Ley 2157/21:** Datacrédito y Habeas Data
    - 🏥 **Ley Estatutaria 1751 de 2015:** Salud y medicamentos
    - 🛒 **Ley 1480 de 2011:** Consumidor y garantías
    - 🏠 **Ley 820 de 2003:** Arrendamiento urbano
    - 📋 **Ley 1755 de 2015:** Derecho de petición
    - 📞 **Ley 2300 de 2023:** Ley "Dejen de Fregar" (Spam/Cobranza)
    - 🇨🇴 **Ley 43 de 1993:** Nacionalidad colombiana
    - 👮 **Ley 1801 de 2016:** Código de Policía
    - ⚖️ **Sentencia C-055 de 2022:** IVE
    """)
    st.divider()
    st.subheader("🎓 Proyecto Académico")
    st.caption("Pontificia Universidad Javeriana · 2026-II")
    st.caption("Docente: Pedro Ardila")
    st.caption("Estudiantes: Melanie Bulla & Valeria Suarez")

# ----------------- Preguntas Frecuentes Rápidas -----------------
st.subheader("💡 Consultas Frecuentes Rápidas")
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

sample_query = None
with col1:
    if st.button("🚨 Fui víctima de robo / hurto"):
        sample_query = "Me robaron el celular en la calle con un cuchillo, ¿cómo denuncio y qué delito es en Colombia?"
with col2:
    if st.button("🛡️ Violencia intrafamiliar y desalojo"):
        sample_query = "Mi pareja me agredió físicamente y me insulta, ¿cómo pido que lo desalojen de la casa en la Comisaría?"
with col3:
    if st.button("⚖️ Homicidio, dolo vs culpa y legítima defensa"):
        sample_query = "¿Cuál es la diferencia entre dolo, culpa, preterintención y legítima defensa en el Código Penal?"

with col4:
    if st.button("👨‍👩‍👧 Demanda de alimentos y REDAM"):
        sample_query = "¿Cómo fijo la cuota de alimentos de mis hijos y qué consecuencias tiene el reporte en el REDAM?"
with col5:
    if st.button("🚗 Fotomultas y choques de tránsito"):
        sample_query = "¿Cómo impugno una fotomulta si yo no iba conduciendo y qué hacer en un choque simple?"
with col6:
    if st.button("💼 Despido y liquidación laboral"):
        sample_query = "Me despidieron de mi trabajo sin justa causa, ¿qué indemnización y liquidación me corresponde?"

# ----------------- Gestión del Chat -----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "¡Hola! Soy tu asistente de **Conoce tus Derechos**. Puedes consultarme sobre **robos, delitos penales (dolo, culpa, legítima defensa), homicidios, feminicidios, violencia intrafamiliar, cuota de alimentos, accidentes y fotomultas, despidos laborales, servicios públicos, datacrédito, salud, arriendo o trámites públicos**. Describe tu caso en lenguaje común y te orientaré con las leyes colombianas aplicables."
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Escribe tu pregunta jurídica sobre cualquier tema aquí...")
if sample_query:
    user_input = sample_query

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    lower = user_input.lower()
    resp_text = ""

    # 1. Delitos Penales: Dolo, Culpa, Preterintención, Legítima Defensa
    if "dolo" in lower or "culpa" in lower or "preterintencion" in lower or "preterintención" in lower or "legítima defensa" in lower or "legitima defensa" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

En el **Código Penal Colombiano (Ley 599 de 2000)**, la responsabilidad penal exige culpabilidad (Art. 9 CP):

### ⚖️ 1. Formas de Culpabilidad:
* **Dolo (Art. 22 CP):** Se configura cuando la persona **conoce los hechos delictivos y quiere su realización** (dolo directo), o cuando los prevé como probables y los acepta (dolo eventual).
* **Culpa (Art. 23 CP):** El resultado punible ocurre por **imprudencia, negligencia, impericia o violación de deberes objetivos de cuidado**, habiendo sido previsible (por ejemplo, accidentes de tránsito por exceso de velocidad o negligencia médica).
* **Preterintención (Art. 24 CP):** El resultado **excede la intención del autor**. Por ejemplo, quien propina un golpe con la sola intención de causar una lesión menor, pero la persona cae y fallece (Homicidio Preterintencional - Art. 105 CP).

### 🛡️ 2. Legítima Defensa (Art. 32 Num. 6 CP):
Es una causal de **ausencia de responsabilidad penal** cuando una persona obra en necesidad de defender un derecho propio o ajeno contra una agresión ilegítima, actual o inminente, con proporcionalidad en el medio.
* **Legítima defensa privilegiada:** Se presume legal defenderse frente a quien pretenda penetrar indebidamente a la vivienda o vehículo habitado.
        """
    # 2. Homicidio, Muerte, Asesinato, Feminicidio
    elif "matar" in lower or "muerte" in lower or "homicidio" in lower or "asesinato" in lower or "feminicidio" in lower or "cadáver" in lower or "sicariato" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Los delitos contra la vida humana son los más graves del ordenamiento jurídico colombiano (**Código Penal - Ley 599 de 2000**):

### 🚨 Tipificación y Sanciones:
1. **Homicidio Simple (Art. 103 CP):** Prisión de 208 a 450 meses (17.3 a 37.5 años).
2. **Homicidio Agravado (Art. 104 CP):** Pena de hasta 50 o 60 años de cárcel cuando se comete con sevicia, contra familiares/cónyuge, para ocultar otro delito, por precio o recompensa (sicariato), o colocando a la víctima en indefensión.
3. **Feminicidio (Art. 104A CP - Ley 1761 de 2015 "Rosa Elvira Cely"):** Causar la muerte a una mujer por su condición de ser mujer o por motivos de identidad de género (con antecedentes de violencia familiar, relaciones de poder, mutilaciones o exposición del cuerpo). Pena de 250 a 500 meses de prisión sin rebaja de penas.
4. **Homicidio Culposo (Art. 109 CP):** Muerte causada por negligencia o impericia (típico en accidentes de tránsito o impericia profesional).

### ⚡ Canales Urgentes:
* **Denuncia inmediata:** Línea 122 (Fiscalía), Línea 123 (Policía Nacional) o URI de turno presencial.
* **Medicina Legal:** Dictamina la causa de muerte y protocolo de necropsia para el juicio oral.
        """
    # 3. Hurto, Robo, Atraco, Escopolamina, Extorsión, Estafa
    elif "robo" in lower or "robaron" in lower or "hurto" in lower or "atraco" in lower or "estafa" in lower or "extorsión" in lower or "extorsion" in lower or "escopolamina" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Los delitos patrimoniales se tipifican en el **Código Penal (Ley 599 de 2000)**:

### 💼 Clasificación del delito:
1. **Hurto Calificado (Art. 240 CP):** Ocurre cuando se usa **violencia sobre las personas**, armas, o se coloca a la víctima en **indefensión** (mediante escopolamina o somníferos), o con ruptura de cerraduras o escalamiento. Es delito investigable de oficio.
2. **Hurto Agravado (Art. 241 CP):** Se agrava si participan 2 o más personas, si es en transporte público o sobre vehículos automotores.
3. **Estafa (Art. 246 CP):** Obtener dinero o bienes induciendo a la víctima en error mediante engaños o artificios (ventas fraudulentas, pirámides).
4. **Extorsión (Art. 244 CP):** Constreñimiento o amenaza para exigir pagos indebidos. **Denuncia prioritaria ante el GAULA en la Línea 165.**

### 📲 ¿Cómo denunciar de inmediato?:
* Radica tu denuncia 24/7 en el portal virtual conjunto de Fiscalía y Policía: **[adenunciar.policia.gov.co](https://adenunciar.policia.gov.co)**.
* Si hubo capturado en flagrancia, la policía dispone de un término constitucional estricto de **36 horas** para presentarlo ante el Juez de Control de Garantías (Art. 302 CPP).
* Puedes reclamar indemnización a través del **Incidente de Reparación Integral (Art. 102 CPP)**.
        """
    # 4. Violencia Intrafamiliar, Violencia contra la Mujer, Golpes, Agresión
    elif "violencia" in lower or "agredió" in lower or "agredio" in lower or "golpeó" in lower or "golpeo" in lower or "maltrato" in lower or "intrafamiliar" in lower or "desalojo" in lower or "comisaría" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

La violencia intrafamiliar y contra la mujer es un delito prioritario sancionado por el **Art. 229 del Código Penal** y la **Ley 1257 de 2008**:

### 🛡️ Medidas Urgentes de Protección (Ley 294/96 y Ley 2126/21):
Acude a la **Comisaría de Familia** más cercana (o Juzgado Municipal). El comisario puede expedir en menos de 4 horas:
1. **Desalojo inmediato del agresor:** El agresor debe abandonar inmediatamente el hogar compartido con la víctima, sin importar de quién sea la vivienda.
2. **Orden de alejamiento:** Prohibición estricta de acercarse a tu casa, trabajo o comunicarse contigo por llamadas o redes sociales.
3. **Pensión provisional de alimentos:** Fijación de cuota para sustento de hijos y cónyuge.
4. **Acompañamiento policial y custodia provisional:** Protección para retirar pertenencias personales y custodia inmediata de menores.

### 🚨 Líneas de Auxilio Gratuito 24/7:
* 📞 **Línea 155:** Orientación nacional a mujeres víctimas de violencia.
* 🚨 **Línea 123:** Emergencias con patrulla policial inmediata.
* ⚖️ **Línea 122:** Fiscalía General de la Nación para denuncia penal (delito no desistible ni conciliable).
* 🟣 **Línea Púrpura:** 018000 112 137 o WhatsApp 300 755 1846.
        """
    # 5. Familia: Alimentos, Pensión, REDAM, Custodia
    elif "alimentos" in lower or "cuota alimentaria" in lower or "pensión alimenticia" in lower or "hijos" in lower or "redam" in lower or "patria potestad" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

El derecho de alimentos en favor de los hijos se regula por el **Código de la Infancia y la Adolescencia (Ley 1098 de 2006)**:

### 👨‍👩‍👧 1. Fijación de la Cuota (Trámite Gratuito sin Abogado):
* Solicita audiencia de conciliación ante el **ICBF**, la **Comisaría de Familia** o la **Personería Municipal**.
* El acta de conciliación presta **mérito ejecutivo**: si el obligado incumple tan solo una cuota, se pueden embargar sus cuentas y bienes directamente ante un juez de familia.
* **Tope de embargo:** La ley permite embargar **hasta el 50% de todo el salario y prestaciones sociales** (incluidas cesantías y primas) para responder por alimentos (Art. 130).

### 🚫 2. Sanciones por Incumplimiento:
1. **Delito de Inasistencia Alimentaria (Art. 233 CP):** Prisión de 16 a 54 meses.
2. **Reporte en el REDAM (Ley 2097 de 2021):** Si adeuda 3 cuotas, se inscribe en el Registro de Deudores Alimentarios Morosos, acarreando:
   * **Prohibición de salir del país** (Migración Colombia impide la salida).
   * **Prohibición de contratar con el Estado** o asumir cargos públicos.
   * **Bloqueo de créditos financieros** e impedimento para traspasar vehículos o inmuebles.
        """
    # 6. Tránsito: Fotomultas, Choques, Accidentes, SOAT
    elif "fotomulta" in lower or "fotodetección" in lower or "accidente de tránsito" in lower or "choque" in lower or "soat" in lower or "comparendo" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

El régimen de tránsito se rige por la **Ley 769 de 2002**, la **Ley 2251 de 2022** y la jurisprudencia constitucional:

### 🚗 1. Fotomultas (Sentencia C-038 de 2020 de la Corte Constitucional):
* **Identificación obligatoria del infractor:** Está prohibido multar automáticamente al dueño del carro. La secretaría de tránsito **debe probar quién iba conduciendo** al momento de la infracción.
* **Término de notificación:** Deben notificarte dentro de los **3 días hábiles** siguientes a la validación del comparendo. Si no fuiste notificado debidamente, puedes solicitar audiencia y pedir la revocatoria directa por violación al debido proceso.

### 💥 2. Choques Simples (Ley 2251 de 2022 - Ley Julián Esteban):
* Si en el choque solo hubo daños materiales ("latas"), **NO es necesario esperar al agente de tránsito ni policía**.
* Los conductores deben tomar fotos/videos de los daños y retirar los carros de inmediato para no obstaculizar la vía. Las aseguradoras resuelven con las pruebas recaudadas.

### 🏥 3. Accidentes con Lesionados (Cobertura SOAT - Ley 2161 de 2021):
* El SOAT cubre automáticamente y sin excepciones a todas las víctimas (peatones, ciclistas, pasajeros). Ninguna clínica puede condicionar la atención de urgencias a copagos ni autorizaciones.
        """
    # 7. Laboral: Despido, Liquidación, Recargos, Acoso
    elif "trabajo" in lower or "laboral" in lower or "despido" in lower or "liquidación" in lower or "liquidacion" in lower or "prima" in lower or "cesantías" in lower or "horas extras" in lower or "acoso laboral" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Tus derechos laborales se fundamentan en el **Código Sustantivo del Trabajo (CST)** y la **Ley 2101 de 2021**:
1. **Despido sin justa causa (Art. 64 CST):** Da derecho a indemnización económica obligatoria.
2. **Sanción por no pago de liquidación (Art. 65 CST):** El empleador debe pagar la liquidación completa al terminar el contrato. Por cada día de mora, debe pagarte **un día de salario** (hasta por 24 meses).
3. **Prestaciones de ley:** Prima de servicios (junio y diciembre), Cesantías en fondo (antes del 15 de febrero), intereses (12% en enero) y 15 días hábiles de vacaciones por año.
4. **Jornada y recargos:** Reducción de jornada laboral semanal por Ley 2101/21. Recargo nocturno (35%) y festivo/dominical (75%).
        """
    # 8. Servicios Públicos Domiciliarios
    elif "servicio público" in lower or "servicios publicos" in lower or "factura" in lower or "recibo" in lower or "luz" in lower or "agua" in lower or "gas" in lower or "corte" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Los servicios públicos domiciliarios se rigen por la **Ley 142 de 1994**:
1. **Desviaciones de consumo (Art. 149):** La empresa debe investigar técnicamente anomalías en el contador antes de cobrar sumas desmedidas. Solo pagas tu promedio histórico.
2. **Prohibición de corte (Art. 155):** No pueden suspender el servicio por cobros que estén en trámite de reclamación formal.
3. **Recursos legales (Art. 154):** Si rechazan el reclamo, interpon **Recurso de Reposición y en subsidio de Apelación** ante la **Superservicios**.
4. **Silencio Administrativo Positivo (Art. 158):** Si tardan más de 15 días hábiles en responder, ganas automáticamente por ley.
        """
    # 9. Datacrédito / Centrales de Riesgo
    elif "datacrédito" in lower or "datacredito" in lower or "cifin" in lower or "centrales de riesgo" in lower or "reporte negativo" in lower or "deuda" in lower or "suplantación" in lower or "suplantacion" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Tu historial crediticio está amparado por la **Ley 1266 de 2008** y la **Ley 2157 de 2021 ("Borrón y Cuenta Nueva")**:
1. **Aviso previo de 20 días calendario (Art. 12):** Sin este aviso formal previo, el reporte es ilegal y puedes exigir su retiro.
2. **Permanencia del reporte (Art. 13):** Máximo el doble del tiempo de la mora (tope 4 años tras pagar) o caducidad definitiva a los 8 años sin necesidad de pagar.
3. **Suplantación de identidad:** Con copia de la denuncia penal ante Fiscalía, la entidad debe suspender el reporte negativo en 10 días y colocar leyenda de víctima de falsedad.
        """
    # 10. Salud y Medicamentos
    elif "salud" in lower or "eps" in lower or "medicamento" in lower or "urgencias" in lower or "medico" in lower or "médico" in lower or "cirugía" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría médica ni jurídica formal.*

La salud es un derecho fundamental irrenunciable amparado por la **Ley Estatutaria 1751 de 2015**:
1. **Atención de urgencias incondicional (Arts. 10 y 14):** Ningún hospital puede negar urgencias o exigir copagos o autorizaciones previas.
2. **Entrega de medicamentos en 48 horas (Res. 1604/13):** Plazo máximo para entrega de medicamentos formulados.
3. **Mecanismos:** Queja ante la **Supersalud** (018000 513700) o **Acción de Tutela con solicitud de medida provisional** ante cualquier juez.
        """
    # 11. Llamadas Spam / Cobranza
    elif "llamada" in lower or "cobranza" in lower or "spam" in lower or "dejen de fregar" in lower or "banco llama" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Las gestiones de cobro comercial están reguladas por la **Ley 2300 de 2023 ("Ley Dejen de Fregar")**:
1. **Horarios estrictos (Art. 3):** Lunes a viernes de 7am a 7pm, sábados de 8am a 3pm. **Domingos y festivos está totalmente prohibido.**
2. **Periodicidad:** Máximo 2 contactos por semana por entidad.
3. **Prohibición a referencias:** No pueden contactar a tus familiares ni amigos para indagar sobre tu deuda.
        """
    # 12. Petición Ciudadana
    elif "petición" in lower or "peticion" in lower or "no responde" in lower or "entidad pública" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Si una entidad pública no respondió dentro de los términos legales, se vulnera tu **Derecho de Petición** (Art. 23 C.P. y Ley 1755 de 2015):
* **Términos:** 10 días hábiles (documentos), 15 días (interés general), 30 días (consultas jurídicas).
* **Acciones:** Acción de Tutela (Art. 86 C.P.), Silencio Administrativo Positivo para copias (Art. 14) o queja ante Personería y Procuraduría.
        """
    # 13. Arrendamiento
    elif "arriendo" in lower or "arrendamiento" in lower or "canon" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

En Colombia, el arrendamiento de vivienda se rige por la **Ley 820 de 2003**:
* **Incremento (Art. 20):** Solo cada 12 meses y máximo el 100% de la inflación (IPC) del año anterior.
* **Prohibición de depósitos (Art. 18):** Ilegal exigir depósitos en efectivo o pagarés en garantía.
        """
    # 14. Consumidor y Garantías
    elif "consumidor" in lower or "garantía" in lower or "garantia" in lower or "compra" in lower or "dañado" in lower or "retracto" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Tus derechos como consumidor están amparados por la **Ley 1480 de 2011**:
* **Garantía Legal (Arts. 7 y 11):** Si el bien repite la falla o no admite arreglo, puedes exigir el cambio o la devolución total de tu dinero.
* **Retracto (Art. 47):** 5 días hábiles en compras virtuales para devolver el producto y recibir el 100% del dinero.
        """
    # 15. Requisas y Tránsito
    elif "transito" in lower or "tránsito" in lower or "requisa" in lower or "policia" in lower or "policía" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

### 👮 Procedimientos en vía pública:
* **Agentes Civiles de Tránsito:** NO pueden requisar personas ni bolsos (Sentencia C-128/18).
* **Policía Nacional:** Registro preventivo bajo Art. 159 Ley 1801/16 (mismo género, sin desnudamiento ni revisar chats de celular).
* **Derecho a filmar (Art. 21 Ley 1801/16):** Derecho constitucional inalienable a grabar en video todo procedimiento público policial.
        """
    # 16. IVE
    elif "abortar" in lower or "ive" in lower or "embarazo" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría médica ni jurídica formal.*

En Colombia, la **Interrupción Voluntaria del Embarazo (IVE)** es un derecho fundamental amparado por la **Sentencia C-055 de 2022**:
* Libre y voluntario hasta la semana 24 de gestación; posterior a la semana 24 aplican las 3 causales de la Sentencia C-355 de 2006.
* Gratuito en la red de salud de tu EPS en máximo 5 días (Res. 051/23).
        """
    # 17. Nacionalidad y Retención
    elif "nacionalidad" in lower or "venezuela" in lower or "pasaporte" in lower or "ius solis" in lower or "ius sanguinis" in lower or "caballo" in lower or "retención" in lower or "retencion" in lower:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

* **Nacionalidad (Art. 96 C.P. y Ley 43/93):** Criterio mixto por nacimiento (Ius sanguinis e Ius domicilii). Medida "Primero la Niñez" (Ley 1997/19) para hijos de venezolanos nacidos en Colombia. Se admite la doble nacionalidad.
* **Derecho de Retención (Art. 2417 Código Civil):** Retener una cosa o animal por deudas de cuidado o mantenimiento **no transfiere la propiedad** ni autoriza a venderlo o explotarlo. Los animales son seres sintientes protegidos por la Ley 1774 de 2016.
        """
    else:
        resp_text = f"""
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

He recibido tu consulta sobre: *"{user_input}"*.

Para orientarte de forma veraz y prevenir alucinaciones jurídicas:
1. **Marco normativo general:** En Colombia tus derechos están amparados por la **Constitución Política de 1991** (Art. 23 Petición, Art. 29 Debido Proceso, Art. 86 Tutela, Art. 96 Nacionalidad) y los códigos y leyes sustantivas de la República.
2. **Ruta sugerida:** Puedes presentar un **Derecho de Petición**, interponer una denuncia penal ante la Fiscalía (en [adenunciar.policia.gov.co](https://adenunciar.policia.gov.co)) o solicitar conciliación gratuita.
3. **Canales gratuitos:** Consulta el portal **[LegalApp del Ministerio de Justicia](https://www.legalapp.gov.co)** o acude al **Consultorio Jurídico de la Pontificia Universidad Javeriana** para atención presencial personalizada.
        """

    with st.chat_message("assistant"):
        st.markdown(resp_text)
    st.session_state.messages.append({"role": "assistant", "content": resp_text})
