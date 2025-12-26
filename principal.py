import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN DEL BÚNKER (NUEVO MOTOR) ---
def conectar_hoja():
    # Usamos las credenciales del archivo JSON que ya tienes
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # IMPORTANTE: Para Streamlit Cloud, pegaremos el contenido del JSON en 'secrets'
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"], 
        scopes=scope
    )
    client = gspread.authorize(creds)
    # Conecta con tu hoja: oasis_Data
    return client.open("oasis_Data").sheet1

# --- INTERFAZ DE OASIS (ESTÉTICA MANTENIDA) ---
st.title("🏝️ Oasis Bot - Sistema de Curaduría")
st.subheader("Registro de Cotizaciones y Talento")

with st.form("cotizador_oasis"):
    col1, col2 = st.columns(2)
    with col1:
        cliente = st.text_input("Nombre del Cliente / Idea")
        zona = st.selectbox("Zona del cuerpo", ["Brazo", "Pierna", "Espalda", "Pecho", "Otro"])
    with col2:
        pulgadas = st.number_input("Tamaño (Pulgadas)", min_value=1, step=1)
        precio = st.number_input("Precio estimado ($USD)", min_value=0)

    horas = st.slider("Horas estimadas de sesión", 1, 10, 3)
    
    # Botón para activar el nuevo motor
    btn_registrar = st.form_submit_button("Registrar en el Búnker")

if btn_registrar:
    try:
        hoja = conectar_hoja()
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # El bot escribe la fila en tu oasis_Data
        hoja.append_row([fecha, cliente, zona, pulgadas, precio, horas])
        
        st.success(f"✅ {cliente} ha sido registrado con éxito en Oasis_Data.")
        st.balloons()
    except Exception as e:
        st.error(f"Error de conexión: {e}")

# --- PIE DE PÁGINA ---
st.info("Reconozco tu visión, Victor. El búnker está operando bajo el nuevo protocolo.")
