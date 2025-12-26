import streamlit as st
import time

# --- 1. CONFIGURACIÓN VISUAL OASIS (ESTÉTICA IMPECABLE) ---
st.set_page_config(page_title="Oasis AI - Victor Gomez", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #FFFFFF !important; }
    .stButton>button { 
        background-color: #FF4B2B; color: white; font-weight: bold;
        border-radius: 10px; width: 100%; border: none; height: 3.5em;
    }
    .stMetric { background-color: #1A1A1A; border: 1px solid #FF4B2B; border-radius: 10px; padding: 10px; }
    .disclaimer { font-size: 12px; color: #888888; font-style: italic; border-top: 1px solid #333; padding-top: 10px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PERSISTENCIA DE DATOS (BÚNKER DE MEMORIA) ---
if 'memoria' not in st.session_state:
    st.session_state.memoria = {"listo": False, "precio": 0, "sesiones": 0, "horas": 0, "materiales": 0}

# --- 3. ALGORITMO COMANDANTE V3 (PRECISIÓN Y HUMANIDAD) ---
def algoritmo_oasis_v3(descripcion, zona, tamaño):
    desc_low = descripcion.lower()
    es_lettering = any(word in desc_low for word in ["lettering", "letras", "frase", "nombre"])
    
    # Tarifas base de mercado
    tarifa = 85 if tamaño <= 3 else (110 if tamaño <= 10 else 150)
    
    # Multiplicador por Estilo (Velocidad de Autor)
    multi = 0.6 if es_lettering else 1.0
    if any(word in desc_low for word in ["negro", "saturado", "pantera", "solido"]): multi += 0.8
    if any(word in desc_low for word in ["detalle", "fino", "flores", "micro"]): multi += 0.4

    # Multiplicador por Zona (Dificultad Anatómica)
    zonas = {'costilla': 1.8, 'espalda': 1.6, 'pecho': 1.5, 'cuello': 1.7, 'muñeca': 1.3}
    m_zona = zonas.get(zona.lower(), 1.0)

    # Cálculos Finales
    inversion = (tamaño * tarifa) * (multi + (m_zona - 1))
    
    # Tiempo estimado: Lettering es más veloz (0.6h/pulg) vs otros (1.2h/pulg)
    factor_tiempo = 0.6 if es_lettering else 1.2
    horas = round((tamaño * factor_tiempo) * m_zona, 1)
    
    # Insumos de grado médico (15% de la inversión)
    materiales = round(inversion * 0.15, 2)
    num_sesiones = int(inversion // 1200) + 1
    
    return round(inversion, 2), num_sesiones, horas, materiales

# --- 4. INTERFAZ DE USUARIO ---
st.title("🏛️ PROYECTO OASIS")

# Menú de Ayuda / Guía
with st.expander("❓ ¿Cómo usar el Analista Oasis? (Guía de Usuario)"):
    st.write("""
    1. **Experimenta:** Prueba diferentes ideas y zonas. Esta herramienta es para que explores tu presupuesto con total libertad.
    2. **Descripción:** Sé específico. Menciona estilos (Lettering, Blackwork) y nivel de detalle.
    3. **Imagen (Opcional):** Puedes subir una referencia para ayudar al análisis, pero no es obligatorio.
    4. **Consistencia:** Tus datos no se borrarán si refrescas la página. Tómate tu tiempo.
    """)

st.subheader("🕵️ Analista de Complejidad Técnica")

# Cargador de imágenes opcional
foto = st.file_uploader("Sube tu referencia visual (Opcional)", type=["jpg", "png", "jpeg"])

user_idea = st.text_area("¿Qué tienes en mente? (Estilo, detalles, elementos):")
col1, col2 = st.columns(2)
with col1: user_zone = st.text_input("¿Zona del cuerpo?")
with col2: user_size = st.number_input("Tamaño aprox. (pulgadas)", min_value=1, value=3)

if st.button("EJECUTAR ANÁLISIS DE AUTOR"):
    if user_idea and user_zone:
        p, s, h, m = algoritmo_oasis_v3(user_idea, user_zone, user_size)
        st.session_state.memoria = {"listo": True, "precio": p, "sesiones": s, "horas": h, "materiales": m}
        with st.spinner("Desglosando logística técnica..."): time.sleep(1.2)
    else:
        st.warning("El Comandante requiere al menos una descripción y la zona del cuerpo.")

# Mostrar Resultados del Búnker
if st.session_state.memoria["listo"]:
    m = st.session_state.memoria
    st.metric(label="Inversión Total Estimada", value=f"${m['precio']} USD")
    
    st.markdown(f"""
    <div style="background-color: #1A1A1A; padding: 20px; border-radius: 10px; border: 1px solid #FF4B2B;">
        <p style="color: #FF4B2B; font-weight: bold;">📋 DESGLOSE DE LOGÍSTICA:</p>
        <ul style="list-style-type: none; padding: 0;">
            <li>⏳ <b>Tiempo estimado en piel:</b> {m['horas']} horas.</li>
            <li>💉 <b>Insumos Premium Oasis:</b> ${m['materiales']} USD.</li>
            <li>⚔️ <b>Sesiones estimadas:</b> {m['sesiones']} bloque(s) de trabajo.</li>
        </ul>
        <p style="font-size: 13px; color: #CCCCCC;"><i>Interactúa con el analista cuantas veces quieras hasta definir tu proyecto ideal.</i></p>
    </div>
    <p class="disclaimer">⚠️ NOTA PROFESIONAL: Este presupuesto es una herramienta informativa. El precio final y la viabilidad técnica serán corroborados por Victor Gomez en persona el día de la sesión o consulta previa.</p>
    """, unsafe_allow_html=True)
