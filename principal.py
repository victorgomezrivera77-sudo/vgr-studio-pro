import streamlit as st
from PIL import Image
import time

# --- 1. CONFIGURACIÓN VISUAL OASIS ---
st.set_page_config(page_title="Oasis AI - Victor Gomez", layout="centered")

# Estilos de color Naranja y Negro (Tu identidad visual)
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
        height: 3em;
    }
    /* Estilo para los inputs */
    input, textarea {
        background-color: #1A1A1A !important;
        color: white !important;
        border: 1px solid #FF4B2B !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ PROYECTO OASIS")
st.write("Bienvenido a la curaduría de Victor Gomez. Elige tu proceso:")

# --- 2. LÓGICA DEL ANALISTA (CEREBRO) ---
def calcular_presupuesto(descripcion, zona, tamaño):
    zonas_dificiles = ['costillas', 'cuello', 'estomago', 'manos', 'pies', 'cara']
    base_por_pulgada = 50 # Un punto de partida base
    
    complejidad = 1.0
    # Análisis de palabras clave
    desc_low = descripcion.lower()
    if any(word in desc_low for word in ["detalle", "micro", "realismo", "neotraditional"]):
        complejidad += 0.6
    if "color" in desc_low:
        complejidad += 0.4
        
    # Multiplicador por zona de dificultad
    if zona.lower() in zonas_dificiles:
        complejidad += 0.5
        
    total = (base_por_pulgada * tamaño) * complejidad
    return round(total, 2)

# --- 3. INTERFAZ DE USUARIO ---
tab1, tab2 = st.tabs(["🔍 ESCÁNER E IA", "📅 AGENDA OASIS"])

with tab1:
    st.subheader("🕵️ Analista de Complejidad")
    
    foto = st.file_uploader("Sube tu referencia visual", type=["jpg", "png", "jpeg"])
    if foto:
        st.image(foto, width=300)

    user_idea = st.text_area("¿Qué tienes en mente? (Estilo, detalles, elementos)")
    col1, col2 = st.columns(2)
    with col1:
        user_zone = st.text_input("¿Zona del cuerpo?")
    with col2:
        user_size = st.number_input("Tamaño aprox. (pulgadas)", min_value=1, value=3)

    if st.button("Analizar Idea con IA"):
        if user_idea and user_zone:
            precio_final = calcular_presupuesto(user_idea, user_zone, user_size)
            
            with st.status("Analizando densidad de pigmento y zona...", expanded=True) as status:
                time.sleep(1.2)
                st.write("🔬 Escaneando referencia visual...")
                time.sleep(1)
                st.write("⚖️ Calculando horas de sesión y técnica...")
                status.update(label="Análisis de Oasis Completado", state="complete")
            
            st.metric(label="Inversión Estimada", value=f"${precio_final} USD")
            st.info(f"**Veredicto:** Este diseño en '{user_zone}' requiere precisión de alto nivel. Ve a la pestaña de Agenda para reservar.")
        else:
            st.warning("Por favor, describe tu visión y la zona para que la IA pueda trabajar.")

with tab2:
    st.subheader("📅 Reserva tu Espacio")
    st.write("Para asegurar tu cita en Oasis, se requiere un depósito de reserva.")
    st.date_input("Selecciona tu fecha tentativa", value=None)
    
    st.markdown("""
    <div style="background-color: #1A1A1A; padding: 20px; border-radius: 10px; border-left: 5px solid #FF4B2B;">
        <h3 style="margin:0;">💳 DEPÓSITO DE RESERVA</h3>
        <p style="font-size: 24px; font-weight: bold; color: #FF4B2B !important;">Monto: $60.00</p>
        <p style="font-size: 12px;">Este monto asegura tu lugar y se deduce del total de la obra.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.write("👉 **IMPORTANTE:** Una vez analizada tu idea, envía la captura del presupuesto al DM de @vikin_ink_tatoo.")
