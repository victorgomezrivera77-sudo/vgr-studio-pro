import streamlit as st
import streamlit.components.v1 as components

# Configuración del Oasis
st.set_page_config(page_title="Oasis | Calculadora", layout="wide")

# Estética Impecable: Ocultar menús de Streamlit
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    </style>
    """, unsafe_allow_html=True)

# Interfaz Unificada (Calculadora + Chat + Medidas)
# Usamos comillas triples para que no haya errores de llaves { }
oasis_html = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --ink: #0a0a0a; --soft: #f9f9f9; }
        body { margin: 0; background: #fff; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .hero { text-align: center; }
        h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 200; font-style: italic; margin: 0; }
        
        #launcher { position: fixed; bottom: 40px; right: 40px; width: 75px; height: 75px; border-radius: 50%; background: var(--ink); color: #fff; border: none; cursor: pointer; font-size: 30px; box-shadow: 0 15px 40px rgba(0,0,0,0.2); z-index: 1000; transition: 0.4s; }
        #window { position: fixed; bottom: 130px; right: 40px; width: 380px; height: 620px; background: white; border-radius: 35px; display: none; flex-direction: column; box-shadow: 0 25px 80px rgba(0,0,0,0.15); border: 1px solid #eee; overflow: hidden; z-index: 1000; }
        #header { padding: 25px; background: var(--ink); color: #fff; text-align: center; letter-spacing: 4px; font-size: 10px; }
        #feed { flex: 1; padding: 25px; background: var(--soft); overflow-y: auto; display: flex; flex-direction: column; gap: 15px; }
        #footer { padding: 25px; background: #fff; display: flex; flex-direction: column; gap: 10px; border-top: 1px solid #eee; }
        
        .bubble { padding: 15px; border-radius: 18px; font-size: 13px; background: #fff; border: 1px solid #eee; }
        .btn { width: 100%; padding: 15px; border-radius: 15px; border: 1px solid #eee; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 10px; letter-spacing: 1px; }
        .primary { background: var(--ink); color: #fff; border: none; }
        .input-m { width: 100%; padding: 12px; border-radius: 10px; border: 1px solid #ddd; box-sizing: border-box; }
    </style>
</head>
<body>
    <div class="hero"><h1>Oasis</h1><p style="letter-spacing: 5px; color: #999; font-size: 11px;">MICROANÁLISIS VISUAL</p></div>
    
    <button id="launcher" onclick="toggle()">✧</button>
    
    <div id="window">
        <div id="header">CENTRO DE CURADURÍA</div>
        <div id="feed">
            <div class="bubble">Bienvenido. Ingresa las medidas y carga tu diseño para que el <strong>Director</strong> analice la complejidad.</div>
        </div>
        <div id="footer">
            <div style="display:flex; gap:10px;">
                <input type="number" id="ancho" class="input-m" placeholder="Ancho (cm)">
                <input type="number" id="alto" class="input-m" placeholder="Alto (cm)">
            </div>
            <input type="file" id="up" hidden accept="image/*" onchange="analizar()">
            <button class="btn primary" onclick="document.getElementById('up').click()">📸 CARGAR DISEÑO</button>
            <button class="btn" onclick="alert('Abriendo Chat...')">💬 ASISTENTE</button>
        </div>
    </div>

    <script>
        function toggle() {
            const w = document.getElementById('window');
            w.style.display = (w.style.display === 'flex') ? 'none' : 'flex';
        }
        function analizar() {
            const f = document.getElementById('feed');
            const a = document.getElementById('ancho').value;
            const h = document.getElementById('alto').value;
            if(!a || !h) { alert('Ingresa medidas primero'); return; }
            
            f.innerHTML += '<div style="text-align:center; font-size:10px; color:#999"><em>SUPERVISOR: Escaneando...</em></div>';
            setTimeout(() => {
                f.innerHTML += '<div class="bubble"><strong>DIRECTOR:</strong> Estilo analizado.<br>Presupuesto calculado para ' + (a*h) + 'cm².</div>';
                f.innerHTML += '<button class="btn primary" onclick="window.open(\'https://wa.me/Oasis-writer\')">📅 AGENDAR EN OASIS</button>';
                f.scrollTop = f.scrollHeight;
            }, 2000);
        }
    </script>
</body>
</html>
"""

# Mostramos el Oasis con altura suficiente para que no se corte
components.html(oasis_html, height=1000)
