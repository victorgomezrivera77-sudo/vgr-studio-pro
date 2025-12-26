import streamlit as st
from PIL import Image
import time

# --- 1. CONFIGURACIÓN VISUAL OASIS (ESTÉTICA IMPECABLE) ---
st.set_page_config(page_title="Oasis AI - Victor Gomez", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #FFFFFF !important; }
    .stButton>button { 
        background-color: #FF4B2B; 
        color: white; 
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
        border: none;
        height: 3.5em;
    }
    input, textarea {
        background-color: #1A1A1A !important;
        color: white !important;
        border: 1px solid #FF4B2B !important;
    }
    .stMetric {
        background-color: #1A1A1A;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #FF4B2B;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ PROYECTO OASIS")
st.write("Bienvenido a la curaduría de Victor Gomez. Inteligencia aplicada al arte.")

# --- 2. EL ALGORITMO COMANDANTE (LÓGICA DE MERCADO REAL) ---
def algoritmo_oasis_elite(descripcion, zona, tamaño):
    desc_low = descripcion.lower()
    
    # Tarifas base escalonadas (Datos de Mercado 2025)
    if tamaño <= 3:
        tarifa_base = 85  # Mínimo de autor
    elif tamaño <= 10:
        tarifa_base = 110 # Rango medio alta precisión
    else:
        tarifa_base = 150 # Proyectos monumentales (Arquitecto)

    # Multiplicadores de Complejidad Técnica
    multiplicador_tecnico = 1.0
    if any(word in desc_low for word in ["negro solido", "blackwork", "saturado", "relleno"]):
        multiplicador_tecnico += 0.8 # El saturado es el asedio más costoso
    if any(word in desc_low for word in ["detalle", "micro", "fino", "chicano", "filigrana"]):
        multiplicador_tecnico += 0.5

    # Multiplicador por Zona de Guerra
    zonas_guerra = {
        'espalda': 1.6, 'pecho': 1.5, 'costillas': 1.8, 
        'cuello': 1.7, 'manos': 1.6, 'estomago': 1.9, 'cara': 2.0
    }
    multiplicador_zona = zonas_guerra.get(zona.lower(), 1.0)

    # Cálculo Final: (Tamaño * Tarifa) * (Suma de multiplicadores)
    inversion_total = (tamaño * tarifa_base) * (multiplicador_tecnico + (multiplicador_zona - 1))
    
    # Logística de Sesiones (Basado en bloques de $1,200 USD)
    num_sesiones = 1
    if inversion_total > 1500:
        num_sesiones = int(inversion_total // 1200) + 1

    return round(inversion_total, 2), num_sesiones

# --- 3. INTERFAZ DE USUARIO ---
tab1, tab2 = st.tabs(["🔍 ANALISTA ELITE", "📅 AGENDA CASTILLO"])

with tab1:
    st.subheader("🕵️ Analista de Complejidad Técnica")
    
    foto = st.file_uploader("Sube tu referencia visual", type=["jpg", "png", "jpeg"])
    user_idea = st.text_area("Describe tu visión (Estilo, saturación, detalles):")
    
    col1, col2 = st.columns(2)
    with col1:
        user_zone = st.text_input("¿Zona del cuerpo?")
    with col2:
        user_size = st.number_input("Tamaño (pulgadas)", min_value=1, value=3)

    if st.button("ANALIZAR CON OASIS ELITE"):
        if user_idea and user_zone:
            precio, sesiones = algoritmo_oasis_elite(user_idea, user_zone, user_size)
            
            with st.status("Comandante Oasis procesando asedio...", expanded=True) as status:
                time.sleep(1)
                st.write("🔬 Evaluando densidad de pigmento...")
                time.sleep(1)
                st.write(f"⚔️ Calculando logística para {sesiones} sesiones...")
                status.update(label="Análisis de Mercado Completado", state="complete")
            
            st.metric(label="Inversión Total Estimada", value=f"${precio} USD")
            st.write(f"**Veredicto:** Este proyecto en '{user_zone}' requiere **{sesiones} sesiones** de alta intensidad. Inversión protegida por Oasis.")
        else:
            st.warning("El Comandante necesita datos: describe la idea y la zona.")

with tab2:
    st.subheader("📅 Reserva de Plaza")
    st.write("Asegura tu lugar en la historia. Se requiere depósito de reserva.")
    st.date_input("Fecha tentativa", value=None)
    
    st.markdown("""
    <div style="background-color: #1A1A1A; padding: 20px; border-radius: 10px; border-left: 5px solid #FF4B2B;">
        <h3 style="margin:0;">💳 DEPÓSITO DE RESERVA</h3>
        <p style="font-size: 28px; font-weight: bold; color: #FF4B2B !important;">Monto: $60.00</p>
        <p style="font-size: 14px;">Deducible del precio total de la obra.</p>
    </div>
    """, unsafe_allow_html=True)
