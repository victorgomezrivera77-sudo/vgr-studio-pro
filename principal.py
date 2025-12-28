import streamlit as st
import streamlit.components.v1 as components

# Configuración base del Oasis
st.set_page_config(page_title="Oasis | Microanálisis", layout="wide")

# Encapsulamos TODA la interfaz en una sola variable de texto
# Esto evita el error de la llave '}'
oasis_app = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --ink: #0a0a0a; --gold: #d4af37; --bg-soft: #f8f8f8; }
        body { margin: 0; background: #fff; font-family: 'Inter', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        .aura { position: absolute; width: 100%; height: 100%; background: radial-gradient(circle, #fff 0%, #f2f2f2 100%); z-index: -1; }
        .main-ui { text-align: center; }
        h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 200; font-style: italic; margin: 0; color: var(--ink); }
        
        /* Botón Flotante */
        #launcher { position: fixed; bottom: 40px; right: 40px; width: 75px; height: 75px; border-radius: 50%; background: var(--ink); color: #fff; border: none; cursor: pointer; font-size: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); z-index: 1000; transition: 0.4s; }
        #launcher:hover { transform: scale(1.1) rotate(90deg); }

        /* Ventana de Chat */
        #window { position: fixed; bottom: 130px; right: 40px; width: 400px; height: 620px; background: #fff; border-radius: 35px; display: none; flex-direction: column; box-shadow: 0 25px 70px rgba(0,0,0,0.15); border: 1px solid rgba(0,0,0,0.05); overflow: hidden; z-index: 1000; }
        #header { padding: 30px; background: var(--ink); color: #fff; text-align: center; letter-spacing: 4px; font-size: 11px; font-weight: 600; }
        #feed { flex: 1; padding: 25px; background: var(--bg-soft); overflow-y: auto; display: flex; flex-direction: column; gap: 20px; }
        #footer { padding: 25px; background: #fff; display: flex; flex-direction: column; gap: 12px; }

        .bubble { max-width: 85%; padding: 16px; border-radius: 20px; font-size: 14px; line-height: 1.5; box-shadow: 0 2px 5px rgba(0,0,0,0.02); }
        .bot { background: #fff; border: 1px solid #eee; align-self: flex-start; color: #333; }
        .log { font-style: italic; color: #999; font-size: 11px; text-align: center; width: 100%; margin: 5px 0; }
        
        .btn { width: 100%; padding: 16px; border-radius: 15px; border: 1px solid #eee; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 11px; letter-spacing: 1px; transition: 0.3s; }
        .primary { background: var(--ink); color: #fff; border: none; }
        .btn:hover { background: #f0f0f0; transform: translateY(-2px); }
    </style>
</head>
<body>
    <div class="aura"></div>
    <div class="main-ui">
        <h1>Oasis</h1>
        <p style="letter-spacing: 5px; text-transform: uppercase; color: #aaa; font-size: 0.7rem; margin-top: 10px;">Microanálisis & Curaduría</p>
    </div>

    <button id="launcher" onclick="toggle()">✧</button>
    
    <div id="window">
        <div id="header">SISTEMA DE PRECISIÓN VISUAL</div>
        <div id="feed" id="chatFeed">
            <div class="bubble bot">Bienvenido al <strong>Oasis</strong>. Sube la imagen de tu diseño para que nuestro <strong>Director</strong> calcule el presupuesto basado en los 10 estilos de mercado.</div>
        </div>
        <div id="footer">
            <input type="file" id="fileInp" hidden accept="image/*" onchange="iniciarAnalisis()">
            <button class="btn primary" onclick="document.getElementById('fileInp').click()">📸 INICIAR MICROANÁLISIS</button>
            <button class="btn">💬 CONSULTAR ASISTENTE</button>
        </div>
    </div>

    <script>
        function toggle() {
            const win = document.getElementById('window');
            win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
        }

        function iniciarAnalisis() {
            const feed = document.getElementById('feed');
            
            // Simulación de los Pisos de trabajo
            feed.innerHTML += '<div class="log">SUPERVISOR: Validando calidad de imagen...</div>';
            
            setTimeout(() => {
                feed.innerHTML += '<div class="bubble bot"><strong>DIRECTOR:</strong> Estilo detectado (Fine Line/Lettering).<br><strong>ANALISTA:</strong> Complejidad Nivel 2 confirmada.</div>';
                
                setTimeout(() => {
                    feed.innerHTML += '<div class="bubble bot"><strong>ANÁLISIS FINAL:</strong> Presupuesto calculado con éxito.</div>';
                    feed.innerHTML += '<button class="btn primary" style="margin-top:10px" onclick="window.open(\'https://wa.me/TU_NUMERO\')">📅 AGENDAR EN OASIS</button>';
                    feed.scrollTop = feed.scrollHeight;
                }, 1500);
            }, 2500);
        }
    </script>
</body>
</html>
"""

# Le pedimos a Streamlit que muestre nuestra interfaz sin intentar "leerla"
components.html(oasis_app, height=900, scrolling=False)
