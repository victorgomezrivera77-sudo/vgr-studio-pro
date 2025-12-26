import streamlit as st
from PIL import Image
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="VGR Art Studio", layout="centered")

# --- DISEÑO DE LUJO (Negro, Hueso y Naranja) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #F5F5DC !important; }
    h1 { color: #FF4B00 !important; text-align: center; }
    .stButton>button { background-color: #FF4B00; color: white; width: 100%; border-radius: 8px; }
    .billetera-reserva { border: 1px solid #333; padding: 15px; border-radius: 10px; background-color: #0a0a0a; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ OASIS ART STUDIO")
st.markdown("<p style='text-align: center;'>Curaduría Artística | Victor Gomez Rivera</p>", unsafe_allow_html=True)

# --- PESTAÑAS ---
tab1, tab2, tab3 = st.tabs(["📸 Cotizar Imagen", "✍️ Cotizar Idea", "📅 Calendario"])

with tab1:
    st.write("Sube tu referencia para un análisis técnico de complejidad.")
    foto = st.file_uploader("", type=["jpg", "png", "jpeg"])
    if foto:
        st.image(Image.open(foto), use_container_width=True)
        with st.spinner("Analizando composición técnica..."):
            time.sleep(2)
        st.success("✅ ANÁLISIS COMPLETADO")

with tab2:
    st.write("Describe tu visión para recibir una propuesta.")
    st.text_area("¿Qué diseño tienes en mente?")
    st.button("Enviar Propuesta")

with tab3:
    st.write("Consulta disponibilidad en el jardín.")
    st.button("Ver Calendario")

# --- BILLETERA ---
st.markdown("---")
st.markdown("""
    <div class="billetera-reserva">
        <h3 style='margin:0;'>💳 Reserva de Cita</h3>
        <p>Monto del depósito: <strong>$60.00</strong></p>
        <p style="font-size: 0.8em; color: #888 !important;">* Este monto se incluye en el precio total de la obra.</p>
    </div>
    """, unsafe_allow_html=True)
