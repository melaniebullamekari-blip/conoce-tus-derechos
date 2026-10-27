import os
import streamlit as st

st.set_page_config(
    page_title="Conoce tus Derechos — Asistente Jurídico",
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
    .source-card {
        background-color: #F3F4F6;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #E5E7EB;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Advertencia Ética Visible Obligatoria -----------------
st.markdown('<h1 class="main-title">⚖️ Conoce tus Derechos</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Tu orientador jurídico ciudadano: claridad y respaldo legal al alcance de todos (Colombia 🇨🇴)</p>', unsafe_allow_html=True)

st.markdown("""
<div class="legal-alert">
    ⚠️ <strong>Advertencia legal visible:</strong> Esta herramienta es un ejercicio académico con fines exclusivamente pedagógicos e informativos. 
    <strong>No constituye asesoría jurídica formal ni sustituye la consulta con un profesional del derecho.</strong>
</div>
""", unsafe_allow_html=True)

# ----------------- Barra Lateral (Configuración y Fuentes) -----------------
with st.sidebar:
    st.header("📚 Marco Jurídico & Fuentes")
    st.markdown("""
    Este asistente consulta normas oficiales colombianas:
    - 🏛️ **Constitución de 1991** (Arts. 15, 23, 74, 86, 96)
    - 📋 **Ley 1755 de 2015** (Derecho de Petición)
    - 🛒 **Ley 1480 de 2011** (Estatuto del Consumidor)
    - 🏠 **Ley 820 de 2003** (Arrendamiento Urbano)
    - 👮 **Ley 1801 de 2016** (Código de Convivencia)
    - 💼 **Código Sustantivo del Trabajo** (CST - Laboral)
    - 💡 **Ley 142 de 1994** (Servicios Públicos)
    - 💳 **Ley 1266/08 y Ley 2157/21** (Datacrédito / Habeas Data)
    - 🏥 **Ley 1751 de 2015** (Derecho a la Salud)
    - 🇨🇴 **Ley 43 de 1993** (Nacionalidad Colombiana)
    - 📞 **Ley 2300 de 2023** (Ley "Dejen de Fregar")
    - ⚖️ **Sentencia C-055 de 2022** (IVE - Salud Sexual)
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
    if st.button("📋 Petición no respondida"):
        sample_query = "¿Qué hago si una entidad pública no responde una petición que hice?"
with col2:
    if st.button("🛒 Producto por internet dañado"):
        sample_query = "Compré un producto por internet, me llegó dañado y no me quieren devolver el dinero. ¿Qué derechos tengo?"
with col3:
    if st.button("🏠 Aumento excesivo de arriendo"):
        sample_query = "¿Cuánto es lo máximo que me pueden subir el arriendo este año en Colombia?"

with col4:
    if st.button("💼 Despido o liquidación laboral"):
        sample_query = "Me despidieron de mi trabajo sin justa causa, ¿qué indemnización y liquidación me corresponde?"
with col5:
    if st.button("💳 Reporte negativo en Datacrédito"):
        sample_query = "¿Cuánto tiempo puede durar un reporte negativo en Datacrédito y qué requisitos tiene?"
with col6:
    if st.button("💡 Cobro excesivo en factura de luz/agua"):
        sample_query = "Me llegó la factura de servicios públicos con cobro desmedido, ¿me pueden cortar el servicio si reclamo?"

# ----------------- Gestión del Chat -----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "¡Hola! Soy tu asistente de **Conoce tus Derechos**. Describe en tus propias palabras la situación o el problema que estás experimentando (por ejemplo, en tu trabajo, servicios públicos, datacrédito, salud, vivienda, compras, trámites públicos, nacionalidad o convivencia) y te explicaré qué normas te protegen y qué pasos seguir."
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Escribe tu pregunta o situación aquí...")
if sample_query:
    user_input = sample_query

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    resp_text = ""
    lower_input = user_input.lower()

    if "petición" in lower_input or "peticion" in lower_input or "no responde" in lower_input or "entidad pública" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Si una entidad pública no respondió tu solicitud dentro de los términos legales, se vulnera tu **Derecho Fundamental de Petición** (Art. 23 Constitución Política y Ley 1755 de 2015).

### 📅 1. Términos legales de respuesta (Días Hábiles):
* **10 días hábiles:** Para solicitud de información y entrega de documentos/copias.
* **15 días hábiles:** Para peticiones de interés general o particular.
* **30 días hábiles:** Para consultas técnicas o jurídicas.

### ⚡ 2. ¿Qué puedes hacer?:
1. **Acción de Tutela:** Procede de inmediato por tratarse de un derecho fundamental. Se presenta ante cualquier juez, es gratuita y no requiere abogado. El juez debe resolver en máximo 10 días hábiles.
2. **Silencio Administrativo Positivo (para documentos):** Si pediste copias y pasaron 10 días, la ley asume que fue aprobada y deben entregártelas en 3 días (Art. 14 Ley 1755 de 2015).
3. **Queja Disciplinaria:** Puedes presentar queja ante la **Personería Municipal** o la **Procuraduría General de la Nación**.
        """
    elif "arriendo" in lower_input or "arrendamiento" in lower_input or "canon" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

En Colombia, los arrendamientos de vivienda urbana están regulados por la **Ley 820 de 2003**:

### 🏠 Reglas clave del canon de arrendamiento:
1. **Tope máximo de incremento (Art. 20):** El arrendador solo puede subir el valor cada **12 meses** continuos de contrato, y el aumento no puede superar el **100% de la inflación (IPC)** del año anterior.
2. **Tope del valor total:** El canon mensual jamás podrá superar el 1% del valor comercial del inmueble.
3. **Aviso previo:** El arrendador está obligado a notificarte el incremento por escrito antes de cobrarlo.
4. **Prohibición de depósitos (Art. 18):** Está expresamente prohibido exigir depósitos en efectivo o pagarés en garantía para vivienda urbana.
        """
    elif "consumidor" in lower_input or "garantía" in lower_input or "garantia" in lower_input or "compra" in lower_input or "dañado" in lower_input or "retracto" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Tus derechos como comprador están amparados por el **Estatuto del Consumidor (Ley 1480 de 2011)**:

### 🛒 Tus derechos principales:
1. **Garantía Legal (Arts. 7 y 11):** Todo producto nuevo tiene garantía mínima. Si el producto falla y no puede ser reparado, o si repite la falla, **tienes derecho a elegir** entre el cambio por uno nuevo o la devolución total de tu dinero.
2. **Derecho de Retracto (Art. 47):** Si compraste por internet o teléfono, tienes **5 días hábiles** desde la entrega para arrepentirte y devolverlo; el vendedor debe reembolsarte el 100% en máximo 30 días.
3. **Reversión del Pago (Art. 51):** Si pagaste con tarjeta y fuiste víctima de fraude, producto no entregado o defectuoso, puedes pedir la reversión a tu banco en 5 días hábiles.
4. **Demanda ante la SIC:** Puedes demandar gratis y virtualmente en [sic.gov.co](https://www.sic.gov.co) sin necesidad de abogado.
        """
    elif "trabajo" in lower_input or "laboral" in lower_input or "despido" in lower_input or "liquidación" in lower_input or "liquidacion" in lower_input or "prima" in lower_input or "cesantías" in lower_input or "horas extras" in lower_input or "acoso laboral" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Tus derechos laborales están regulados por el **Código Sustantivo del Trabajo (CST)** y la **Ley 2101 de 2021**:

### 💼 Aspectos clave que debes conocer:
1. **Despido sin justa causa (Art. 64 CST):** Da derecho inmediato a indemnización económica. A término indefinido: 30 días de salario por el primer año y 20 días adicionales por cada año siguiente (para sueldos menores a 10 SMLMV).
2. **Liquidación y sanción moratoria (Art. 65 CST):** El empleador debe pagar la liquidación completa al momento del despido o renuncia. Si se demora injustificadamente, debe pagar **un día de salario por cada día de retraso** (hasta por 24 meses).
3. **Prestaciones obligatorias:** Prima de servicios (junio y diciembre), Cesantías consignadas antes del 15 de febrero, Intereses de cesantías pagados en enero (12%), y 15 días hábiles de vacaciones por año.
4. **Jornada laboral y recargos:** La jornada máxima legal se reduce gradualmente por Ley 2101/21 (46/44/42 horas). El recargo nocturno ordinario es del 35% y los dominicales/festivos se remuneran con recargo del 75%.
5. **Acoso laboral (Ley 1010 de 2006):** Si radicas queja ante el Comité de Convivencia o MinTrabajo, gozas de fuero de protección frente al despido por 6 meses.
        """
    elif "servicio público" in lower_input or "servicios publicos" in lower_input or "factura" in lower_input or "recibo" in lower_input or "luz" in lower_input or "agua" in lower_input or "gas" in lower_input or "corte" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Los servicios públicos domiciliarios se rigen por la **Ley 142 de 1994**:

### 💡 Tus derechos frente a la empresa prestadora:
1. **Cobros desmedidos o anomalías (Art. 149):** Frente a desviaciones significativas de consumo, la empresa debe investigar técnicamente antes de cobrar el valor extraordinario. Solo estás obligado a pagar el promedio histórico habitual mientras se define el reclamo.
2. **Prohibición de corte (Art. 155):** La empresa **NO puede suspenderte el servicio** por las sumas que estén en reclamación formal, siempre que canceles la porción no disputada.
3. **Plazo para reclamar y recursos (Art. 154):** Tienes hasta 5 meses para objetar la factura. Si la empresa te niega la queja, debes interponer **Recurso de Reposición y en subsidio de Apelación** ante la **Superservicios** dentro de los 5 días hábiles siguientes.
4. **Silencio Administrativo Positivo (Art. 158):** Si la empresa tarda más de **15 días hábiles** en responder y notificar tu reclamo, la ley entiende que ganaste el caso por derecho y el cobro debe anularse.
        """
    elif "datacrédito" in lower_input or "datacredito" in lower_input or "cifin" in lower_input or "centrales de riesgo" in lower_input or "reporte negativo" in lower_input or "deuda" in lower_input or "suplantación" in lower_input or "suplantacion" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Tu información crediticia está protegida por la **Ley 1266 de 2008** y la **Ley 2157 de 2021 ("Borrón y Cuenta Nueva")**:

### 💳 Reglas del Habeas Data Financiero:
1. **Aviso previo obligatorio (Art. 12):** La entidad acreedora debe enviarte una notificación previa por escrito al menos **20 días calendario antes** de reportarte a Datacrédito o CIFIN. Si no lo hizo, el reporte es nulo y puedes exigir su retiro inmediato.
2. **Caducidad del reporte negativo (Art. 13):**
   * Si la mora fue menor a 2 años: El reporte negativo dura el **doble del tiempo de la mora** una vez pagada la deuda.
   * Si la mora fue de 2 o más años: Una vez cancelada la obligación, el reporte dura **máximo 4 años**.
   * Prescripción por paso del tiempo: Si nunca pagaste y pasaron **8 años** en mora, el reporte debe eliminarse automáticamente.
3. **Suplantación de identidad:** Si sacaron créditos a tu nombre fraudulentamente, radica copia de la denuncia penal ante la entidad. En 10 días deben colocar la leyenda *"Víctima de falsedad personal"* y suspender el reporte.
4. **Consulta gratis:** Consultar tu historial en Datacrédito es 100% gratuito y no baja tu puntaje score.
        """
    elif "salud" in lower_input or "eps" in lower_input or "medicamento" in lower_input or "urgencias" in lower_input or "medico" in lower_input or "médico" in lower_input or "cirugía" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría médica ni jurídica formal.*

En Colombia, la salud es un **derecho fundamental autónomo e irrenunciable** amparado por la **Ley Estatutaria 1751 de 2015**:

### 🏥 Principios y garantías irrenunciables:
1. **Prohibición absoluta de negación de urgencias (Arts. 10 y 14):** Ningún hospital o clínica pública o privada puede exigir copagos, cheques, pagarés o autorizaciones de la EPS para atender una urgencia vital. El "paseo de la muerte" es un delito.
2. **Entrega de medicamentos en 48 horas (Res. 1604/13):** Si el dispensario de tu EPS no tiene el medicamento formulado, dispone de máximo **48 horas** para entregarlo (incluso a domicilio si estás imposibilitado).
3. **Principio de Integralidad (Art. 8):** La EPS no puede imponer barreras administrativas ni fragmentar tratamientos. Debe cubrir diagnóstico, procedimientos y medicinas completas.
4. **Vías inmediatas:** Radica queja urgente ante la **Superintendencia Nacional de Salud (Supersalud)** al 018000 513700. Si está en peligro la vida o la salud, presenta **Acción de Tutela con solicitud de medida cautelar provisional** ante cualquier juez.
        """
    elif "nacionalidad" in lower_input or "venezuela" in lower_input or "pasaporte" in lower_input or "ius solis" in lower_input or "ius sanguinis" in lower_input or "doble nacionalidad" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

La nacionalidad colombiana se rige por el **Artículo 96 de la Constitución Política** y la **Ley 43 de 1993**:

### 🇨🇴 Criterios de Nacionalidad en Colombia:
1. **Criterio Mixto por Nacimiento:**
   * **Ius Sanguinis:** Si naciste en Colombia y al menos uno de tus padres es colombiano, eres colombiano por nacimiento.
   * **Ius Solis con domicilio:** Si naciste en Colombia de padres extranjeros, eres colombiano si al menos uno de ellos estaba domiciliado legalmente en el país al momento de nacer.
   * **Hijos de venezolanos nacidos en Colombia (Ley 1997/19 - Primero la Niñez):** Se otorga nacionalidad colombiana preventiva contra la apatridia a los nacidos en territorio nacional desde 2015.
2. **Doble Nacionalidad (Ley 43/93 Art. 22):** Colombia reconoce la doble y múltiple nacionalidad (puedes tener pasaporte venezolano, libanés y colombiano simultáneamente).
3. **Obligación legal:** Al ingresar, permanecer o salir de Colombia, debes identificarte y actuar obligatoriamente como ciudadano colombiano portando tus documentos nacionales.
        """
    elif "caballo" in lower_input or "retención" in lower_input or "retencion" in lower_input or "club" in lower_input or "deuda animal" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Respecto a deudas de mantenimiento o hospedaje y tenencia de animales en Colombia:

### 🐴 Marco Civil y de Bienestar Animal:
1. **Derecho de Retención (Art. 2417 Código Civil):** Si adeudas el hospedaje o manutención, el club o pesebrera puede retener provisionalmente el animal hasta el pago de los gastos necesarios.
2. **NO transfiere la propiedad:** El derecho de retención jamás convierte al club o entrenador en dueño del animal. **No pueden venderlo, cederlo ni dejar que terceros lo monten o exploten comercialmente** sin una orden judicial previa en un proceso ejecutivo.
3. **Animales como seres sintientes (Ley 1774 de 2016):** El tenedor temporal está obligado a brindar alimentación adecuada y atención veterinaria. Dejarlo montar arbitrariamente o descuidarlo puede configurar abuso de confianza o maltrato sancionable.
        """
    elif "llamadas" in lower_input or "cobranza" in lower_input or "spam" in lower_input or "dejen de fregar" in lower_input or "banco llama" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Las llamadas y mensajes comerciales o de cobro están estrictamente regulados por la **Ley 2300 de 2023 ("Ley Dejen de Fregar")**:

### 📞 Reglas obligatorias para entidades y bancos:
1. **Horarios permitidos (Art. 3):**
   * Lunes a viernes: de 7:00 a.m. a 7:00 p.m.
   * Sábados: de 8:00 a.m. a 3:00 p.m.
   * **Domingos y festivos: TERMINANTEMENTE PROHIBIDO contactar al usuario.**
2. **Periodicidad:** Máximo 2 contactos por semana por entidad, sin importar el canal (llamada, SMS o WhatsApp).
3. **Prohibición a referencias:** Las entidades NO pueden llamar a tus familiares o amigos para cobrarles o avergonzarte sobre tu deuda.
4. **Sanciones:** Puedes presentar queja formal ante la **Superintendencia de Industria y Comercio (SIC)** o la **Superfinanciera**.
        """
    elif "transito" in lower_input or "tránsito" in lower_input or "requisa" in lower_input or "policia" in lower_input or "policía" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

### 👮 Procedimientos en vía pública y registro a personas:
1. **Agentes Civiles / Guardas de Tránsito:** **NO pueden requisar** a las personas ni revisar bolsos o pertenencias personales (Ley 769 de 2002 y Sentencia C-128 de 2018). Solo verifican documentos del vehículo y equipo de prevención vial.
2. **Policía Nacional Uniformada:** Sí está facultada para realizar registros preventivos bajo el **Art. 159 de la Ley 1801 de 2016** para buscar armas o sustancias, siempre con respeto a la dignidad y por personal del mismo género.
3. **Derecho a Grabar (Art. 21 Ley 1801 de 2016 y Sentencia T-032/21):** Todo ciudadano tiene derecho constitucional a filmar en audio y video los procedimientos públicos de las autoridades.
        """
    elif "abortar" in lower_input or "ive" in lower_input or "embarazo" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría médica ni jurídica formal.*

En Colombia, la **Interrupción Voluntaria del Embarazo (IVE)** es un derecho fundamental amparado por la **Sentencia C-055 de 2022 de la Corte Constitucional**:
1. **Hasta la semana 24 de gestación:** Es libre, voluntaria y no requiere cumplir causales.
2. **Después de la semana 24:** Aplican las 3 causales de la Sentencia C-355 de 2006 (salud/vida de la madre, malformación fetal o agresión sexual).
3. **Atención gratuita en EPS:** Regulado por la Resolución 051 de 2023 del MinSalud con plazo máximo de 5 días calendario.
4. **Líneas de apoyo confidencial:** Profamilia (300 912 4560), Oriéntame ((601) 744 7633) y Línea Púrpura (01 8000 112 137).
        """
    else:
        resp_text = f"""
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

He recibido tu consulta sobre: *"{user_input}"*.

Para brindarte una respuesta precisa y evitar alucinaciones jurídicas:
1. **Marco normativo general:** En Colombia tus derechos constitucionales están protegidos por la **Constitución Política de 1991** (Art. 86 Tutela, Art. 23 Petición, Art. 29 Debido Proceso).
2. **Mecanismo sugerido:** Si una entidad o particular está afectando tus derechos, puedes radicar un **Derecho de Petición** solicitando explicaciones o solución, o acudir a los canales de conciliación y justicia gratuita.
3. **Apoyo gratuito:** Te recomendamos consultar el portal **[LegalApp del Ministerio de Justicia](https://www.legalapp.gov.co)** o acudir al **Consultorio Jurídico de la Pontificia Universidad Javeriana** para revisión personalizada de tu caso.
        """

    with st.chat_message("assistant"):
        st.markdown(resp_text)
    st.session_state.messages.append({"role": "assistant", "content": resp_text})
