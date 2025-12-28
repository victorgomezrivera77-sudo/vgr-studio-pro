import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# 1. Configuración del Oasis
st.set_page_config(page_title="Oasis | Motor Visual", layout="wide")

# 2. Estética de Fondo (Inyección directa)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    body {background-color: #0a0a0a;}
    </style>
    """, unsafe_allow_html=True)

# 3. La Interfaz Completa (Carga, Medidas y Estética)
# Asegúrate de copiar hasta las comillas finales """
oasis_interface = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --gold: #d4af37; --ink: #0a0a0a; }
        body { margin: 0; background: var(--ink); color: white; font-family: 'Inter', sans-serif; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; overflow: hidden; }
        .hero h1 { font-family: 'Playfair Display', serif; font-size: 3.8rem; font-style: italic; font-weight: 200; margin: 0; color: white; }
        .tagline { letter-spacing: 7px; text-transform: uppercase; font-size: 0.7rem; color: var(--gold); margin-bottom: 35px; }
        
        .panel { background: rgba(255,255,255,0.05); backdrop-filter: blur(15px); padding: 40px; border-radius: 40px; border: 1px solid rgba(255,255,255,0.1); width: 330px; display: flex; flex-direction: column; gap: 18px; box-shadow: 0 40px 100px rgba(0,0,0,0.6); }
        .input-group { display: flex; gap: 10px; }
        input { width: 100%; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); padding: 14px; border-radius: 12px; color: white; outline: none; font-size: 14px; }
        
        .btn { width: 100%; padding: 16px; border-radius: 14px; border: none; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 10px; letter-spacing: 2px; transition: 0.3s; }
        .btn-gold { background: var(--gold); color: black; margin-top: 10px; }
        .btn-gold:hover { transform: scale(1.03); background: #e5be4d; }
        .btn-outline { background: transparent; border: 1px solid rgba(255,255,255,0.2); color: white; }
        
        #chat-btn { position: fixed; bottom: 35px; right: 35px; width: 65px; height: 65px; border-radius: 50%; background: white; border: none; cursor: pointer; font-size: 22px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
    </style>
</head>
<body>
    <div class="hero"><h1>Oasis</h1></div>
    <div class="tagline">Microanálisis Visual</div>

    <div class="panel">
        <div class="input-group">
            <input type="number" id="w_cm" placeholder="Ancho cm">
            <input type="number" id="h_cm" placeholder="Alto cm">
        </div>
        
        <input type="file" id="real_up" hidden accept="image/*" onchange="document.getElementById('fake_btn').innerText = '✅ LISTO'">
        <button class="btn btn-outline" id="fake_btn" onclick="document.getElementById('real_up').click()">📸 CARGAR DISEÑO</button>
        
        <button class="btn btn-gold" onclick="alert('Analizando complejidad...')">INICIAR CÁLCULO</button>
    </div>

    <button id="chat-btn">💬</button>
</body>
</html>
"""

# 4. Renderizado Final (Sin errores)
components.html(oasis_interface, height=900)
