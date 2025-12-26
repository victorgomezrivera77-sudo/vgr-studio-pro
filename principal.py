import streamlit as st
from PIL import Image
import time
from datetime import date

# --- CONFIGURACIÓN OASIS ---
st.set_page_config(page_title="VGR Art Studio | Oasis", layout="centered")

# --- ESTILO DE LUJO ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #F5F5DC; }
    h1 { color: #FF4B00 !important; text-align: center; font-weight: 800; }
    .card { background-color: #0a0a0a; padding: 25px; border-radius: 15px; border: 1px solid #222; margin-bottom: 20px; }
    .ejemplo-box { background-color: #111; border-left: 4px solid #FF4B00; padding: 10px; margin: 10px 0; font-size: 0.9em; color: #bbb; }
    .stButton>button { background: linear-gradient(45deg, #FF4B00, #FF7034); color: white; border-radius: 12px; width: 100%; height: 50px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🏛️ OASIS ART STUDIO</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📸 Análisis Referencia", "✍️ Tu Idea de Autor", "📅 Agenda Oasis"])

with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Análisis de Complejidad")
    foto = st.file_uploader("Sube tu referencia", type=["jpg", "png", "jpeg"])
    if foto:
        st.image(Image.open(foto), use_container_width=True)
        st.info("🤖 IA: Esperando descripción técnica en la siguiente pestaña para cruzar datos.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Cuéntame tu Visión")
    st.write("Para que nuestra IA calcule un presupuesto preciso, describe tu idea siguiendo estos ejemplos:")
    
    # --- BLOQUE DE INTELIGENCIA / GUÍA AL CLIENTE ---
    st.markdown("""
    <div class='ejemplo-box'>
        <b>Ejemplo 1:</b> "Un tatuaje de 3 pulgadas a color, estilo Neotraditional, un poco más arriba del codo."<br><br>
        <b>Ejemplo 2:</b> "Un tatuaje Blackwork en mi muslo de 14 pulgadas con detalles tribales."
    </div>
    """, unsafe_allow_html=True)
    
    vision = st.text_area("¿Qué tienes en mente? (Incluye tamaño en pulgadas y ubicación)", placeholder="Ej: 5 pulgadas, antebrazo, estilo neotribal...")
    
    if st.button("Analizar Idea con IA"):
        with st.spinner("Procesando dimensiones y complejidad..."):
            time.sleep(2)
            if vision:
                st.success("✅ Datos recibidos. La IA ha detectado los parámetros de escala y ubicación.")
                st.write("Victor revisará esta descripción junto a tu referencia para validar el presupuesto final.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Reserva de Fecha")
    fecha = st.date_input("Selecciona tu día", min_value=date.today())
    st.write(f"Has seleccionado: {fecha}")
    st.markdown("</div>", unsafe_allow_html=True)

# --- BILLETERA DE RESERVA ---
st.markdown(f"""
    <div class='card' style='border: 1px solid #FF4B00;'>
        <h3 style='color: #FF4B00 !important; border:none;'>💳 DEPÓSITO DE RESERVA</h3>
        <p style='font-size: 1.2em;'>Monto: <strong>$60.00</strong></p>
        <p style='color: #888; font-size: 0.85em;'>Este monto asegura tu espacio en Oasis y se deduce del precio total de la obra.</p>
    </div>
    """, unsafe_allow_html=True)
