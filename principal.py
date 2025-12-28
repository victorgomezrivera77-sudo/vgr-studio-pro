import streamlit as st
import streamlit.components.v1 as components

# Configuración Maestra del Oasis
st.set_page_config(page_title="Oasis | Business Automation", layout="wide")

# Estética Impecable y Ocultamiento de herramientas estándar
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px;}
    body {background-color: #0a0a0a; color: white;}
    </style>
    """, unsafe_allow_html=True)

# Interfaz Avanzada: Curaduría + Inteligencia de Negocio
oasis_master_ui = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --gold: #d4af37; --ink: #0a0a0a; --glass: rgba(255,255,255,0.03); }
        body { margin: 0; background: var(--ink); font-family: 'Inter', sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; overflow-x: hidden; }
        
        .main-container { width: 90%; max-width: 400px; text-align: center; animation: fadeIn 2s ease; }
        h1 { font-family: 'Playfair Display', serif; font-size: 4rem; font-style: italic; font-weight: 200; margin: 0; letter-spacing: -2px; }
        .tagline { color: var(--gold); letter-spacing: 8px; text-transform: uppercase; font-size: 10px; margin-bottom: 40px; opacity: 0.8; }

        /* Panel de Control Pro */
        .panel { background: var(--glass); backdrop-filter: blur(20px); padding: 35px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.08); margin-bottom: 20px; transition: 0.5s; }
        .panel:hover { border-color: var(--gold); box-shadow: 0 0 30px rgba(212, 175, 55, 0.1); }
        
        .input-group { display: flex; gap: 10px; margin-bottom: 15px; }
        input, select { background: rgba(0,0,0,0.6); border: 1px solid #222; padding: 16px; border-radius: 18px; color: white; width: 100%; outline: none; font-size: 14px; }
        
        .btn-main { width: 100%; padding: 20px; border-radius: 20px; border: none; background: var(--gold); color: black; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; cursor: pointer; transition: 0.3s; }
        .btn-main:hover { transform: scale(1.02); background: #fff; }

        /* Chat Flotante (La Meta de Automatización) */
        #oasis-chat { position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; border-radius: 50%; background: white; color: black; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 10px 30px rgba(0,0,0,0.5); font-size: 24px; z-index: 1000; }

        /* Resultado Elegante */
        #result { margin-top: 25px; padding: 20px; border-radius: 25px; background: rgba(255,255,255,0.02); display: none; border: 1px dashed var(--gold); }
        .price-val { font-size: 32px; color: var(--gold); font-weight: 200; margin: 10px 0; }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div class="main-container">
        <h1>Oasis</h1>
        <div class="tagline">Calculadora de Precios de Tatuajes</div>

        <div class="panel">
            <div class="input-group">
                <input type="number" id="width" placeholder="Ancho (cm)">
                <input type="number" id="height" placeholder="Alto (cm)">
            </div>
            
            <select id="complexity">
                <option value="100">ALTA COMPLEJIDAD ($100/h)</option>
                <option value="80">SOMBRADO / COLOR ($80/h)</option>
                <option value="60">LETTERING / SIMPLE ($60/h)</option>
            </select>
            
            <button class="btn-main" style="margin-top: 20px;" onclick="calculate()">GENERAR COTIZACIÓN</button>

            <div id="result">
                <div style="font-size: 10px; letter-spacing: 2px; opacity: 0.6;">INVERSIÓN ESTIMADA</div>
                <div class="price-val" id="total-price">$0.00</div>
                <button class="btn-main" style="background: white; font-size: 9px; padding: 10px;" onclick="alert('Conectando con el Director...')">AGENDAR EN EL OASIS</button>
            </div>
        </div>
    </div>

    <div id="oasis-chat" onclick="alert('Oasis-AI: Hola Victor, estoy analizando tu visión...')">💬</div>

    <script>
        function calculate() {
            const w = document.getElementById('width').value;
            const h = document.getElementById('height').value;
            const rate = document.getElementById('complexity').value;
            
            if(!w || !h) return;

            // Algoritmo Oasis: (Área / factor de velocidad 40cm2/h) * Tarifa
            // Ajustamos a 40 para ser más precisos con la curaduría
            const area = w * h;
            const time = area / 40;
            let total = time * rate;

            // Precio base de mesa (Curaduría mínima)
            if(total < 80) total = 80;

            document.getElementById('total-price').innerText = "$" + Math.round(total).toLocaleString();
            document.getElementById('result').style.display = 'block';
        }
    </script>
</body>
</html>
"""

components.html(oasis_master_ui, height=900)
