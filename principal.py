import streamlit as st
import streamlit.components.v1 as components

# Configuración del Oasis
st.set_page_config(page_title="Oasis | Microanálisis", layout="wide")

# Limpieza de Interfaz
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    </style>
    """, unsafe_allow_html=True)

# Interfaz Integrada (Medidas + Carga + Chat)
oasis_interface = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --ink: #0a0a0a; --soft: #f8f8f8; }
        body { margin: 0; background: #fff; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .hero { text-align: center; }
        h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 200; font-style: italic; margin: 0; }
        #launcher { position: fixed; bottom: 40px; right: 40px; width: 75px; height: 75px; border-radius: 50%; background: var(--ink); color: #fff; border: none; cursor: pointer; font-size: 30px; box-shadow: 0 15px 40px rgba(0,0,0,0.2); z-index: 1000; }
        #window { position: fixed; bottom: 130px; right: 40px; width: 380px; height: 600px; background: white; border-radius: 35px; display: none; flex-direction: column; box-shadow: 0 25px 80px rgba(0,0,0,0.15); border: 1px solid #eee; overflow: hidden; z-index: 1000; }
        #header { padding: 25px; background: var(--ink); color: #fff; text-align: center; letter-spacing: 4px; font-size: 10px; }
        #feed { flex: 1; padding: 20px; background: var(--soft); overflow-y: auto; display: flex; flex-direction: column; gap: 15px; }
        #footer { padding: 25px; background: #fff; display: flex; flex-direction: column; gap: 10px; border-top: 1px solid #eee; }
        .bubble { padding: 15px; border-radius: 18px; font-size: 13px; background: #fff; border: 1px solid #eee; }
        .btn { width: 100%; padding: 14px; border-radius: 12px; border: 1px solid #eee; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 10px; }
        .primary { background: var(--ink); color: #fff; border: none; }
        .input-m { width: 100%; padding: 10px; border-radius: 8px; border: 1px solid #ddd; box-sizing: border-box; }
    </style>
</head>
<body>
    <div class="hero"><h1>Oasis</h1><p style="letter-spacing: 5px; color: #aaa; font-size: 12px;">MICROANÁLISIS VISUAL</p></div>
    <button id="launcher" onclick="toggle()">✧</button>
    <div id="window">
        <div id="header">CENTRO DE CURADURÍA</div>
        <div id="feed">
            <div class="bubble">Bienvenido. Indica las medidas y sube tu diseño para que el <strong>Director</strong> inicie el análisis.</div>
        </div>
        <div id="footer">
            <div style="display:flex; gap:8px;">
                <input type="number" id="w" class="input-m" placeholder="Ancho (cm)">
                <input type="number" id="h" class="input-m" placeholder="Alto (cm)">
            </div>
            <input type="file" id="up" hidden accept="image/*" onchange="run()">
            <button class="btn primary" onclick="document.getElementById('up').click()">📸 SUBIR DISEÑO</button>
            <button class="btn" onclick="alert('Iniciando Chat...')">💬 ASISTENTE</button>
        </div>
    </div>
    <script>
        function toggle() {
            const w = document.getElementById('window');
            w.style.display = (w.style.display === 'flex') ? 'none' : 'flex';
        }
        function run() {
            const f = document.getElementById('feed');
            f.innerHTML += '<div style="text-align:center; font-size:10px; color:#999"><em>SUPERVISOR: Procesando imagen...</em></div>';
            setTimeout(() => {
                f.innerHTML += '<div class="bubble"><strong>DIRECTOR:</strong> Análisis de complejidad completo.<br>Presupuesto generado.</div>';
                f.innerHTML += '<button class="btn primary" onclick="window.open(\'https://wa.me/Oasis-writer\')">📅 AGENDAR CITA</button>';
                f.scrollTop = f.scrollHeight;
            }, 2000);
        }
    </script>
</body>
</html>
"""

components.html(oasis_interface, height=1000)
