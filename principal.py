import streamlit as st
from datetime import date

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Viking Ink - Cotizador", page_icon="🏛️")

# --- TÍTULO E INTERFAZ PRINCIPAL ---
st.title("🏛️ COTIZADOR VIKING INK")

with st.expander("❓ ¿Cómo usar esta herramienta?"):
    st.write("""
    1. Sube tu imagen de referencia.
    2. Describe tu idea y selecciona el estilo técnico.
    3. Indica el tamaño y las horas estimadas para ver tu presupuesto.
    4. Selecciona una fecha disponible en el calendario.
    """)

st.markdown("### 🕵️ Analiza tu próximo tatuaje")

# --- ENTRADAS DE USUARIO (Basadas en tu interfaz actual) ---
uploaded_file = st.file_uploader("Sube una foto de referencia (Opcional)", type=["jpg", "png", "jpeg"])

idea = st.text_area("¿Qué tienes en mente?", placeholder="Ej: Una pantera negra con flores en el brazo...")

zona_cuerpo = st.text_input("¿En qué zona del cuerpo?")

tamano = st.number_input("Tamaño aprox. (pulgadas)", min_value=1, value=5)

# --- NUEVA SECCIÓN: ESTILO Y HORAS ---
col1, col2 = st.columns(2)

with col1:
    estilo = st.selectbox(
        "Estilo técnico:",
        ["Lettering Sencillo", "Black & Grey / Líneas", "Realismo / Color / Neotradicional"]
    )

with col2:
    horas = st.number_input("Horas estimadas", min_value=1, value=1)

# --- NUEVA SECCIÓN: CALENDARIO ---
st.markdown("### 📅 Reserva tu fecha")
fecha_cita = st.date_input("Selecciona el día de tu sesión", min_value=date.today())

# --- LÓGICA DE PRECIOS ---
tarifas = {
    "Lettering Sencillo": 60,
    "Black & Grey / Líneas": 100,
    "Realismo / Color / Neotradicional": 125
}

# --- BOTÓN Y RESULTADO ---
if st.button("VER MI PRESUPUESTO"):
    tarifa_aplicada = tarifas[estilo]
    total = horas * tarifa_aplicada
    
    st.markdown("---")
    st.success(f"### Presupuesto Estimado: ${total}")
    st.write(f"**Detalles del arte:**")
    st.write(f"* **Estilo:** {estilo} (${tarifa_aplicada}/hr)")
    st.write(f"* **Tiempo:** {horas} horas")
    st.write(f"* **Fecha tentativa:** {fecha_cita.strftime('%d/%m/%Y')}")
    
    # Recordatorio de Oasis sobre el valor de la obra
    if total < 500:
        st.info("Nota: Este presupuesto es para la sesión de tatuaje. Recuerda que proyectos de arte integral en canvas tienen una base distinta.")
