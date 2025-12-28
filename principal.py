import streamlit as st
import streamlit.components.v1 as components

# Configuración del Entorno Oasis
st.set_page_config(page_title="Oasis | Microanálisis", layout="wide")

# El Corazón: Interfaz, Galería de 10 Estilos y Chat
# Aquí encapsulamos todo el HTML/JS que diseñamos
oasis_full_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --ink: #0a0a0a; --soft: #f9f9f9; }
        body { margin: 0; background: #fff; font-family: 'Inter', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        .bg { position: absolute; width: 100%; height: 100%; background: radial-gradient(circle, #fff 0%, #f4f4f4 100%); z-index: -1; }
        .title { text-align: center; }
        h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 200; font-style: italic; margin: 0; }
        
        /* El Botón de Chat */
        #launcher { position: fixed; bottom: 40px; right: 40px; width: 70px; height: 70px; border-radius: 50%; background: var(--ink); color: #fff; border: none; cursor: pointer; font-size: 28px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); z-index: 1000; }
        
        /* La Ventana del Oasis */
        #window { position: fixed; bottom: 120px; right: 40px; width: 400px; height: 600px; background: #fff; border-radius: 30px; display: none; flex-direction: column; box-shadow: 0 20px 80px rgba(0,0,0,0.15); border: 1px solid #eee; overflow: hidden; z-index: 1000; }
        #header { padding: 25px; background: var(--ink); color: #fff; text-align: center; letter-spacing: 3px; font-size: 12px; }
        #feed { flex: 1; padding: 25px; background: var(--soft); overflow-y: auto; display: flex; flex-direction: column; gap: 15px; }
        #footer { padding: 25px; display: flex; flex-direction: column; gap: 10px; }
        
        .bubble { max-width: 85%; padding: 15px; border-radius: 18px; font-size: 14px; line-height: 1.5; }
        .bot { background: #fff; border: 1px solid #eee; align-self: flex-start; }
        .btn { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid #eee; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 11px; transition: 0.3s; }
        .primary { background: var(--ink); color: #fff; border: none; }
    </style>
</head>
<body>
    <div class="bg"></div>
    <div class="title"><h1>Oasis</h1><p style="letter-spacing: 4px; color: #999;">CURADURÍA VISUAL</p></div>

    <button id="launcher" onclick="toggle()">✧</button>
    <div id="window">
        <div id="header">MICROANÁLISIS DE PRECISIÓN</div>
        <div id="feed">
            <div class="bubble bot">Bienvenido al Oasis. Sube tu diseño para que el <strong>Director</strong> analice estilo y complejidad.</div>
        </div>
        <div id="footer">
            <input type="file" id="imgInp" hidden onchange="analizar()">
            <button class="btn primary" onclick="document.getElementById('imgInp').click()">📸 SUBIR IMAGEN</button>
            <button class="btn" onclick="alert('Conectando con Asistente...')">💬 CHAT DIRECTO</button>
        </div>
    </div>

    <script>
        const GALERIAS = {
            "FINE_LINE": 15, "LETTERING": 12, "REALISMO": 150, "TRADICIONAL": 100, "NEOTRAD": 130
        };

        function toggle() { 
            const w = document.getElementById('window');
            w.style.display = w.style.display === 'flex' ? 'none' : 'flex';
        }

        function analizar() {
            const f = document.getElementById('feed');
            f.innerHTML += '<div class="bubble bot"><em>Supervisor: Analizando pigmentos y complejidad...</em></div>';
            
            setTimeout(() => {
                f.innerHTML += '<div class="bubble bot"><strong>DIRECTOR:</strong> Estilo Detectado.<br><strong>ANALISTA:</strong> Complejidad evaluada.</div>';
                f.innerHTML += '<button class="btn primary" style="margin-top:10px" onclick="window.open(\'https://wa.me/Oasis-writer\')">📅 AGENDAR CITA</button>';
                f.scrollTop = f.scrollHeight;
            }, 2500);
        }
    </script>
</body>
</html>
"""

# Renderizado del bloque completo
components.html(oasis_full_code, height=900)
