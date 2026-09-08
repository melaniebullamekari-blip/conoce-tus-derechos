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
    - 🏛️ **Constitución Política de 1991** (Arts. 15, 23, 74, 86)
    - 📋 **Ley 1755 de 2015** (Derecho de Petición)
    - 🛒 **Ley 1480 de 2011** (Estatuto del Consumidor)
    - 🏠 **Ley 820 de 2003** (Arrendamiento de Vivienda)
    - 👮 **Ley 1801 de 2016** (Código de Convivencia)
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

sample_query = None
with col1:
    if st.button("📋 ¿Qué hacer si no responden mi petición?"):
        sample_query = "¿Qué hago si una entidad pública no responde una petición que hice?"
with col2:
    if st.button("🛒 Compré algo por internet y llegó dañado"):
        sample_query = "Compré un producto por internet, me llegó dañado y no me quieren devolver el dinero. ¿Qué derechos tengo?"
with col3:
    if st.button("🏠 Me subieron el arriendo demasiado"):
        sample_query = "¿Cuánto es lo máximo que me pueden subir el arriendo este año en Colombia?"

# ----------------- Gestión del Chat -----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "¡Hola! Soy tu asistente de **Conoce tus Derechos**. Describe en tus propias palabras la situación o el problema que estás experimentando (por ejemplo, en tu trabajo, vivienda, compras, trámites públicos o convivencia) y te explicaré qué normas te protegen y qué pasos puedes seguir."
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

    # Base de conocimiento estructurada para respuesta instantánea verificada
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
1. **Acción de Tutela:** Procede de inmediato por tratarse de un derecho fundamental. Se presenta ante cualquier juez de la República, es gratuita y no requiere abogado. El juez debe resolver en un plazo máximo de 10 días hábiles.
2. **Silencio Administrativo Positivo (para documentos):** Si pediste copias y pasaron 10 días, la ley asume que fue aprobada y deben entregártelas en 3 días (Art. 14 Ley 1755 de 2015).
3. **Queja Disciplinaria:** Puedes presentar queja ante la **Personería Municipal** o la **Procuraduría General de la Nación** por falta disciplinaria del funcionario.
        """
    elif "arriendo" in lower_input or "arrendamiento" in lower_input or "canon" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

En Colombia, los arrendamientos de vivienda urbana están regulados por la **Ley 820 de 2003**:

### 🏠 Reglas clave del canon de arrendamiento:
1. **Tope máximo de incremento ([Art. 20](corpus/ley_820_2003_arrendamiento.md)):** El arrendador solo puede subir el valor cada **12 meses** continuos de contrato, y el aumento no puede superar el **100% de la inflación (IPC)** del año anterior.
2. **Tope del valor total:** El canon mensual jamás podrá superar el 1% del valor comercial del inmueble.
3. **Aviso previo:** El arrendador está obligado a notificarte el incremento por escrito antes de cobrarlo.
4. **Prohibición de depósitos ([Art. 18](corpus/ley_820_2003_arrendamiento.md)):** Está expresamente prohibido exigir depósitos en efectivo o pagarés en garantía para vivienda urbana.
        """
    elif "consumidor" in lower_input or "garantía" in lower_input or "garantia" in lower_input or "compra" in lower_input or "dañado" in lower_input or "retracto" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

Tus derechos como comprador están amparados por el **Estatuto del Consumidor ([Ley 1480 de 2011](corpus/ley_1480_2011_consumidor.md))**:

### 🛒 Tus derechos principales:
1. **Garantía Legal ([Art. 7 y 11](corpus/ley_1480_2011_consumidor.md)):** Todo producto nuevo tiene garantía mínima. Si el producto falla y no puede ser reparado, o si repite la falla, **tienes derecho a elegir** entre el cambio por uno nuevo o la devolución total de tu dinero.
2. **Derecho de Retracto ([Art. 47](corpus/ley_1480_2011_consumidor.md)):** Si compraste por internet o teléfono, tienes **5 días hábiles** desde la entrega para arrepentirte y devolverlo; el vendedor debe reembolsarte el 100% en máximo 30 días.
3. **Reversión del Pago ([Art. 51](corpus/ley_1480_2011_consumidor.md)):** Si pagaste con tarjeta y fuiste víctima de fraude, producto no entregado o defectuoso, puedes pedir la reversión a tu banco en 5 días hábiles.
4. **Demanda ante la SIC:** Puedes demandar gratis y virtualmente en [sic.gov.co](https://www.sic.gov.co) sin necesidad de abogado.
        """
    elif "transito" in lower_input or "tránsito" in lower_input or "requisa" in lower_input or "policia" in lower_input or "policía" in lower_input:
        resp_text = """
> ⚠️ **Advertencia legal:** *Esta herramienta es un ejercicio académico pedagógico. No constituye asesoría jurídica formal.*

### 👮 Procedimientos en vía pública y registro a personas:
1. **Agentes Civiles / Guardas de Tránsito:** **NO pueden requisar** a las personas ni revisar bolsos o pertenencias personales (Ley 769 de 2002 y Sentencia C-128 de 2018). Solo verifican documentos del vehículo y equipo de prevención vial.
2. **Policía Nacional Uniformada:** Sí está facultada para realizar registros preventivos bajo el **Art. 159 de la Ley 1801 de 2016** para buscar armas o sustancias, siempre con respeto a la dignidad y por personal del mismo género.
3. **Derecho a Grabar ([Art. 21 Ley 1801 de 2016](corpus/ley_1801_2016_codigo_policia.md) y Sentencia T-032/21):** Todo ciudadano tiene derecho constitucional a filmar en audio y video los procedimientos públicos de las autoridades.
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
