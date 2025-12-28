import streamlit as st
from PIL import Image, ImageFilter, ImageStat
import urllib.parse # Necesario para crear el mensaje de WhatsApp

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Oasis | Studio Mobile", layout="centered")

# --- 2. EL ALGORITMO (Cerebro) ---
def analizar_complejidad(image):
    img_gray = image.convert("L")
    edges = img_gray.filter(ImageFilter.FIND_EDGES)
    stat = ImageStat.Stat(edges)
    densidad = stat.sum[0] / (image.size[0] * image.size[1]) * 1000
    
    if densidad > 50:
        return "ALTA COMPLEJIDAD", 100
    elif densidad > 20:
        return "MEDIA (Sombreado)", 80
    else:
        return "SIMPLE (Línea)", 60

# --- 3. ESTÉTICA DE LUJO ---
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .stApp { background-color: #0a0a0a; }
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Playfair+Display:ital@1&display=swap');
        
        h1 { font-family: 'Playfair Display', serif; color: white; font-size: 3rem; text-align: center; font-style: italic; margin-top: 10px; }
        .subtitle { color: #d4af37; text-align: center; font-family: 'Inter', sans-serif; letter-spacing: 4px; font-size: 10px; text-transform: uppercase; margin-bottom: 20px; }
        
        .warning-box { background: rgba(255, 0, 0, 0.1); border: 1px solid #ff4444; color: #ffcccc; padding: 15px; border-radius: 10px; font-size: 11px; text-align: center; margin-bottom: 15px; }
        .result-box { border: 1px solid #333; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px; }
        .price-big { font-size: 40px; color: #d4af37; font-family: 'Playfair Display'; }
        
        div.stButton > button { width: 100%; background-color: #d4af37; color: black; border: none; padding: 18px; font-weight: bold; border-radius: 12px; margin-top: 15px; text-transform: uppercase; letter-spacing: 2px; }
        
        /* Estilo para el enlace de WhatsApp (Botón de Reserva) */
        .whatsapp-btn {
            display: block;
            width: 100%;
            background-color: #25D366; /* Verde WhatsApp */
            color: white;
            text-align: center;
            padding: 18px;
            border-radius: 12px;
            text-decoration: none;
            font-family: 'Inter', sans-serif;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-top: 15px;
            border: 1px solid #128C7E;
        }
        .whatsapp-btn:hover { background-color: #128C7E; color: white; }
    </style>
""", unsafe_allow_html=True)

# --- 4. INTERFAZ ---
st.markdown("<h1>Oasis</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>CALCULADORA IMPERIAL</div>", unsafe_allow_html=True)

st.markdown("""
<div class='warning-box'>
    ⚠️ <b>REQUISITO OBLIGATORIO</b><br>
    Sube la imagen <b>RECORTADA</b> (Solo el diseño).<br>
    Sin fondos ni bordes de pantalla.
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("1. SUBE EL DISEÑO", type=['jpg', 'png', 'jpeg'])

estilo = "..."
tarifa = 0

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    estilo, tarifa = analizar_complejidad(image)
    st.image(image, use_container_width=True)
    st.markdown(f"<div style='text-align: center; color: #d4af37; border: 1px solid #d4af37; padding: 10px; border-radius: 10px; margin: 10px 0;'>DETECTADO: <b>{estilo}</b></div>", unsafe_allow_html=True)

st.write("---")
w_in = st.number_input("2. ANCHO (Pulgadas)", value=0.0, step=0.5)
h_in = st.number_input("3. ALTO (Pulgadas)", value=0.0, step=0.5)

if st.button("CALCULAR PRECIO"):
    if uploaded_file is None or w_in == 0:
        st.warning("⚠️ Faltan datos.")
    else:
        # Cálculos
        area_cm = (w_in * 2.54) * (h_in * 2.54)
        horas = area_cm / 45
        total = horas * tarifa
        if total < 80: total = 80
        total_final = int(total)
        
        # Mostramos el precio
        st.markdown(f"""
        <div class='result-box'>
            <div style='font-size: 10px; color: #aaa; letter-spacing: 2px;'>PRESUPUESTO ESTIMADO</div>
            <div class='price-big'>${total_final}</div>
            <div style='font-size: 10px; color: white; margin-top: 5px;'>{w_in}" x {h_in}" | {estilo}</div>
        </div>
        """, unsafe_allow_html=True)

        # --- 5. EL PUENTE A TU WHATSAPP ---
        # Tu número (sin espacios ni guiones)
        telefono = "12109045463"
        
        # El mensaje que le aparecerá al cliente
        mensaje = f"Hola Oasis Director, quiero reservar esta cotización:\n\n💎 Estilo: {estilo}\n📏 Medidas: {w_in}x{h_in} pulgadas\n💰 Presupuesto: ${total_final}\n\n¿Cuándo tienes disponibilidad?"
        
        # Codificamos el mensaje para internet (los espacios se vuelven %20, etc.)
        mensaje_encoded = urllib.parse.quote(mensaje)
        
        # El enlace mágico
        link_whatsapp = f"https://wa.me/{telefono}?text={mensaje_encoded}"
        
        # Botón HTML para ir a WhatsApp
        st.markdown(f"""
            <a href="{link_whatsapp}" class="whatsapp-btn" target="_blank">
                RESERVAR CITA AHORA 💬
            </a>
        """, unsafe_allow_html=True)
