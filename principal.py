import streamlit as st
from datetime import date

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Adrenaline Tattoo Studio", 
    layout="centered",
    page_icon="💉"
)

# --- 1. ENCABEZADO Y CARTEL (MANUAL DEL CLIENTE) ---
st.title("💉 Bienvenidos a Adrenaline")

with st.expander("📖 CÓMO INICIAR TU PROYECTO", expanded=True):
    st.write("""
    1. **Visualiza:** Sube tu referencia (opcional).
    2. **Describe:** Cuéntanos tu idea para cotizar.
    3. **Mide:** Elige pulgadas o centímetros (el sistema convierte solo).
    4. **Cotiza:** El algoritmo calcula el tiempo y costo exacto.
    5. **Reserva:** Bloquea tu fecha en el calendario.
    """)

# --- 2. EL AVATAR: STEPHANIE ---
st.info("👋 **Stephanie:** Hola. Soy la coordinadora de Adrenaline. Introduce tus datos abajo para generar tu presupuesto y reservar.")

# --- 3. FORMULARIO DE ENTRADA ---
col_foto, col_desc = st.columns([1, 2])

with col_foto:
    foto_referencia = st.file_uploader("Sube referencia (Opcional)", type=['jpg', 'png', 'jpeg'])

with col_desc:
    descripcion = st.text_area("Descripción de tu pieza:", placeholder="Ej: Cráneo con rosas neotradicionales...")

# Selección de unidad y medida
col_unidad, col_medida = st.columns(2)
with col_unidad:
    unidad = st.radio("Unidad de medida:", ["Pulgadas", "Centímetros"], horizontal=True)

with col_medida:
    if unidad == "Pulgadas":
        medida = st.number_input("Tamaño (Pulgadas)", min_value=1, value=5)
        pulgadas_reales = medida
    else:
        medida = st.number_input("Tamaño (Centímetros)", min_value=2, value=12)
        pulgadas_reales = medida / 2.54 # Conversión interna

# Lista de estilos base (Pilares)
estilo = st.selectbox("Estilo técnico:", ["Lettering Sencillo", "Neotradicional", "Neotribal", "Blackwork", "Realismo"])

# --- 4. ALGORITMO DE CÁLCULO (LÓGICA INTERNA) ---
factores_estilo = {
    "Lettering Sencillo": 0.4,
    "Neotradicional": 1.2,
    "Neotribal": 1.0,
    "Blackwork": 1.1,
    "Realismo": 1.8
}

factor = factores_estilo.get(estilo, 1.0)
horas_estimadas = round(pulgadas_reales * factor, 1)

# Variables de precio
precio_insumos = 50 
precio_por_hora = 100 
precio_final = (horas_estimadas * precio_por_hora) + precio_insumos

# --- 5. CALENDARIO ---
st.subheader("📅 Disponibilidad")
fecha_cita = st.date_input("Selecciona tu día", min_value=date.today())

# --- 6. EQUIPO DE ARTISTAS ---
st.divider()
st.subheader("🩸 Artistas Residentes")
artistas = ["Momo", "Steve", "Sonia", "Víctor"]
st.write(f"Especialistas disponibles: **{', '.join(artistas)}**")

# Recomendación inteligente
st.success(f"⚡ Para un trabajo **{estilo}**, cualquiera de nuestros artistas ({', '.join(artistas)}) está cualificado.")

# --- 7. RESUMEN Y ACCIÓN ---
if st.button("CALCULAR Y CONFIRMAR"):
    st.markdown("---")
    st.header("💀 Resumen del Proyecto")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        if foto_referencia:
            st.image(foto_referencia, width=150)
        st.write(f"**Idea:** {descripcion}")
        st.write(f"**Estilo:** {estilo}")
        st.write(f"**Tamaño:** {medida} {unidad}")
        st.write(f"**Fecha:** {fecha_cita}")
    
    with col_res2:
        st.metric(label="Tiempo de Sesión", value=f"{horas_estimadas} Horas")
        st.write(f"**Insumos estériles:** ${precio_insumos}")
        st.metric(label="Total Estimado", value=f"${precio_final:.2f}")
    
    st.info("📧 **Stephanie:** Datos recibidos. Te enviaremos la confirmación oficial al correo.")
