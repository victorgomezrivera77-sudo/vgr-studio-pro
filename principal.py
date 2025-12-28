import streamlit as st
from PIL import Image, ImageFilter, ImageStat

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Oasis | Studio Mobile", layout="centered")

# --- 2. EL ALGORITMO (Calibrado para ser exigente) ---
def analizar_complejidad(image):
    # Convertir a escala de grises
    img_gray = image.convert("L")
    
    # Detectar bordes
    edges = img_gray.filter(ImageFilter.FIND_EDGES)
    
    # Calcular densidad de tinta (qué tanto 'blanco' queda)
    stat = ImageStat.Stat(edges)
    densidad = stat.sum[0] / (image.size[0] * image.size[1]) * 1000
    
    # NUEVOS UMBRALES (Ajustados por tus capturas)
    # Antes 25 -> Ahora 50 (El pájaro llegará aquí)
    # Antes 12 -> Ahora 20 (El fantasma o sombras)
    # Menos de 20 -> Simple (El elefante debería caer aquí)
    
    if densidad > 50:
        return "ALTA COMPLEJIDAD", 100
    elif densidad > 20:
        return "MEDIA (Sombreado)", 80
    else:
        return "SIMPLE (Línea)", 60

# --- 3. ESTÉTICA MÓVIL (Sin columnas que estorben) ---
st.markdown("""
    <style>
        /* Ocultar menú default */
        #MainMenu, footer, header {visibility: hidden;}
        .stApp { background-color: #0a0a0a; }
        
        /* Tipografía */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Playfair+Display:ital@1&display=swap');
        
        h1 { font-family: 'Playfair Display', serif; color: white; font-size: 3rem; text-align: center; font-style: italic; margin-top: 20px; }
        .subtitle { color: #d4af37; text-align: center; font-family: 'Inter', sans-serif; letter-spacing: 4px; font-size: 10px; text-transform: uppercase; margin-bottom: 20px; }
        
        /* Forzar visibilidad de textos */
        label { color: white !important; font-size: 12px !important; }
        .stFileUploader { margin-top: 20px; }
        
        /* Cajas de resultados */
        .result-box { border: 1px solid #333; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px; }
        .price-big { font-size: 40px; color: #d4af37; font-family: 'Playfair Display'; }
        
        /* Botón Dorado */
        div.stButton > button { width: 100%; background-color: #d4af37; color: black; border: none; padding: 18px; font-weight: bold; border-radius: 12px; margin-top: 15px; text-transform: uppercase; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# --- 4. INTERFAZ VISUAL ---
st.markdown("<h1>Oasis</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>CALCULADORA IMPERIAL</div>", unsafe_allow_html=True)

# Eliminamos las columnas para que se vea bien en el celular
uploaded_file = st.file_uploader("1. SUBE EL DISEÑO AQUÍ", type=['jpg', 'png', 'jpeg'])

# Variables iniciales
tarifa = 0
estilo = "Esperando diseño..."

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # Análisis automático
    estilo, tarifa = analizar_complejidad(image)
    
    # Mostrar imagen pequeña
    st.image(image, use_container_width=True)
    
    # Mostrar qué detectó la IA
    st.markdown(f"""
    <div style='text-align: center; color: #d4af37; border: 1px solid #d4af37; padding: 10px; border-radius: 10px; margin: 10px 0;'>
        DETECTADO: <b>{estilo} (${tarifa}/h)</b>
    </div>
    """, unsafe_allow_html=True)

# Inputs de medidas (Pulgadas)
st.write("---")
w_in = st.number_input("2. ANCHO (Pulgadas)", value=0.0, step=0.5)
h_in = st.number_input("3. ALTO (Pulgadas)", value=0.0, step=0.5)

if st.button("CALCULAR PRECIO"):
    if uploaded_file is None:
        st.warning("⚠️ Primero sube la imagen.")
    elif w_in == 0 or h_in == 0:
        st.warning("⚠️ Faltan las medidas.")
    else:
        # Conversión a CM y cálculo
        area_cm = (w_in * 2.54) * (h_in * 2.54)
        
        # Fórmula: Área / 45 cm2 por hora * Tarifa
        horas = area_cm / 45
        total = horas * tarifa
        
        # Mínimo de mesa
        if total < 80: total = 80
        
        st.markdown(f"""
        <div class='result-box'>
            <div style='font-size: 10px; color: #aaa; letter-spacing: 2px;'>PRESUPUESTO ESTIMADO</div>
            <div class='price-big'>${int(total)}</div>
            <div style='font-size: 10px; color: white; margin-top: 5px;'>
                MEDIDAS: {w_in}" x {h_in}" <br>
                ESTILO: {estilo}
            </div>
        </div>
        """, unsafe_allow_html=True)
