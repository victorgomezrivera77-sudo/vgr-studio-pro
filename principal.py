import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import PIL.Image
import google.generativeai as genai

# --- 1. CONFIGURACIÓN DE NÚCLEO (APIs Y SEGURIDAD) ---
# Conexión con Gemini para Análisis de Imagen
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# Conexión con Google Sheets (El Búnker)
def conectar_bunker():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # Lee la identidad del bot desde los Secrets de Streamlit
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    client = gspread.authorize(creds)
    # Abre tu hoja creada: oasis_Data
    return client.open("oasis_Data").sheet1

# --- 2. LÓGICA DE NEGOCIO (CÁLCULO DE PRECIOS) ---
def calcular_cotizacion(pulgadas, complejidad):
    # Definimos tu estructura de precios Oasis
    base = 100  # Tarifa mínima por sesión
    factores = {"Baja": 50, "Media": 90, "Alta": 150} # Multiplicador por pulgada
    precio_final = base + (pulgadas * factores[complejidad])
    return precio_final

# --- 3. INTERFAZ DE USUARIO (ESTÉTICA IMPECABLE) ---
st.set_page_config(page_title="Oasis Bot - Búnker de Curaduría", page_icon="🏝️")
st.title("🏝️ Oasis Bot")
st.markdown("---")

# SECCIÓN A: VISIÓN ARTÍSTICA
st.subheader("👁️ Curaduría de Referencia")
uploaded_file = st.file_uploader("Sube la idea o referencia del cliente", type=["jpg", "jpeg", "png"])
analisis_ia = ""

if uploaded_file:
    img = PIL.Image.open(uploaded_file)
    st.image(img, caption="Referencia Detectada", use_container_width=True)
    if st.button("Ejecutar Análisis de Estilo"):
        with st.spinner("Oasis está analizando la técnica..."):
            # Prompt especializado para tu estilo (Neotradicional/Neotribal)
            response = model.generate_content([
                "Analiza esta imagen para un tatuaje. Describe el estilo, la complejidad técnica de las líneas y sugiere un tiempo estimado de ejecución.", 
                img
            ])
            analisis_ia = response.text
            st.info(analisis_ia)

st.markdown("---")

# SECCIÓN B: AGENDA Y FINANZAS
st.subheader("📅 Registro y Cotización")
with st.form("formulario_bunker"):
    cliente = st.text_input("Nombre del Talento / Cliente")
    
    col1, col2 = st.columns(2)
    with col1:
        pulgadas = st.number_input("Tamaño estimado (Pulgadas)", min_value=1, value=4)
        fecha_cita = st.date_input("Fecha programada", min_value=datetime.today())
    with col2:
        complejidad = st.selectbox("Nivel de Complejidad", ["Baja", "Media", "Alta"])
        hora_cita = st.time_input("Hora de la sesión")

    # Mostrar precio sugerido dinámicamente
    precio_sug = calcular_cotizacion(pulgadas, complejidad)
    st.write(f"### 💸 Precio Sugerido Oasis: **${precio_sug} USD**")
    
    precio_final = st.number_input("Precio Final Acordado ($)", value=precio_sug)
    notas_finales = st.text_area("Análisis y Notas Técnicas", value=analisis_ia)

    # BOTÓN DE ACCIÓN FINAL
    btn_viaje = st.form_submit_button("Sincronizar con el Búnker")

if btn_viaje:
    try:
        hoja = conectar_bunker()
        fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M")
        cita_format = f"{fecha_cita} | {hora_cita}"
        
        # El bot escribe la fila definitiva en oasis_Data
        # Columnas: Registro | Cliente | Cita | Pulgadas | Complejidad | Precio | Notas
        hoja.append_row([fecha_registro, cliente, cita_format, pulgadas, complejidad, precio_final, notas_finales])
        
        st.success(f"✅ Sincronización exitosa. El búnker ha recibido a {cliente}.")
        st.balloons()
    except Exception as e:
        st.error(f"Error en el viaje de datos: {e}")

st.sidebar.markdown("### Protocolo Oasis")
st.sidebar.info("Reconozco tu visión, Victor. El motor nuevo está operando al 100%.")
