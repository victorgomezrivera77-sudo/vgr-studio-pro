import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# --- CONEXIÓN AL BÚNKER ---
def conectar_bunker():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # El bot lee la llave desde los Secrets de Streamlit
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    return client.open("oasis_Data").sheet1

# --- INTERFAZ OASIS ---
st.title("🏝️ Oasis Bot")
st.subheader("Sistema de Curaduría y Registro")

with st.form("registro_oasis"):
    cliente = st.text_input("Nombre / Idea del Tatuaje")
    zona = st.text_input("Zona del Cuerpo")
    precio = st.number_input("Precio ($USD)", min_value=0)
    
    btn_enviar = st.form_submit_button("Sincronizar con el Búnker")

if btn_enviar:
    try:
        hoja = conectar_bunker()
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        hoja.append_row([fecha, cliente, zona, precio])
        st.success(f"✅ Registro exitoso: {cliente} guardado en oasis_Data.")
        st.balloons()
    except Exception as e:
        st.error(f"Error en la conexión: {e}")
