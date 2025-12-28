import streamlit as st
import streamlit.components.v1 as components

# CONFIGURACIÓN DE ADMINISTRACIÓN
st.set_page_config(page_title="Oasis | Microanálisis Pro", layout="wide")

# OCULTAR BASURA DE STREAMLIT (Estética Impecable)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    </style>
    """, unsafe_allow_html=True)

# EL CORAZÓN DEL OASIS: INTERFAZ COMPLETA
oasis_full_app = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --ink: #0a0a0a; --bg: #ffffff; --soft: #f4f4f4; }
        body, html { margin: 0; padding: 0; width: 100vw; height: 100vh; background: var(--bg); font-family: 'Inter', sans-serif; overflow: hidden; display: flex; align-items: center; justify-content: center; }
        .aura { position: absolute; width: 100%; height: 100%; background: radial-gradient(circle, #fff 0%, #f0f0f0 100%); z-index: -1; }
        
        /* Títulos */
        .hero { text-align: center; z-index: 1; }
        h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 200; font-style: italic; margin: 0; }
        p.tagline { letter-spacing: 5px; text-transform: uppercase; color: #999; font-size: 0.7rem; margin-top: 10px; }

        /* Botón ✧ Lanzador */
        #launcher { position: fixed; bottom: 40px; right: 40px; width: 75px; height: 75px; border-radius: 50%; background: var(--ink); color: white; border: none; cursor: pointer; font-size: 30px; box-shadow: 0 15px 40px rgba(0,0,0,0.2); z-index: 1000; transition: 0.5s; }
        #launcher:hover { transform: scale(1.1) rotate(90deg); }

        /* Ventana de Microanálisis */
        #window { position: fixed; bottom: 130px; right: 40px; width: 400px; height: 620px; background: white; border-radius: 35px; display: none; flex-direction: column; box-shadow: 0 25px 80px rgba(0,0,0,0.15); border: 1px solid rgba(0,0,0,0.03); overflow: hidden; z-index: 1000; }
        #header { padding: 30px; background: var(--ink); color: white; text-align: center; letter-spacing: 4px; font-size: 0.75rem; }
        #feed { flex: 1; padding: 25px; background: var(--soft); overflow-y: auto; display: flex; flex-direction: column; gap: 20px; }
        
        .bubble { max-width: 85%; padding: 16px; border-radius: 20px; font-size: 14px; line-height: 1.5; background: white; border: 1px solid #eee; animation: slideUp 0.4s ease; }
        .bot { align-self: flex-start; }
        .user-input-area { background: #fff; padding: 25px; display: flex; flex-direction: column; gap: 12px; border-top: 1px solid #eee; }

        /* Botones de Acción */
        .btn { width: 100%; padding: 16px; border-radius: 15px; border: 1px solid #eee; cursor: pointer; font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; }
        .primary { background: var(--ink); color: white; border: none; }
        .btn:hover { background: #f4f4f4; transform: translateY(-2px); }

        /* Inputs de Medidas */
        .input-group { display: flex; gap: 10px; }
        input[type="number"] { width: 100%; padding: 12px; border-radius: 10px; border: 1px solid #ddd; outline: none; }

        @keyframes slideUp { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div class="aura"></div>
    <div class="hero">
        <h1>Oasis</h1>
        <p class="tagline">Microanálisis Visual de Tatuajes</p>
    </div>

    <button id="launcher" onclick="toggle()">✧</button>
    
    <div id="window">
        <div id="header">CENTRO DE CURADURÍA</div>
        <div id="feed" id="chatFeed">
            <div class="bubble bot">Bienvenido al <strong>Oasis</strong>. Sube tu imagen y coloca las medidas para que el <strong>Director</strong> calcule tu presupuesto.</div>
        </div>
        
        <div class="user-input-area">
            <div class="input-group">
                <input type="number" id="ancho" placeholder="Ancho (cm)">
                <input type="number" id="alto" placeholder="Alto (cm)">
            </div>
            <input type="file" id="fileInp" hidden accept="image/*" onchange="iniciarAnalisis()">
            <button class="btn primary" onclick="document.getElementById('fileInp').click()">📸 CARGAR DISEÑO</button>
            <button class="btn" onclick="abrirChat()">💬 HABLAR CON ASISTENTE</button>
        </div>
    </div>

    <script>
        function toggle() {
            const w = document.getElementById('window');
            w.style.display = (w.style.display === 'flex') ? 'none' : 'flex';
        }

        function abrirChat() {
            const f = document.getElementById('feed');
            f.innerHTML += '<div class="bubble bot">¿En qué puedo ayudarte con tu diseño hoy?</div>';
            f.scrollTop = f.scrollHeight;
        }

        function iniciarAnalisis() {
            const ancho = document.getElementById('ancho').value;
            const alto = document.getElementById('alto').value;
            const f = document.getElementById('feed');

            if(!ancho || !alto) {
                alert("Por favor, ingresa las medidas primero.");
                return;
            }

            f.innerHTML += '<div style="text-align:center; color:#999; font-size:11px"><em>SUPERVISOR: Escaneando imagen...</em></div>';
            
            setTimeout(() => {
                f.innerHTML += '<div class="bubble bot"><strong>DIRECTOR:</strong> Estilo Detectado.<br><strong>ANALISTA:</strong> Complejidad evaluada para un área de ' + (ancho*alto) + 'cm².</div>';
                
                setTimeout(() => {
                    f.innerHTML += '<div class="bubble bot" style="border: 1px solid #d4af37"><strong>PRESUPUESTO:</strong> Basado en el microanálisis, tu pieza requiere una sesión profesional.</div>';
                    f.innerHTML += '<button class="btn primary" onclick="window.open(\'https://wa.me/Oasis-writer\')">📅 RESERVAR EN OASIS</button>';
                    f.scrollTop = f.scrollHeight;
                }, 1500);
            }, 2500);
        }
    </script>
</body>
</html>
"""

# RENDERIZADO FINAL
components.html(oasis_full_app, height=900)
