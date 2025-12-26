import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pandas as pd

# --- 1. CONFIGURACIÓN DE SEGURIDAD (SECRETS) ---
# Mantenemos la conexión al Búnker
def conectar_bunker():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    # Asegúrate de que el archivo se llame "oasis_Data"
    return client.open("oasis_Data").sheet1

# --- 2. INTERFAZ DE OASIS: GESTIÓN DE CITAS ---
st.set_page_config(page_title="Oasis Gestión", page_icon="🏝️")

st.title("🏝️ Oasis: Gestión de Citas")
st.subheader("Control de Agenda y Precios")

# SECCIÓN: REGISTRO DIRECTO
with st.form("gestion_citas"):
    col1, col2 = st.columns(2)
    with col1:
        cliente = st.text_input("Nombre del Cliente")
        fecha_cita = st.date_input("Fecha de la Cita", min_value=datetime.today())
        # Recordatorio de tu regla de oro: $500 mínimos o proyectos seleccionados
        precio = st.number_input("Precio Final ($USD)", min_value=0, step=50, help="Recuerda la curaduría de precios de Oasis")
    
    with col2:
        hora_cita = st.time_input("Hora de la Cita")
        proyecto = st.selectbox("Tipo de Proyecto", ["Tatuaje", "Diseño/Arte", "Consultoría", "Otro"])
        estatus = st.selectbox("Estatus del Pago", ["Pendiente", "Depósito Realizado", "Pagado Total"])

    detalles = st.text_area("Notas del Proyecto (Estética, tamaño, zona, etc.)")
    
    btn_sincronizar = st.form_submit_button("Sincronizar Cita con el Búnker")

# --- 3. LÓGICA DE ALMACENAMIENTO ---
if btn_sincronizar:
    if cliente and precio > 0:
        try:
            hoja = conectar_bunker()
            fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            cita_str = f"{fecha_cita} | {hora_cita.strftime('%H:%M')}"
            
            # Registro en el Búnker: 
            # Fecha Reg | Cliente | Proyecto | Cita | Precio | Estatus | Notas
            hoja.append_row([fecha_registro, cliente, proyecto, cita_str, precio, estatus, detalles])
            
            st.success(f"✅ Cita de {cliente} registrada exitosamente.")
            st.balloons()
        except Exception as e:
            st.error(f"Error al conectar con el Búnker: {e}")
    else:
        st.warning("Por favor, completa el nombre del cliente y el precio.")

st.divider()

# OPCIONAL: Visualización rápida de las últimas citas
if st.checkbox("Ver citas recientes"):
    try:
        hoja = conectar_bunker()
        data = hoja.get_all_records()
        if data:
            df = pd.DataFrame(data)
            st.table(df.tail(5)) # Muestra las últimas 5
    except:
        st.info("Conecta el Búnker para ver el historial.")
