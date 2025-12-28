import streamlit as st
from PIL import Image, ImageFilter, ImageStat

# --- 1. CONFIGURACIÓN DEL CEREBRO (BACKEND) ---
st.set_page_config(page_title="Oasis | Studio Pro", layout="centered")

# Función Algorítmica: CALIBRADA V2 (Menos sensible)
def analizar_complejidad(image):
    # Convertimos a escala de grises
    img_gray = image.convert("L")
    
    # Detectamos bordes
    edges = img_gray.filter(ImageFilter.FIND_EDGES)
    
    # Calculamos la densidad de tinta (Energía de la imagen)
    stat = ImageStat.Stat(edges)
    # Ajuste matemático: Promedio de píxeles de borde
    densidad = stat.sum[0] / (image.size[0] * image.size[1]) * 1000
    
    # --- NUEVA CALIBRACIÓN DE UMBRALES ---
    # Antes: >25 era Alto. Ahora exigimos >55 para ser "Realismo".
    # Antes: >12 era Medio. Ahora exigimos >20.
    
    if densidad > 55:  # Solo realismo denso, color full, sombras pesadas
        return "ALTA COMPLEJIDAD (Realismo)", 100
    elif densidad > 20: # Sombreado, puntillismo, líneas detalladas
        return "MEDIA (Sombras/Color)", 80
    else:               # Línea pura, siluetas, minimalismo (El Elefante caerá aquí)
        return "SIMPLE (Línea/Lettering)", 60

# --- 2. ESTÉTICA DE LUJO (FRONTEND) ---
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .stApp { background-color: #0a0a0a; }
        
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&family=Playfair+Display:ital@1&display=swap');
        
        h1 { font-family: 'Playfair Display', serif; color: white; font-size: 3.5rem; text-align: center; font-style: italic; font-weight: 200; margin-bottom: 0;}
        .subtitle { color: #d4af37; text-align: center; font-family: 'Inter', sans-serif; letter-spacing: 6px; font-size: 10px; text-transform: uppercase; margin-bottom: 40px; opacity: 0.8; }
        
        .metric-box { border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.03); padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 15px; }
        .metric-label { font-size: 9px; color: #888; letter-spacing: 2px; text-transform: uppercase; }
        .metric-value { font-size: 24px; color: #d4af37; font-family: 'Playfair Display', serif; }
        
        div.stButton > button { width: 100%; background-color: #d4af37; color: black; border: none; padding: 16px; text-transform: uppercase; letter-spacing: 2px; font-weight: 600; border-radius: 12px; margin-top: 10px; }
        div.stButton > button:hover { background-color: white; transform: scale(1.02); }
        
        /* Ajuste visual para inputs */
        label { color: #888 !important; font-size: 10px !important; letter-spacing: 1px !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. INTERFAZ ---

st.markdown("<h1>Oasis</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>CALCULADORA IMPERIAL</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 8, 1])

with col2:
    uploaded_file = st
