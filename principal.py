import streamlit as st
import streamlit.components.v1 as components

# Configuración de Administración del Oasis
st.set_page_config(page_title="Oasis | Calculadora de Tattoo", layout="wide")

# Ocultar menús para estética impecable
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    </style>
    """, unsafe_allow_html=True)

# Interfaz y Motor de Cálculo (Cerebro y Cuerpo)
oasis_app = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --ink: #0a0a0a; --bg: #fdfdfd; }
        body { margin: 0; background: var(--bg); font-family: 'Inter', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        .hero { text-align: center; }
        h1 { font-family: 'Playfair Display', serif; font-size: 4rem; font-weight: 200; font-style: italic; margin: 0; }
        
        /* Interfaz de Calculadora */
        #launcher { position: fixed; bottom: 40px; right: 40px; width: 75px; height: 75px; border-radius: 50%; background: var(--ink); color: #fff; border: none; cursor: pointer; font-size: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); z-index: 1000; }
        #window { position: fixed; bottom: 130px; right: 40px; width: 400px; height: 600px; background: #fff; border-radius: 35px; display: none; flex-direction: column; box-shadow: 0 25px 70px rgba(0,0,0,0.15); border: 1px solid #eee; overflow: hidden; z-index: 1000; }
        #header { padding: 30px; background: var(--ink); color: #fff; text-align: center; letter-spacing: 4px; font-size: 11px; }
        #feed { flex: 1; padding: 25px; background: #f9f9f9; overflow-y: auto; display: flex; flex-direction: column; gap: 20px; }
        #footer { padding: 25px; display: flex; flex-direction: column; gap: 12px; }
        
        .bubble { max-width: 85%; padding: 15px; border-radius: 20px; font-size: 14px; line-height: 1.5; background: #fff; border: 1px solid #eee; }
        .btn { width: 100%; padding: 16px; border-radius: 15px; border: 1px solid #eee; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 11px; }
        .primary { background: var(--ink); color: #fff; border: none; }
    </style>
</head>
<body>
    <div class="hero"><h1>Oasis</h1><p style="letter-spacing: 5px; color: #999;">CALCULADORA DE PRECISIÓN</p></div>
    <button id="launcher" onclick="toggle()">✧</button>
    
    <div id="window">
        <div id="header">MICROANÁLISIS VISUAL</div>
        <div id="feed">
            <div class="bubble">Bienvenido. Sube una imagen para calcular el presupuesto basado en estilo y complejidad.</div>
        </div>
        <div id="footer">
            <input type="file" id="fileInp" hidden accept="image/*" onchange="calcular()">
            <button class="btn primary" onclick="document.getElementById('fileInp').click()">📸 SUBIR DISEÑO</button>
        </div>
    </div>

    <script>
        const GALERIAS = {
            "FINE_LINE": 15, "LETTERING": 12, "REALISMO": 150, "TRADICIONAL": 100, "NEOTRAD": 130
        };

        function toggle() {
            const w = document.getElementById('window');
            w.style.display = (w.style.display === 'flex') ? 'none' : 'flex';
        }

        function calcular() {
            const feed = document.getElementById('feed');
            feed.innerHTML += '<div style="text-align:center; font-size:11px; color:#aaa"><em>SUPERVISOR: Analizando complejidad...</em></div>';
            
            setTimeout(() => {
                feed.innerHTML += '<div class="bubble"><strong>DIRECTOR:</strong> Estilo Detectado.<br><strong>ANALISTA:</strong> Complejidad evaluada.</div>';
                feed.innerHTML += '<button class="btn primary" onclick="window.open(\'https://wa.me/Oasis-writer\')">📅 RESERVAR CITA</button>';
                feed.scrollTop = feed.scrollHeight;
            }, 2500);
        }
    </script>
</body>
</html>
"""

components.html(oasis_app, height=900)
