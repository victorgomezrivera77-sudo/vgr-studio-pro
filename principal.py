import streamlit as st
from PIL import Image, ImageFilter, ImageStat, ImageOps
import urllib.parse 

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Calculadora de Presupuestos", layout="centered")

# --- 2. EL CEREBRO HÍBRIDO (Modo Stencil Activado) ---
def analizar_complejidad(image):
    # A. ANÁLISIS DE COLOR (¿Hay tinta viva?)
    # (Se mantiene igual: busca saturación alta)
    img_hsv = image.convert("HSV")
    s = img_hsv.split()[1]
    stat_s = ImageStat.Stat(s)
    saturacion_promedio = stat_s.mean[0]
    es_color = saturacion_promedio > 50 

    if es_color:
        # Si es color, devolvemos la imagen original y el resultado
        return image, "FULL COLOR / REALISMO", 100

    # B. ANÁLISIS DE DENSIDAD (Modo Stencil/Esqueleto)
    # 1. Convertir a escala de grises
    img_gray = image.convert("L")
    
    # 2. Suavizar piel (Blur ligero para quitar ruido)
    img_blurred = img_gray.filter(ImageFilter.GaussianBlur(radius=1))

    # 3. BINARIZACIÓN RADICAL (Crear el Stencil)
    # Umbral: Define qué tan oscuro debe ser algo para ser considerado tinta.
    # Ajustable entre 80 (muy exigente) y 130 (más permisivo). 110 es un buen punto medio para piel.
    umbral = 110
    # La magia: Si pixel < umbral se vuelve NEGRO (0), si no BLANCO (255).
    img_stencil = img_blurred.point(lambda x: 0 if x < umbral else 255, '1')

    # 4. Calcular densidad sobre el STENCIL PURO
    # Invertimos para que el fondo sea negro y las líneas blancas, para contar la "luz" (tinta)
    img_inverted_stencil = ImageOps.invert(img_stencil.convert("L"))
    stat = ImageStat.Stat(img_inverted_stencil)
    # Calculamos el porcentaje de píxeles negros (tinta)
    densidad = (stat.sum[0] / (img_stencil.size[0] * img_stencil.size[1])) * 100
    
    # UMBRALES RE-CALIBRADOS PARA STENCIL PURO
    # Al ser blanco y negro puro, los números de densidad cambian.
    if densidad > 15: # Mucha tinta negra sólida
        resultado = "ALTA COMPLEJIDAD (Blackwork/Tribal Denso)"
        tarifa = 100
    elif densidad > 5: # Sombreado normal, líneas gruesas
        resultado = "MEDIA (Sombreado/Geométrico)"
        tarifa = 80
    else: # Pocas líneas finas
        resultado = "SIMPLE (Línea Fina/Minimalista)"
        tarifa = 60
        
    # Devolvemos la imagen del stencil para mostrarla y el resultado
    return img_stencil, resultado, tarifa

# --- 3. ESTÉTICA "LAVA" ---
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .stApp { background-color: #0a0a0a; }
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Bebas+Neue&display=swap');
        
        h1 { font-family: 'Bebas Neue', sans-serif; color: #FF3300; font-size: 3.5rem; text-align: center; margin-top: 10px; letter-spacing: 2px; line-height: 1; }
        .subtitle { color: white; text-align: center; font-family: 'Inter', sans-serif; letter-spacing: 1px; font-size: 12px; text-transform: uppercase; margin-bottom: 20px; opacity: 0.7; }
        
        .result-box { border: 2px solid #FF3300; background: rgba(255, 51, 0, 0.05); padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px; box-shadow: 0 0 20px rgba(255, 51, 0, 0.1); }
        .price-big { font-size: 50px; color: #FF3300; font-family: 'Bebas Neue'; }
        
        div.stButton > button { width: 100%; background: linear-gradient(45deg, #FF3300, #FF6600); color: white; border: none; padding: 18px; font-weight: bold; border-radius: 12px; margin-top: 15px; text-transform: uppercase; letter-spacing: 2px; box-shadow: 0 4px 15px rgba(255, 51, 0, 0.3); }
        .whatsapp-btn { display: block; width: 100%; background-color: #25D366; color: white; text-align: center; padding: 18px; border-radius: 12px; text-decoration: none; font-family: 'Inter', sans-serif; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; margin-top: 15px; }
        .stSlider > div > div > div > div { background-color: #FF3300; }
    </style>
""", unsafe_allow_html=True)

# --- 4. INTERFAZ ---
st.markdown("<h1>PRESUPUESTOS<br>DE TATUAJES</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>SISTEMA DE COTIZACIÓN AUTOMATIZADO</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("1. CARGAR IMAGEN ORIGINAL", type=['jpg', 'png', 'jpeg'])

final_image_processed = None
estilo = "..."
tarifa = 0

if uploaded_file is not None:
    original_image = Image.open(uploaded_file)
    width, height = original_image.size
    
    st.markdown("<div style='color:#FF3300; font-size:12px; margin-top:10px; text-align:center;'>BISTURÍ DIGITAL (Recorta el diseño)</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: crop_x = st.slider("↔ Ancho", 0, width, (0, width), label_visibility="collapsed")
    with col2: crop_y = st.slider("↕ Alto", 0, height, (0, height), label_visibility="collapsed")
    
    left, right = crop_x
    top, bottom = crop_y
    
    if right > left and bottom > top:
        # Imagen recortada a color
        cropped_image = original_image.crop((left, top, right, bottom))
        
        # --- EL CEREBRO ANALIZA ---
        # Recibimos la imagen procesada (stencil) y el resultado
        final_image_processed, estilo, tarifa = analizar_complejidad(cropped_image)
        
        # Mostrar resultados visuales
        c1, c2 = st.columns(2)
        with c1:
            st.image(cropped_image, caption="Tu Recorte", use_container_width=True)
        with c2:
            # Aquí mostramos lo que ve la IA (el Stencil)
            st.image(final_image_processed, caption="Lo que ve la IA (Esqueleto)", use_container_width=True)
            
        st.markdown(f"<div style='text-align: center; color: #FF3300; border: 1px solid #FF3300; padding: 10px; border-radius: 10px; margin: 10px 0; background: rgba(255,51,0,0.1); font-weight:bold;'>{estilo}</div>", unsafe_allow_html=True)
    else:
        st.warning("Ajusta los controles para ver la imagen.")

st.write("---")
w_in = st.number_input("2. ANCHO FINAL (Pulgadas)", value=0.0, step=0.5)
h_in = st.number_input("3. ALTO FINAL (Pulgadas)", value=0.0, step=0.5)

if st.button("CALCULAR PRECIO"):
    if final_image_processed is None:
        st.warning("⚠️ Ajusta el recorte primero.")
    elif w_in == 0:
        st.warning("⚠️ Faltan las medidas.")
    else:
        area_cm = (w_in * 2.54) * (h_in * 2.54)
        horas = area_cm / 45
        total = horas * tarifa
        if total < 80: total = 80
        total_final = int(total)
        
        st.markdown(f"""
        <div class='result-box'>
            <div style='font-size: 10px; color: #aaa; letter-spacing: 2px;'>INVERSIÓN TOTAL</div>
            <div class='price-big'>${total_final}</div>
            <div style='font-size: 12px; color: white; margin-top: 5px;'>
                {w_in}" x {h_in}" <br> 
                <span style='color:#FF3300'>{estilo}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        telefono = "12109045463"
        mensaje = f"Hola, quiero reservar este tatuaje:\n\n🔥 Estilo: {estilo}\n📏 Medidas: {w_in}x{h_in}\n💰 Precio: ${total_final}\n\n¿Cuándo tienes espacio?"
        link_whatsapp = f"https://wa.me/{telefono}?text={urllib.parse.quote(mensaje)}"
        
        st.markdown(f"""<a href="{link_whatsapp}" class="whatsapp-btn" target="_blank">AGENDAR CITA 📅</a>""", unsafe_allow_html=True)
