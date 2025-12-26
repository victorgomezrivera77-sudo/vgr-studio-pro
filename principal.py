import streamlit as st
import time

# --- 1. CONFIGURACIÓN VISUAL OASIS ---
st.set_page_config(page_title="Oasis AI - Victor Gomez", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #FFFFFF !important; }
    .stButton>button { 
        background-color: #FF4B2B; color: white; font-weight: bold;
        border-radius: 10px; width: 100%; border: none; height: 3.5em;
    }
    .stMetric { background-color: #1A1A1A; border: 1px solid #FF4B2B; border-radius: 10px; padding: 10px; }
    .disclaimer { font-size: 12px; color: #888888; font-style: italic; border-top: 1px solid #333; padding-top: 10px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PERSISTENCIA DE DATOS ---
if 'memoria' not in st.session_state:
    st.session_state.memoria = {"listo": False, "precio": 0, "sesiones": 0, "texto": "", "horas": 0, "materiales": 0}

# --- 3. ALGORITMO COMANDANTE V3 ---
def algoritmo_oasis_v3(descripcion, zona, tamaño):
    desc_low = descripcion.lower()
    es_lettering = any(word in desc_low for word in ["lettering", "letras", "frase"])
    
    tarifa = 85 if tamaño <= 3 else (110 if tamaño <= 10 else 150)
    multi = 0.6 if es_lettering else 1.0
    if any(word in desc_low for word in ["negro", "saturado", "pantera", "solido"]): multi += 0.8
    if any(word in desc_low for word in ["detalle", "fino", "flores", "micro"]): multi += 0.4

    zonas = {'costilla': 1.8, 'espalda': 1.6, 'pecho': 1.5, 'cuello': 1.7, 'muñeca': 1.3}
    m_zona = zonas.get(zona.lower(), 1.0)

    inversion = (tamaño * tarifa) * (multi + (m_zona - 1))
    horas = round((tamaño * (0.6 if es_lettering else 1.2)) * m_zona, 1)
    materiales = round(inversion * 0.15, 2)
    num_sesiones = int(inversion // 1200) + 1
    
    return round(inversion, 2), num_sesiones, horas, materiales

# --- 4. INTERFAZ ---
st.title("🏛️ PROYECTO OASIS")

# SECCIÓN DE AYUDA / GUÍA
with st.expander("❓ ¿Cómo usar el Analista Oasis? (Guía de Usuario)"):
    st.write("""
    1. **Experimenta:** Siéntete libre de probar diferentes ideas, tamaños y zonas. Esta herramienta es para que explores tu presupuesto sin compromiso.
    2. **Descripción:** Sé específico. Menciona si quieres mucho negro o líneas finas.
    3. **Imagen (Opcional):** Si tienes una referencia, súbela para ayudar al análisis, si no, la IA usará tu descripción.
    4. **Reserva:** Una vez tengas tu idea final, puedes proceder a reservar tu lugar en el Castillo.
    """)

st.subheader("🕵️ Analista de Autor")

# Imagen Opcional
foto = st.file_uploader("Sube tu referencia (Opcional)", type=["jpg", "png", "jpeg"])
if foto:
    st.image(foto, caption="Referencia cargada correctamente", width=200)

user_idea = st.text_area("Describe tu visión:", placeholder="Ej: Una rosa neotradicional con sombras profundas...")
col1, col2 = st.columns(2)
with col1: user_zone = st.text_input("¿Zona del cuerpo?")
with col2: user_size = st.number_input("Pulgadas aprox.", min_value=1, value=5)

if st.button("EJECUTAR ANÁLISIS TÉCNICO"):
    if user_idea and user_zone:
        p, s, h, m = algoritmo_oasis_v3(user_idea, user_zone, user_size)
        st.session_state.memoria = {"listo": True, "precio": p, "sesiones": s, "horas": h, "materiales": m}
        with st.spinner("Calculando logística de autor..."): time.sleep(1.2)
    else:
        st.warning("Comandante, indique al menos la idea y la zona.")

if st.session_state.memoria["listo"]:
    m = st.session_state.memoria
    st.metric(label="Presupuesto Estimado", value=f"${m['precio']} USD")
    
    st.markdown(f"""
    <div style="background-color: #1A1A1A; padding: 20px; border-radius: 10px; border: 1px solid #FF4B2B;">
        <p style="color: #FF4B2B; font-weight: bold;">📊 LOGÍSTICA ESTIMADA:</p>
        <p>⏳ <b>Tiempo en Piel:</b> {m['horas']} horas totales.</p>
        <p>💉 <b>Insumos Premium:</b> ${m['materiales']} USD.</p>
        <p>⚔️ <b>Sesiones:</b> {m['sesiones']} sesión(es).</p>
    </div>
    <p class="disclaimer">⚠️ NOTA PROFESIONAL: Este presupuesto es una herramienta informativa basada en parámetros técnicos. El precio final será corroborado y confirmado por Victor Gomez en persona durante la consulta o el día de la sesión, considerando la anatomía final y ajustes de diseño.</p>
    """, unsafe_allow_html=True)

    if st.button("CONFIRMAR IDEA Y RESERVAR"):
        st.success("¡Excelente elección! Dirígete a la pestaña de Agenda para asegurar tu plaza.")
