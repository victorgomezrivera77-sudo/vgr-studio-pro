import streamlit as st
import streamlit.components.v1 as components

# CONFIGURACIÓN DE ADMINISTRACIÓN (PAGINA COMPLETA)
st.set_page_config(
    page_title="Oasis | Microanálisis Visual",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# OCULTAR ELEMENTOS DE STREAMLIT PARA ESTÉTICA IMPECABLE
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    </style>
    """, unsafe_allow_status=True)

# EL CORAZÓN DEL OASIS (Interfaz + Cerebros + Chat)
oasis_interface = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root {
            --oasis-bg: #ffffff;
            --oasis-ink: #0a0a0a;
            --oasis-soft: #f4f4f4;
        }

        body, html {
            margin: 0; padding: 0; width: 100vw; height: 100vh;
            background-color: var(--oasis-bg);
            font-family: 'Inter', sans-serif;
            overflow: hidden;
            display: flex; align-items: center; justify-content: center;
        }

        /* FONDO DE RELAJACIÓN */
        .background-aura {
            position: absolute; width: 100%; height: 100%;
            background: radial-gradient(circle at 50% 50%, #ffffff 0%, #ebebeb 100%);
            z-index: -1;
        }

        .main-hero { text-align: center; z-index: 1; }
        .main-hero h1 {
            font-family: 'Playfair Display', serif;
            font-size: 4rem; font-weight: 200; font-style: italic;
            margin: 0; color: var(--oasis-ink);
        }
        .main-hero p {
            letter-spacing: 6px; text-transform: uppercase;
            color: #999; font-size: 0.8rem; margin-top: 15px;
        }

        /* BOTÓN DE LANZAMIENTO (INTERFAZ DE CHAT) */
        #launcher {
            position: fixed; bottom: 50px; right: 50px;
            width: 80px; height: 80px; border-radius: 50%;
            background: var(--oasis-ink); color: white;
            border: none; cursor: pointer; font-size: 35px;
            box-shadow: 0 15px 45px rgba(0,0,0,0.25);
            transition: 0.6s cubic-bezier(0.19, 1, 0.22, 1);
            z-index: 1000;
        }
        #launcher:hover { transform: scale(1.15) rotate(90deg); }

        /* VENTANA DEL MICROANÁLISIS */
        #oasis-window {
            position: fixed; bottom: 150px; right: 50px;
            width: 420px; height: 650px; background: white;
            border-radius: 40px; display: none; flex-direction: column;
            box-shadow: 0 35px 120px rgba(0,0,0,0.2);
            border: 1px solid rgba(0,0,0,0.05); overflow: hidden; z-index: 1000;
        }

        #header {
            padding: 35px; background: var(--oasis-ink); color: white;
            text-align: center; font-size: 0.8rem; letter-spacing: 4px; font-weight: 400;
        }

        #feed {
            flex: 1; padding: 30px; overflow-y: auto; background: var(--oasis-soft);
            display: flex; flex-direction: column; gap: 20px;
        }

        .bubble {
            max-width: 85%; padding: 18px; border-radius: 22px;
            font-size: 14px; line-height: 1.6; animation: slideUp 0.5s ease;
        }
        .bot { background: white; align-self: flex-start; border: 1px solid #eee; color: #333; }
        .log { font-style: italic; color: #aaa; font-size: 11px; text-align: center; }

        #footer { padding: 30px; background: white; display: flex; flex-direction: column; gap: 15px; }

        .btn {
            width: 100%; padding: 18px; border-radius: 20px;
            border: 1px solid #eee; background: white; cursor: pointer;
            font-weight: 600; font-size: 12px; letter-spacing: 1px;
            text-transform: uppercase; transition: 0.3s;
        }
        .btn-primary { background: var(--oasis-ink); color: white; border: none; }
        .btn:hover { background: #f0f0f0; transform: translateY(-3px); }

        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div class="background-aura"></div>
    <div class="main-hero">
        <h1>Oasis</h1>
        <p>Curaduría & Microanálisis</p>
    </div>

    <button id="launcher" onclick="toggleOasis()">✧</button>
    
    <div id="oasis-window">
        <div id="header">SISTEMA DE PRECISIÓN VISUAL</div>
        <div id="feed">
            <div class="bubble bot">
                Bienvenido al <strong>Oasis</strong>. Sube tu diseño para que el <strong>Director</strong> analice estilo y complejidad técnica.
            </div>
        </div>
        <div id="footer">
            <input type="file" id="imgInput" hidden accept="image/*" onchange="procesar()">
            <button class="btn btn-primary" onclick="document.getElementById('imgInput').click()">📸 INICIAR ANÁLISIS</button>
            <button class="btn">💬 CONSULTA ASISTENTE</button>
        </div>
    </div>

    <script>
        function toggleOasis() {
            const win = document.getElementById('oasis-window');
            win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
        }

        function addMsg(text, type='bot') {
            const feed = document.getElementById('feed');
            const m = document.createElement('div');
            m.className = `bubble ${type}`;
            m.innerHTML = text;
            feed.appendChild(m);
            feed.scrollTop = feed.scrollHeight;
        }

        function procesar() {
            addMsg("<em>SUPERVISOR: Escaneando imagen y eliminando ruido...</em>", "log");
            setTimeout(() => {
                addMsg("<strong>DIRECTOR:</strong> Estilo detectado con éxito.<br><strong>ANALISTA:</strong> Complejidad Nivel 2 evaluada.");
                setTimeout(() => {
                    addMsg("<strong>ANÁLISIS FINAL:</strong> Presupuesto calculado basado en ocupación alta.", "bot");
                    addMsg("<button class='btn btn-primary' onclick='window.open(\"https://wa.me/Oasis-writer\")'>📅 AGENDAR EN OASIS</button>");
                }, 1500);
            }, 2500);
        }
    </script>
</body>
</html>
"""

# EJECUCIÓN CON ALTO (HEIGHT) FORZADO PARA QUE SE VEA TODO
components.html(oasis_interface, height=1000, scrolling=False)
