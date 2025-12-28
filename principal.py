import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la Obra
st.set_page_config(page_title="Oasis | Microanálisis", layout="wide")

# 2. Limpieza Visual (Escondemos los menús de Streamlit)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    </style>
    """, unsafe_allow_html=True)

# 3. El Cuerpo del Oasis (Interfaz, Medidas, Carga y Chat)
oasis_interface = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --ink: #0a0a0a; --gold: #d4af37; --soft: #f4f4f4; }
        body { margin: 0; background: #fff; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .hero { text-align: center; }
        h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 200; font-style: italic; margin: 0; }
        
        /* Sistema de Ventana Flotante */
        #launcher { position: fixed; bottom: 40px; right: 40px; width: 75px; height: 75px; border-radius: 50%; background: var(--ink); color: #fff; border: none; cursor: pointer; font-size: 30px; box-shadow: 0 15px 40px rgba(0,0,0,0.2); z-index: 1000; }
        #window { position: fixed; bottom: 130px; right: 40px; width: 400px; height: 650px; background: white; border-radius: 35px; display: none; flex-direction: column; box-shadow: 0 25px 80px rgba(0,0,0,0.15); border: 1px solid #eee; overflow: hidden; z-index: 1000; }
        
        #header { padding: 30px; background: var(--ink); color: #fff; text-align: center; letter-spacing: 4px; font-size: 11px; }
        #feed { flex: 1; padding: 25px; background: var(--soft); overflow-y: auto; display: flex; flex-direction: column; gap: 15px; }
        #footer { padding: 25px; background: #fff; display: flex; flex-direction: column; gap: 12px; border-top: 1px solid #eee; }
        
        .bubble { padding: 15px; border-radius: 20px; font-size: 14px; background: #fff; border: 1px solid #eee; }
        .btn { width: 100%; padding: 15px; border-radius: 15px; border: 1px solid #eee; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 11px; transition: 0.3s; }
        .primary { background: var(--ink); color: #fff; border: none; }
        .input-m { width: 100%; padding: 12px; margin-bottom: 5px; border-radius: 10px; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <div class="hero"><h1>Oasis</h1><p style="letter-spacing: 5px; color: #aaa;">MICROANÁLISIS VISUAL</p></div>
    
    <button id="launcher" onclick="toggle()">✧</button>
    
    <div id="window">
        <div id="header">CENTRO DE CURADURÍA</div>
        <div id="feed" id="chat">
            <div class="bubble">Ingresa las medidas y carga tu diseño para que el <strong>Director</strong> analice estilo y complejidad.</div>
        </div>
        <div id="footer">
            <div style="display:flex; gap:10px;">
                <input type="number" id="w" class="input-m" placeholder="Ancho">
                <input type="number" id="h" class="input-m" placeholder="Alto">
            </div>
            <input type="file" id="up" hidden accept="image/*" onchange="analizar()">
            <button class="btn primary" onclick="document.getElementById('up').click()">📸 SUBIR DISEÑO</button>
            <button class="btn" onclick="alert('Abriendo Chat...')">💬 ASISTENTE</button>
        </div>
    </div>

    <script>
        function toggle() {
            const win = document.getElementById('window');
            win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
        }
        function analizar() {
            const f = document.getElementById('feed');
            f.innerHTML += '<div style="text-align:center; font-size:11px; color:#999"><em>SUPERVISOR: Escaneando...</em></div>';
            setTimeout(() => {
                f.innerHTML += '<div class="bubble"><strong>DIRECTOR:</strong> Estilo y medidas procesadas.<br>Presupuesto listo.</div>';
                f.innerHTML += '<button class="btn primary" onclick="window.open(\'https://wa.me/Oasis-writer\')">📅 AGENDAR</button>';
                f.scrollTop = f.scrollHeight;
            }, 2000);
        }
    </script>
</body>
</html>
"""

# 4. Renderizado Final
components.html(oasis_interface, height=1000)
