import streamlit as st
from PIL import Image
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
    input, textarea { background-color: #1A1A1A !important; color: white !important; border: 1px solid #FF4B2B !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PERSISTENCIA: INICIALIZAR MEMORIA DEL CASTILLO ---
if 'analisis_listo' not in st.session_state:
    st.session_state.analisis_listo = False
    st.session_state.precio = 0
    st.session_state.sesiones = 0
    st.session_state.detalle_texto = ""

# --- 3. EL ALGORITMO COMANDANTE (VERSION LETTERING RÁPIDO) ---
def algoritmo_oasis_elite(descripcion, zona, tamaño):
    desc_low = descripcion.lower()
    es_lettering = any(word in desc_low for word in ["lettering", "letras", "frase", "nombre"])
    
    # Ajuste de Tarifa Base
    if tamaño <= 3: tarifa_base = 85
    elif tamaño <= 10: tarifa_base = 110
    else: tarifa_base = 150

    # Multiplicadores de Complejidad
    multiplicador_tecnico = 1.0
    if es_lettering:
        multiplicador_tecnico = 0.6  # EL CABALLO RÁPIDO: El lettering reduce costo por velocidad de ejecución
    elif any(word in desc_low for word in ["negro solido", "blackwork", "saturado"]):
        multiplicador_tecnico += 0.8 
    
    if any(word in desc_low for word in ["detalle", "micro", "fino", "filigrana"]):
        multiplicador_tecnico += 0.4

    # Multiplicador Zona
    zonas_guerra = {'espalda': 1.6, 'pecho': 1.5, 'costillas': 1.8, 'cuello': 1.7, 'manos': 1.6, 'estomago': 1.9}
    multi_zona = zonas_guerra.get(zona.lower(), 1.0)

    inversion = (tamaño * tarifa_base) * (multiplicador_tecnico + (multi_zona - 1))
    
    # Construcción del Veredicto Extenso
    texto = f"Análisis técnico para proyecto de {tamaño} pulg. en {zona}. "
    if es_lettering:
        texto += "He detectado que buscas Lettering. Aunque la pieza es de gran escala, Victor domina este estilo con alta velocidad técnica, lo que permite optimizar tu inversión sin sacrificar la fluidez caligráfica. Es una pieza de alto impacto visual y ejecución eficiente."
    else:
        texto += "La densidad de pigmento y la zona elegida requieren un asedio técnico prolongado para asegurar la integridad de la obra a largo plazo."

    num_sesiones = int(inversion // 1200) + 1
    return round(inversion, 2), num_sesiones, texto

# --- 4. INTERFAZ ---
st.title("🏛️ PROYECTO OASIS")

tab1, tab2 = st.tabs(["🔍 ANALISTA ELITE", "📅 AGENDA CASTILLO"])

with tab1:
    st.subheader("🕵️ Analista de Complejidad")
    user_idea = st.text_area("Describe tu visión:", placeholder="Ej: Lettering chicano grande en el pecho...")
    col1, col2 = st.columns(2)
    with col1: user_zone = st.text_input("¿Zona?")
    with col2: user_size = st.number_input("Pulgadas", min_value=1, value=3)

    if st.button("EJECUTAR ANÁLISIS"):
        if user_idea and user_zone:
            p, s, t = algoritmo_oasis_elite(user_idea, user_zone, user_size)
            # Guardar en la memoria del búnker
            st.session_state.precio = p
            st.session_state.sesiones = s
            st.session_state.detalle_texto = t
            st.session_state.analisis_listo = True
            
            with st.spinner("El Comandante está calculando..."):
                time.sleep(1.5)
        else:
            st.warning("Faltan datos para el Comandante.")

    # Mostrar resultados persistentes
    if st.session_state.analisis_listo:
        st.markdown(f"""
        <div style="background-color: #1A1A1A; padding: 20px; border-radius: 10px; border: 1px solid #FF4B2B;">
            <h2 style="color: #FF4B2B !important;">Inversión: ${st.session_state.precio} USD</h2>
            <p style="font-size: 14px; color: #CCCCCC !important;">{st.session_state.detalle_texto}</p>
            <hr>
            <p><b>Sesiones estimadas:</b> {st.session_state.sesiones}</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("📅 Reserva de Plaza")
    st.write("Tu progreso está guardado. Puedes seleccionar tu fecha ahora.")
    st.date_input("Fecha de asalto")
