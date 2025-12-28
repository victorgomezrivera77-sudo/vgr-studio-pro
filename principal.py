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
