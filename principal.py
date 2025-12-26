import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import PIL.Image
import google.generativeai as genai

# --- CONFIGURACIÓN DE APIS ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def conectar_bunker():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    return client.open("oasis_Data").sheet1

# --- LÓGICA DE ESTIMACIÓN (LA ESENCIA DE LAS CAPTURAS) ---
def calcular_logistica(pulgadas, complejidad):
    # Valores basados en tus capturas
    precio_pulgada = {"Baja": 80, "Media": 110, "Alta": 160}
    horas_pulgada = {"Baja": 0.8, "Media": 1.2, "Alta": 2.0}
    
    inversion = pulgadas * precio_pulgada[complejidad]
    tiempo_total = pulgadas * horas_pulgada[complejidad]
    insumos = inversion * 0.15  # 15% para materiales premium
    sesiones = max(1, round(tiempo_total / 6)) # Sesiones de 6 horas aprox.
    
    return inversion, tiempo_total, insumos, sesiones

# --- INTERFAZ ESTÉTRICA OASIS ---
st.title("🏝️ Oasis Bot")
st.subheader("Curaduría Artística & Presupuesto Pro")

uploaded_file = st.file_uploader("Sube tu referencia", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = PIL.Image.open(uploaded_file)
    st.image(img, caption="Referencia lista para análisis", use_container_width=True)
    
    # Formulario de entrada
    idea = st.text_area("¿Qué tienes en mente?", placeholder="Ej: Busco un trabajo impecable...")
    zona = st.text_input("¿En qué zona del cuerpo?", value="Pantorrilla")
    pulgadas = st.number_input("Tamaño aprox. (pulgadas)", min_value=1, value=8)
    complejidad = st.select_slider("Nivel de Detalle", options=["Baja", "Media", "Alta"], value="Media")

    if st.button("VER MI PRESUPUESTO"):
        inv, tiempo, ins, ses = calcular_logistica(pulgadas, complejidad)
        
        # EL RECUADRO NEGRO DE TUS CAPTURAS
        st.markdown(f"""
        <div style="background-color: #121212; padding: 20px; border-radius: 10px; border: 1px solid #FF4B4B;">
            <p style="color: white; margin-bottom: 5px;">Inversión Estimada</p>
            <h1 style="color: white; margin-top: 0;">${inv:,.1f} USD</h1>
        </div>
        """, unsafe_allow_html=True)

        # LOGÍSTICA DE SESIÓN
        st.markdown(f"""
        <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; margin-top: 15px; border-left: 5px solid #FF4B4B;">
            <h3 style="color: white;">📋 LOGÍSTICA DE TU SESIÓN:</h3>
            <p style="color: white;">🕒 <b>Tiempo estimado:</b> Unas {tiempo:.1f} horas de trabajo.</p>
            <p style="color: white;">💉 <b>Insumos Premium:</b> ${ins:,.1f} USD (Material estéril y tintas de alta gama).</p>
            <p style="color: white;">📅 <b>Planificación:</b> Se estima en {ses} sesión(es).</p>
            <p style="font-style: italic; color: #aaaaaa; font-size: 0.9em;">
                ¡Siéntete libre de ajustar el tamaño o la idea para ver cómo cambia el presupuesto!
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.warning(f"⚠️ **Nota de Victor:** Este presupuesto es una guía. El precio final lo confirmaremos tú y yo en persona.")

        # BOTÓN DE SINCRONIZACIÓN AL BÚNKER
        if st.button("Sincronizar con el Búnker"):
            try:
                hoja = conectar_bunker()
                fecha = datetime.now().strftime("%d/%m/%Y")
                hoja.append_row([fecha, "Cliente Oasis", zona, pulgadas, inv, f"{tiempo}h / {ses} ses"])
                st.success("✅ Datos blindados en oasis_Data.")
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
