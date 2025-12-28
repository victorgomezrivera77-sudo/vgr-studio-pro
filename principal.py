import streamlit as st
from PIL import Image, ImageFilter, ImageStat, ImageOps
import urllib.parse 

# --- 1. CONFIGURACIÓN DE MARCA ---
# Cambio de Nombre oficial en la pestaña del navegador
st.set_page_config(page_title="Calculadora de Presupuestos", layout="centered")

# --- 2. EL CEREBRO HÍBRIDO (Mantiene la lógica anti-piel y color) ---
def analizar_complejidad(image):
    # A. ANÁLISIS DE COLOR (¿Hay tinta viva?)
    img_hsv = image.convert("HSV")
    s = img_hsv.split()[1]
    stat_s = ImageStat.Stat(s)
    saturacion_promedio = stat_s.mean[0]
    
    es_color = saturacion_promedio > 50 

    if es_color:
        return "FULL COLOR / REALISMO", 100

    # B. ANÁLISIS DE DENSIDAD (Blanco y Negro)
    img_gray = image.convert("L")
    # Filtro de contraste extremo para borrar piel
    img_contraste = ImageOps.autocontrast(img_gray, cutoff=10)
    
    edges = img_contraste.filter(ImageFilter.FIND_EDGES)
    stat_d = ImageStat.Stat(edges)
    densidad = stat_d.sum[0] / (image.size[0] * image.size[1]) * 1000
    
    if densidad > 35:
        return "ALTA COMPLEJIDAD (B&N)", 100
    elif densidad > 12:
        return "MEDIA (Sombreado)", 80
    else:
        return "SIMPLE (Línea)", 60

# --- 3. ESTÉTICA "LAVA" (Naranja con gotas de Rojo) ---
# Color principal: #FF3300
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .stApp { background-color: #0a0a0a; }
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Bebas+Neue&display=swap');
        
        /* Nuevo Título estilo Industrial/Moderno */
        h1 { 
            font-family: 'Bebas Neue', sans-serif; 
            color: #FF3300; 
            font-size: 3.5rem; 
            text-align: center; 
            margin-top: 10px;
            letter-spacing: 2px;
            line-height: 1;
        }
        
        .subtitle { 
            color: white; 
            text-align: center; 
            font-family: 'Inter', sans-serif; 
            letter-spacing: 1px; 
            font-size: 12px; 
            text-transform: uppercase; 
            margin-bottom: 20px; 
            opacity: 0.7;
        }
        
        /* Cajas de Resultados */
        .result-box { 
            border: 2px solid #FF3300; 
            background: rgba(255, 51, 0, 0.05); 
            padding: 20px; 
            border-radius: 15px; 
            text-align: center; 
            margin-top: 20px; 
            box-shadow: 0 0 20px rgba(255, 51, 0, 0.1);
        }
        .price-big { 
            font-size: 50px; 
            color: #FF3300; 
            font-family: 'Bebas Neue'; 
        }
        
        /* Botones Naranja Lava */
        div.stButton > button { 
            width: 100%; 
            background: linear-gradient(45deg, #FF3300, #FF6600);
            color: white; 
            border: none; 
            padding: 18px; 
            font-weight: bold; 
            border-radius: 12px; 
            margin-top: 15px; 
            text-transform: uppercase; 
            letter-spacing: 2px; 
            box-shadow: 0 4px 15px rgba(255, 51, 0, 0.3);
        }
        div.stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(255, 51, 0, 0.5);
            color: white;
        }
        
        .whatsapp-btn { display: block; width: 100%; background-color: #25D366; color: white; text-align: center; padding: 18px; border-radius: 12px; text-decoration: none; font-family: 'Inter', sans-serif; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; margin-top: 15px; }
        
        /* Estilo para los sliders de recorte */
        .stSlider > div > div > div > div { background-color: #FF3300; }
    </style>
""", unsafe_allow_html=True)

# --- 4. INTERFAZ ---

st.markdown("<h1>PRESUPUESTOS<br>DE TATUAJES</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>SISTEMA DE COTIZACIÓN AUTOMATIZADO</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("1. CARGAR IMAGEN ORIGINAL", type=['jpg', 'png', 'jpeg'])

final_image = None
estilo = "..."
tarifa = 0

if uploaded_file is not None:
    # Cargar imagen original
    original_image = Image.open(uploaded_file)
    width, height = original_image.size
    
    # --- MÓDULO DE RECORTE (BISTURÍ DIGITAL) ---
    st.markdown("<div style='color:#FF3300; font-size:12px; margin-top:10px;'>HERRAMIENTA DE RECORTE</div>", unsafe_allow_html=True)
    
    # Sliders para recortar
    col_crop1, col_crop2 = st.columns(2)
    with col_crop1:
        # Recorte horizontal (Izquierda - Derecha)
        crop_x = st.slider("Ancho (Recorte)", 0, width, (0, width), label_visibility="collapsed")
    with col_crop2:
        # Recorte vertical (Arriba - Abajo)
        crop_y = st.slider("Alto (Recorte)", 0, height, (0, height), label_visibility="collapsed")
    
    # Aplicar el recorte
    left, right = crop_x
    top, bottom = crop_y
    
    # Validar que no sea 0
    if right > left and bottom > top:
        final_image = original_image.crop((left, top, right, bottom))
        
        # Mostrar PREVIEW del recorte
        st.image(final_image, caption="IMAGEN LISTA PARA ANÁLISIS", use_container_width=True)
        
        # Analizar SOLO la imagen recortada
        estilo, tarifa = analizar_complejidad(final_image)
        
        st.markdown(f"<div style='text-align: center; color: #FF3300; border: 1px solid #FF3300; padding: 10px; border-radius: 10px; margin: 10px 0; background: rgba(255,51,0,0.1);'>DETECTADO: <b>{estilo}</b></div>", unsafe_allow_html=True)
    else:
        st.warning("Ajusta los controles para ver la imagen.")

st.write("---")
w_in = st.number_input("2. ANCHO FINAL (Pulgadas)", value=0.0, step=0.5)
h_in = st.number_input("3. ALTO FINAL (Pulgadas)", value=0.0, step=0.5)

if st.button("CALCULAR PRECIO"):
    if final_image is None:
        st.warning("⚠️ Sube y recorta la imagen primero.")
    elif w_in == 0:
        st.warning("⚠️ Faltan las medidas en pulgadas.")
    else:
        # Cálculo
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

        # WhatsApp Link
        telefono = "12109045463"
        mensaje = f"Hola, quiero reservar este tatuaje:\n\n🔥 Estilo: {estilo}\n📏 Medidas: {w_in}x{h_in}\n💰 Precio: ${total_final}\n\n¿Cuándo tienes espacio?"
        link_whatsapp = f"https://wa.me/{telefono}?text={urllib.parse.quote(mensaje)}"
        
        st.markdown(f"""<a href="{link_whatsapp}" class="whatsapp-btn" target="_blank">AGENDAR CITA 📅</a>""", unsafe_allow_html=True)
