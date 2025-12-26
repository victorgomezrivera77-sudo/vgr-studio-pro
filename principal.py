import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta
import PIL.Image
import google.generativeai as genai

# --- 1. CONFIGURACIÓN DE SEGURIDAD (SECRETS) ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def conectar_bunker():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    return client.open("oasis_Data").sheet1

# --- 2. INTERFAZ DE OASIS ---
st.title("🏝️ Oasis Bot")
st.subheader("Curaduría, Agenda y Registro Automatizado")

# SECCIÓN A: VISIÓN Y CURADURÍA
uploaded_file = st.file_uploader("Sube la referencia del tatuaje", type=["jpg", "jpeg", "png"])
analisis_texto = ""

if uploaded_file:
    img = PIL.Image.open(uploaded_file)
    st.image(img, caption="Referencia para análisis", use_container_width=True)
    if st.button("Ejecutar Curaduría"):
        with st.spinner("Analizando estética y técnica..."):
            response = model.generate_content(["Actúa como un curador de tatuajes experto. Analiza estilo, complejidad y tiempo estimado.", img])
            analisis_texto = response.text
            st.write(analisis_texto)

st.divider()

# SECCIÓN B: AGENDA Y REGISTRO
with st.form("bunker_form"):
    col1, col2 = st.columns(2)
    with col1:
        cliente = st.text_input("Nombre del Cliente")
        fecha_cita = st.date_input("Fecha de la Cita", min_value=datetime.today())
    with col2:
        precio = st.number_input("Precio ($USD)", min_value=0)
        hora_cita = st.time_input("Hora de la Cita")

    notas = st.text_area("Detalles adicionales", value=analisis_texto)
    
    btn_finalizar = st.form_submit_button("Sincronizar con el Búnker")

if btn_finalizar:
    try:
        hoja = conectar_bunker()
        fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cita_completa = f"{fecha_cita} a las {hora_cita}"
        
        # El bot escribe: Fecha Registro | Cliente | Cita | Precio | Análisis/Notas
        hoja.append_row([fecha_registro, cliente, cita_completa, precio, notas])
        
        st.success(f"✅ {cliente} agendado para el {cita_completa}. Datos blindados en oasis_Data.")
        st.balloons()
    except Exception as e:
        st.error(f"Falla en la sincronización: {e}")
