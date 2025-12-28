import streamlit as st
from PIL import Image, ImageFilter, ImageStat, ImageOps
import urllib.parse 

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Oasis | Studio Mobile", layout="centered")

# --- 2. EL ALGORITMO HÍBRIDO (Color + Densidad) ---
def analizar_complejidad(image):
    # A. ANÁLISIS DE COLOR (¿Hay tinta de color viva?)
    # Convertimos a HSV (Matiz, Saturación, Valor)
    img_hsv = image.convert("HSV")
    # Extraemos solo el canal de Saturación (Qué tan vivo es el color)
    s = img_hsv.split()[1]
    # Calculamos cuánta "intensidad de color" hay
    stat_s = ImageStat.Stat(s)
    saturacion_promedio = stat_s.mean[0]
    
    # Lógica: La piel suele tener saturación baja (< 40). La tinta de color es alta (> 60).
    # Si la saturación promedio es alta, asumimos que es un diseño a Color.
    es_color = saturacion_promedio > 50 

    if es_color:
        return "FULL COLOR / REALISMO", 100

    # B. ANÁLISIS DE DENSIDAD (Si no es color, ¿qué tanta tinta negra hay?)
    # 1. Convertir a Escala de Grises
    img_gray = image.convert("L")
    
    # 2. FILTRO ANTI-PIEL (Contrastar al máximo)
    # Aumentamos el contraste para "quemar" la piel clara y dejar solo la tinta oscura
    img_contraste = ImageOps.autocontrast(img_gray, cutoff=10)
    
    # 3. Detectar bordes en la imagen limpia
    edges = img_contraste.filter(ImageFilter.FIND_EDGES)
    stat_d = ImageStat.Stat(edges)
    densidad = stat_d.sum[0] / (image.size[0] * image.size[1]) * 1000
    
    # UMBRALES DE TINTA NEGRA
    if densidad > 35:
        return "ALTA COMPLEJIDAD (B&N)", 100
    elif densidad > 12:
        return "MEDIA (Sombreado)", 80
    else:
        return "SIMPLE (Línea)", 60

# --- 3. ESTÉTICA ---
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .stApp { background-color: #0a0a0a; }
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Playfair+Display:ital@1&display=swap');
        
        h1 { font-family: 'Playfair Display', serif; color: white; font-size: 3rem; text-align: center; font-style: italic; margin-top: 10px; }
        .subtitle { color: #d4af37; text-align: center; font-family: 'Inter', sans-serif; letter-spacing: 4px; font-size: 10px; text-transform: uppercase; margin-bottom: 20px; }
        
        .result-box { border: 1px solid #333; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px; }
        .price-big { font-size: 40px; color: #d4af37; font-family: 'Playfair Display'; }
        
        div.stButton > button { width: 100%; background-color: #d4af37; color: black; border: none; padding: 18px; font-weight: bold; border-radius: 12px; margin-top: 15px; text-transform: uppercase; letter-spacing: 2px; }
        
        .whatsapp-btn { display: block; width: 100%; background-color: #25D366; color: white; text-align: center; padding: 18px; border-radius: 12px; text-decoration: none; font-family: 'Inter', sans-serif; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- 4. INTERFAZ ---
st.markdown("<h1>Oasis</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>CALCULADORA IMPERIAL</div>", unsafe_allow_html=True)

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
        area_cm = (w_in * 2.54) * (h_in * 2.54)
        horas = area_cm / 45
        total = horas * tarifa
        if total < 80: total = 80
        total_final = int(total)
        
        st.markdown(f"""
        <div class='result-box'>
            <div style='font-size: 10px; color: #aaa; letter-spacing: 2px;'>PRESUPUESTO ESTIMADO</div>
            <div class='price-big'>${total_final}</div>
            <div style='font-size: 10px; color: white; margin-top: 5px;'>{w_in}" x {h_in}" | {estilo}</div>
        </div>
        """, unsafe_allow_html=True)

        # TU NÚMERO
        telefono = "12109045463"
        mensaje = f"Hola, quiero reservar esta cotización del Oasis:\n\n💎 Estilo: {estilo}\n📏 Medidas: {w_in}x{h_in}\n💰 Precio: ${total_final}\n\n¿Tienes citas?"
        link_whatsapp = f"https://wa.me/{telefono}?text={urllib.parse.quote(mensaje)}"
        
        st.markdown(f"""<a href="{link_whatsapp}" class="whatsapp-btn" target="_blank">RESERVAR AHORA 💬</a>""", unsafe_allow_html=True)
