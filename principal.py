import streamlit as st
import time

# --- 1. ESTILO VISUAL OASIS (Mantenemos tu estética impecable) ---
st.set_page_config(page_title="Oasis Art Studio - Presupuestos", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #FFFFFF !important; }
    .stButton>button { 
        background-color: #FF4B2B; color: white; font-weight: bold;
        border-radius: 10px; width: 100%; border: none; height: 3.5em;
    }
    .stMetric { background-color: #1A1A1A; border: 1px solid #FF4B2B; border-radius: 10px; padding: 10px; }
    .info-box { background-color: #1A1A1A; padding: 20px; border-radius: 10px; border: 1px solid #FF4B2B; margin-top: 15px; }
    .nota-final { font-size: 13px; color: #888888; font-style: italic; margin-top: 20px; border-top: 1px solid #333; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BÚNKER DE MEMORIA (Persistencia de datos) ---
if 'memoria' not in st.session_state:
    st.session_state.memoria = {"listo": False, "precio": 0, "sesiones": 0, "horas": 0, "materiales": 0}

# --- 3. EL CALCULADOR INTELIGENTE (Lenguaje cercano, precisión Oasis) ---
def calcular_oasis(descripcion, zona, pulgadas):
    texto = descripcion.lower()
    es_letras = any(word in texto for word in ["letra", "frase", "nombre", "lettering"])
    
    # Precios base según tamaño
    if pulgadas <= 3: tarifa = 85
    elif pulgadas <= 10: tarifa = 110
    else: tarifa = 150
    
    # Ajuste por estilo (Victor es experto y rápido en letras)
    multi = 0.6 if es_letras else 1.0
    if any(word in texto for word in ["negro", "relleno", "oscuro", "solido", "saturado"]): multi += 0.8
    if any(word in texto for word in ["detalle", "fino", "micro", "flores"]): multi += 0.4

    # Dificultad por zona del cuerpo
    zonas_especiales = {'costilla': 1.8, 'espalda': 1.6, 'pecho': 1.5, 'cuello': 1.7, 'muñeca': 1.3}
    m_zona = zonas_especiales.get(zona.lower(), 1.0)

    # Cálculo Final
    total = (pulgadas * tarifa) * (multi + (m_zona - 1))
    
    # Tiempo y Materiales
    factor_tiempo = 0.6 if es_letras else 1.2
    horas = round((pulgadas * factor_tiempo) * m_zona, 1)
    materiales = round(total * 0.15, 2)
    sesiones = int(total // 1200) + 1
    
    return round(total, 2), sesiones, horas, materiales

# --- 4. INTERFAZ COMPLETA ---
st.title("🏛️ COTIZADOR OASIS")

# Guía de Ayuda (Mantenemos la función)
with st.expander("❓ ¿Cómo usar esta herramienta?"):
    st.write("""
    1. **Prueba tus ideas:** Puedes interactuar con el cotizador las veces que quieras hasta tener tu idea final.
    2. **Descripción:** Cuéntame qué quieres (estilos, si quieres mucho negro, etc.).
    3. **Imagen Opcional:** Si tienes una referencia, puedes subirla, pero no es obligatorio.
    4. **Sin prisas:** Tus datos se quedan guardados aunque refresques la página.
    """)

st.subheader("🕵️ Analiza tu próximo tatuaje")

# Foto opcional (Mantenemos la función)
foto = st.file_uploader("Sube una foto de referencia (Opcional)", type=["jpg", "png", "jpeg"])
if foto:
    st.image(foto, caption="Referencia lista para análisis", width=200)

user_idea = st.text_area("¿Qué tienes en mente?", placeholder="Ej: Una pantera negra con flores en el brazo...")
col1, col2 = st.columns(2)
with col1: user_zone = st.text_input("¿En qué zona del cuerpo?")
with col2: user_size = st.number_input("Tamaño aprox. (pulgadas)", min_value=1, value=5)

if st.button("VER MI PRESUPUESTO"):
    if user_idea and user_zone:
        p, s, h, m = calcular_oasis(user_idea, user_zone, user_size)
        st.session_state.memoria = {"listo": True, "precio": p, "sesiones": s, "horas": h, "materiales": m}
        with st.spinner("Analizando detalles técnicos..."): time.sleep(1.2)
    else:
        st.warning("Por favor, escribe tu idea y la zona para poder ayudarte.")

# MOSTRAR RESULTADOS (Mantenemos el desglose detallado)
if st.session_state.memoria["listo"]:
    m = st.session_state.memoria
    st.metric(label="Inversión Estimada", value=f"${m['precio']} USD")
    
    st.markdown(f"""
    <div class="info-box">
        <p style="color: #FF4B2B; font-weight: bold; margin-bottom: 8px;">📋 LOGÍSTICA DE TU SESIÓN:</p>
        <p>🕒 <b>Tiempo estimado:</b> Unas {m['horas']} horas de trabajo.</p>
        <p>💉 <b>Insumos Premium:</b> ${m['materiales']} USD (Material estéril y tintas de alta gama).</p>
        <p>📅 <b>Planificación:</b> Se estima en {m['sesiones']} sesión(es).</p>
        <p style="font-size: 14px; margin-top: 10px; color: #CCCCCC;"><i>¡Siéntete libre de ajustar el tamaño o la idea para ver cómo cambia el presupuesto!</i></p>
    </div>
    <p class="nota-final">⚠️ <b>Nota de Victor:</b> Este presupuesto es una guía para que sepas qué esperar. El precio final lo confirmaremos tú y yo en persona el día de la cita, ajustándolo a tu diseño final y anatomía.</p>
    """, unsafe_allow_html=True)

    if st.button("ME GUSTA, QUIERO RESERVAR"):
        st.balloons()
        st.success("¡Excelente! Pasa a la pestaña de 'Agenda' para asegurar tu espacio.")
