import streamlit as st
from datetime import date

# Configuración de página con estética Adrenaline
st.set_page_config(page_title="Adrenaline Tattoo Studio", layout="centered")

# --- 1. CARTEL DINÁMICO (MANUAL DEL CLIENTE) ---
# CAMBIO APLICADO AQUÍ: Jeringa y nombre "Adrenaline"
st.title("💉 Bienvenidos a Adrenaline")

with st.expander("📖 CÓMO USAR ESTA HERRAMIENTA (Actualizado)", expanded=True):
    st.write("""
    1. **Visualiza:** Sube una foto de referencia (opcional) para que Stephanie y los artistas entiendan tu idea.
    2. **Describe:** Escribe qué quieres tatuarte. Nuestro algoritmo analizará tu descripción para ajustar la precisión del presupuesto.
    3. **Mide:** Introduce el tamaño en **pulgadas o centímetros**. El sistema hará la conversión automática.
    4. **Estilo:** Selecciona uno de los estilos base. El sistema calculará las horas de trabajo y el precio final (incluyendo insumos) sin que tengas que adivinar.
    5. **Elige tu fecha:** Usa el calendario para separar tu espacio.
    """)

# --- 2. EL AVATAR: STEPHANIE ---
st.info("👋 **Stephanie:** Hola, soy la encargada de organizar tu sesión. Cuéntame qué tienes en mente para ayudarte con la cotización.")

# --- 3. FORMULARIO DE ENTRADA ---
col_foto, col_desc = st.columns([1, 2])

with col_foto:
    foto_referencia = st.file_uploader("Sube tu referencia (Opcional)", type=['jpg', 'png', 'jpeg'])

with col_desc:
    descripcion = st.text_area("¿Qué tienes en mente?", placeholder="Ej: Una pantera negra con flores en el antebrazo...")

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
        pulgadas_reales = medida / 2.54 # Convertimos a pulgadas para el algoritmo

# Lista de estilos base principales
estilo = st.selectbox("Estilo técnico base:", ["Lettering Sencillo", "Neotradicional", "Neotribal", "Blackwork", "Realismo"])

# --- 4. ALGORITMO DE CÁLCULO (EL MOTOR) ---
# Definimos factores de tiempo por estilo (horas por pulgada cuadrada o lineal aprox)
factores_estilo = {
    "Lettering Sencillo": 0.4,
    "Neotradicional": 1.2,
    "Neotribal": 1.0,
    "Blackwork": 1.1,
    "Realismo": 1.8
}

factor = factores_estilo.get(estilo, 1.0)
# Cálculo de horas basado en el tamaño y el estilo
horas_estimadas = round(pulgadas_reales * factor, 1)

# Variables de precio
precio_insumos = 50 # Base fija de materiales
precio_por_hora = 100 # Tu tarifa por hora
precio_final = (horas_estimadas * precio_por_hora) + precio_insumos

# --- 5. CALENDARIO DE RESERVA ---
st.subheader("📅 Reserva tu fecha")
fecha_cita = st.date_input("Selecciona el día de tu sesión", min_value=date.today())

# --- 6. SECCIÓN DE ARTISTAS (EDITABLE) ---
st.divider()
st.subheader("🎨 Nuestros Artistas")
# Lista de artistas actuales
artistas = ["Momo",
