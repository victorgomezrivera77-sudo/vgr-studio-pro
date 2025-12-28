import streamlit as st
from PIL import Image, ImageFilter, ImageStat

# --- 1. CONFIGURACIÓN DEL CEREBRO (BACKEND) ---
st.set_page_config(page_title="Oasis | Studio Pro", layout="centered")

# Función Algorítmica: El ojo que todo lo ve
def analizar_complejidad(image):
    img_gray = image.convert("L") # Escala de grises
    edges = img_gray.filter(ImageFilter.FIND_EDGES) # Detectar trazos
    stat = ImageStat.Stat(edges)
    densidad = stat.sum[0] / (image.size[0] * image.size[1]) * 1000
    
    # Decisión automática del motor
    if densidad > 25:
        return "ALTA COMPLEJIDAD", 100
    elif densidad > 12:
        return "SOMBRAS / COLOR", 80
    else:
        return "LÍNEA / SIMPLE", 60

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
    uploaded_file = st.file_uploader("CARGAR REFERENCIA (Sube tu diseño)", type=['jpg', 'png', 'jpeg'])

    # Variables por defecto
    tarifa_detectada = 0
    tipo_trabajo = "PENDIENTE"

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        # MI TRABAJO AUTÓNOMO: Analizo la imagen
        tipo_trabajo, tarifa_detectada = analizar_complejidad(image)
        
        st.image(image, caption="ANÁLISIS DE ESTILO COMPLETADO", use_container_width=True)
        
        # Muestro el resultado de mi análisis
        st.markdown(f"""
        <div class='metric-box'>
            <div class='metric-label'>ESTILO DETECTADO</div>
            <div class='metric-value'>{tipo_trabajo}</div>
            <div style='font-size: 9px; color: #555; margin-top:5px'>Motor activado: ${tarifa_detectada}/h</div>
        </div>
        """, unsafe_allow_html=True)

    # Inputs en PULGADAS
    c1, c2 = st.columns(2)
    with c1:
        w_in = st.number_input("ANCHO (Pulgadas)", value=0.0, step=0.5)
    with c2:
        h_in = st.number_input("ALTO (Pulgadas)", value=0.0, step=0.5)

    if st.button("CALCULAR INVERSIÓN"):
        # Validación: ¿Hay imagen y medidas?
        if uploaded_file is None:
            st.error("⚠️ El Director necesita ver el diseño primero.")
        elif w_in == 0 or h_in == 0:
            st.warning("⚠️ Ingresa las medidas en pulgadas.")
        else:
            # --- FÓRMULA DE CONVERSIÓN INVISIBLE ---
            # Convertimos pulgadas a cm para el motor interno
            # 1 pulgada = 2.54 cm
            w_cm = w_in * 2.54
            h_cm = h_in * 2.54
            area_cm = w_cm * h_cm
            
            # Algoritmo de tiempo (Base: 45 cm2 por hora)
            horas = area_cm / 45
            precio = horas * tarifa_detectada
            
            # Mínimo de sesión ($80)
            if precio < 80: precio = 80
            
            # SALIDA FINAL
            st.markdown(f"""
            <div style='background: rgba(212, 175, 55, 0.1); border: 1px solid #d4af37; padding: 30px; border-radius: 20px; text-align: center; margin-top: 20px; animation: fadeIn 1s;'>
                <div style='font-size: 10px; color: white; letter-spacing: 3px; opacity: 0.7;'>PRESUPUESTO ESTIMADO</div>
                <div style='font-size: 45px; color: #d4af37; font-family: "Playfair Display"; margin: 10px 0;'>${int(precio)}</div>
                <div style='font-size: 9px; color: #aaa;'>MEDIDAS: {w_in}" x {h_in}" | TARIFA: {tipo_trabajo}</div>
            </div>
            """, unsafe_allow_html=True)
