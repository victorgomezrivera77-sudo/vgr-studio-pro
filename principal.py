import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de Marca
st.set_page_config(page_title="Oasis | Calculadora Pro", layout="wide")

# Ocultar elementos de Streamlit para mantener la estética pura
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px;}
    body {background-color: #0a0a0a;}
    </style>
    """, unsafe_allow_html=True)

# 2. El Corazón del Oasis (HTML/JS Avanzado)
oasis_final_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --gold: #d4af37; --ink: #0a0a0a; --glass: rgba(255,255,255,0.03); }
        body { margin: 0; background: var(--ink); color: white; font-family: 'Inter', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        
        .container { width: 340px; text-align: center; animation: fadeIn 1.5s ease; }
        h1 { font-family: 'Playfair Display', serif; font-size: 4rem; font-style: italic; font-weight: 200; margin: 0; color: white; }
        .subtitle { letter-spacing: 5px; text-transform: uppercase; font-size: 9px; color: var(--gold); margin-bottom: 30px; }

        .card { background: var(--glass); backdrop-filter: blur(15px); padding: 30px; border-radius: 40px; border: 1px solid rgba(255,255,255,0.1); }
        
        .input-row { display: flex; gap: 10px; margin-bottom: 12px; }
        input, select { background: rgba(0,0,0,0.7); border: 1px solid #222; padding: 15px; border-radius: 15px; color: white; width: 100%; outline: none; font-size: 14px; transition: 0.3s; }
        input:focus { border-color: var(--gold); }

        .btn-gold { width: 100%; padding: 18px; border-radius: 18px; border: none; background: var(--gold); color: black; font-weight: 600; text-transform: uppercase; font-size: 10px; letter-spacing: 2px; cursor: pointer; margin-top: 15px; transition: 0.4s; }
        .btn-gold:hover { background: white; transform: translateY(-3px); }

        #result-box { margin-top: 20px; padding: 20px; border-radius: 20px; background: rgba(212, 175, 55, 0.05); border: 1px solid var(--gold); display: none; animation: slideUp 0.5s ease; }
        .price { font-size: 30px; color: var(--gold); font-weight: 200; }

        /* Chat de IA de Victor */
        #chat-trigger { position: fixed; bottom: 20px; right: 20px; width: 50px; height: 50px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 5px 20px rgba(0,0,0,0.5); }

        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        @keyframes slideUp { from { transform: translateY(10px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    </style>
</head>
<body>
    <div class="container">
        <h1>Oasis</h1>
        <div class="subtitle">CALCULADORA DE PRECIOS DE TATUAJES</div>
        
        <div class="card">
            <div class="input-row">
                <input type="number" id="w" placeholder="Ancho (cm)">
                <input type="number" id="h" placeholder="Alto (cm)">
            </div>
            
            <select id="motor">
                <option value="100">ALTA COMPLEJIDAD ($100/h)</option>
                <option value="80">MEDIO / SOMBRAS ($80/h)</option>
                <option value="60">SIMPLE / LINEA ($60/h)</option>
            </select>
            
            <button class="btn-gold" onclick="calculate()">GENERAR COTIZACIÓN</button>

            <div id="result-box">
                <div style="font-size: 9px; letter-spacing: 1px; opacity: 0.6;">INVERSIÓN ESTIMADA</div>
                <div class="price" id="total-val">$0.00</div>
                <div style="font-size: 8px; margin-top: 10px; color: var(--gold);">DIRECTOR: DISEÑO LISTO PARA RESERVA</div>
            </div>
        </div>
    </div>

    <div id="chat-trigger" onclick="alert('Oasis Director: Hola Victor, estoy monitoreando la sesión. La visión está lista para el siguiente nivel.')">
        <span style="font-size: 20px;">💬</span>
    </div>

    <script>
        function calculate() {
            const w = document.getElementById('w').value;
            const h = document.getElementById('h').value;
            const rate = document.getElementById('motor').value;
            
            if(!w || !h) { alert("Ingresa medidas"); return; }

            const area = w * h;
            // Calibración pro: área / velocidad de ejecución
            const hours = area / 45; 
            let total = hours * rate;

            // Mínimo de sesión/mesa
            if(total < 80) total = 80;

            document.getElementById('total-val').innerText = "$" + Math.round(total).toLocaleString();
            document.getElementById('result-box').style.display = 'block';
        }
    </script>
</body>
</html>
"""

components.html(oasis_final_code, height=800)
