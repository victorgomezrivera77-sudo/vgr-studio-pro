import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página para que se vea impecable
st.set_page_config(page_title="Oasis | Microanálisis", layout="wide")

# EL CEREBRO: Aquí es donde Streamlit inyecta tu interfaz
oasis_interface = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        /* Tu CSS aquí (lo mantengo igual para no romper la estética) */
        :root { --oasis-bg: #ffffff; --oasis-ink: #0a0a0a; }
        body, html { margin: 0; padding: 0; background: var(--oasis-bg); font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .background-aura { position: absolute; width: 100%; height: 100%; background: radial-gradient(circle at 50% 50%, #ffffff 0%, #f4f4f4 100%); z-index: -1; }
        .main-title { text-align: center; }
        .main-title h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 200; font-style: italic; margin: 0; }
        #oasis-launcher { position: fixed; bottom: 40px; right: 40px; width: 75px; height: 75px; border-radius: 50%; background: #0a0a0a; color: white; border: none; cursor: pointer; font-size: 30px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); }
        #oasis-window { position: fixed; bottom: 130px; right: 40px; width: 420px; height: 600px; background: white; border-radius: 35px; display: none; flex-direction: column; box-shadow: 0 30px 100px rgba(0,0,0,0.18); border: 1px solid rgba(0,0,0,0.04); overflow: hidden; }
        #oasis-header { padding: 30px; background: #0a0a0a; color: white; text-align: center; letter-spacing: 4px; font-size: 0.8rem; }
        #oasis-feed { flex: 1; padding: 25px; overflow-y: auto; background: #f9f9f9; display: flex; flex-direction: column; gap: 20px; }
        .bubble { max-width: 85%; padding: 15px; border-radius: 20px; font-size: 14px; line-height: 1.6; }
        .bot { background: white; border: 1px solid #eee; align-self: flex-start; }
        #oasis-footer { padding: 25px; background: white; display: flex; flex-direction: column; gap: 10px; }
        .btn-action { width: 100%; padding: 15px; border-radius: 15px; border: 1px solid #eee; background: white; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 11px; }
        .primary { background: #0a0a0a !important; color: white !important; border: none; }
    </style>
</head>
<body>
    <div class="background-aura"></div>
    <div class="main-title">
        <h1>Oasis</h1>
        <p style="letter-spacing: 5px; text-transform: uppercase; color: #999; font-size: 0.7rem;">Microanálisis & Curaduría</p>
    </div>

    <button id="oasis-launcher" onclick="toggleOasis()">✧</button>
    <div id="oasis-window">
        <div id="oasis-header">SISTEMA DE PRECISIÓN</div>
        <div id="oasis-feed">
            <div class="bubble bot">Bienvenido. Sube tu imagen para iniciar el microanálisis visual.</div>
        </div>
        <div id="oasis-footer">
            <input type="file" id="imageInput" hidden onchange="runCerebro()">
            <button class="btn-action primary" onclick="document.getElementById('imageInput').click()">📸 SUBIR DISEÑO</button>
        </div>
    </div>

    <script>
        function toggleOasis() {
            const win = document.getElementById('oasis-window');
            win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
        }
        function runCerebro() {
            const feed = document.getElementById('oasis-feed');
            feed.innerHTML += '<div class="bubble bot"><em>SUPERVISOR: Analizando...</em></div>';
            setTimeout(() => {
                feed.innerHTML += '<div class="bubble bot"><strong>DIRECTOR:</strong> Estilo Detectado.<br><strong>ANALISTA:</strong> Complejidad evaluada.</div>';
            }, 2000);
        }
    </script>
</body>
</html>
"""

# Renderizar el componente en Streamlit
components.html(oasis_interface, height=900, scrolling=False)
