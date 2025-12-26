import streamlit as st
from datetime import date

# Configuración de página con estética Oasis
st.set_page_config(page_title="Oasis Tattoo Studio", layout="centered")

# --- 1. CARTEL DINÁMICO (MANUAL DEL CLIENTE) ---
st.title("🌿 Bienvenidos a Oasis")
with st.expander("📖 CÓMO USAR ESTA HERRAMIENTA (Actualizado)", expanded=True):
    st.write("""
    1. **Sube tu idea:** Sube una foto de referencia (opcional) y cuéntanos tu visión.
    2. **Define el tamaño:** Elige entre pulgadas o centímetros.
    3. **Selección técnica:** Elige el estilo. Stephanie y nuestro algoritmo calcularán el tiempo y precio por ti.
    4. **Reserva:** Selecciona tu fecha en el calendario y confirma.
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

estilo = st.selectbox("Estilo técnico:", ["Lettering Sencillo", "Neotradicional", "Neotribal", "Blackwork", "Realismo"])

# --- 4. ALGORITMO DE CÁLCULO (EL MOTOR) ---
# Definimos factores de tiempo por estilo (horas por pulgada cuadrada o lineal)
factores_estilo = {
    "Lettering Sencillo": 0.4,
    "Neotradicional": 1.2,
    "Neotribal": 1.0,
    "Blackwork": 1.1,
    "Realismo": 1.8
}

factor = factores_estilo.get(estilo, 1.0)
horas_estimadas = round(pulgadas_reales * factor, 1)
precio_insumos = 50 # Base fija de materiales
precio_por_hora = 100 # Tu tarifa por hora
precio_final = (horas_estimadas * precio_por_hora) + precio_insumos

# --- 5. CALENDARIO DE RESERVA ---
st.subheader("📅 Reserva tu fecha")
fecha_cita = st.date_input("Selecciona el día de tu sesión", min_value=date.today())

# --- 6. SECCIÓN DE ARTISTAS (EDITABLE) ---
st.divider()
st.subheader("🎨 Nuestros Artistas")
# Esta lista puede ser una base de datos más adelante
artistas = ["Momo", "Steve", "Sonia", "Víctor"]
st.write(f"En Oasis contamos con: **{', '.join(artistas)}**")

# Recomendación del algoritmo
st.success(f"✨ Basado en tu estilo ({estilo}), te recomendamos agendar con cualquiera de nuestros especialistas: {', '.join(artistas)}.")

# --- 7. RESUMEN Y CONFIRMACIÓN ---
if st.button("Confirmar Reserva y Calcular"):
    st.markdown("---")
    st.header("📋 Resumen de tu Reserva")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.write(f"**Descripción:** {descripcion}")
        st.write(f"**Estilo:** {estilo}")
        st.write(f"**Medida:** {medida} {unidad}")
        st.write(f"**Fecha:** {fecha_cita}")
    
    with col_res2:
        st.write(f"**Tiempo estimado:** {horas_estimadas} horas")
        st.write(f"**Insumos:** ${precio_insumos}")
        st.write(f"**Precio Total Estimado:** ${precio_final}")
    
    # LÓGICA DE ENVÍO (Simulación de correo)
    # Aquí es donde el Oasis-writer@... entraría en juego para disparar el mail
    datos_reserva = {
        "cliente": "Usuario Oasis",
        "descripcion": descripcion,
        "precio": precio_final,
        "fecha": fecha_cita,
        "artista_rec": artistas
    }
    st.info("📧 Stephanie: ¡Gracias! He recibido tu información. Te contactaré pronto para confirmar los detalles finales.")
    # st.write(f"DEBUG: Enviando correo a tu service account...") 
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
