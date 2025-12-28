import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de Escena
st.set_page_config(page_title="Calculadora Oasis", layout="wide")

# 2. Estética Impecable (Oasis)
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px;}
    body {background-color: #0a0a0a;}
    </style>
    """, unsafe_allow_html=True)

# 3. Interfaz con el Algoritmo de 3 Motores
oasis_logic = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --gold: #d4af37; --ink: #0a0a0a; }
        body { margin: 0; background: var(--ink); color: white; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; }
        
        .card { background: rgba(255,255,255,0.05); backdrop-filter: blur(20px); padding: 40px; border-radius: 40px; border: 1px solid rgba(255,255,255,0.1); width: 350px; text-align: center; }
        h1 { font-family: 'Inter', sans-serif; font-size: 1.2rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 30px; color: white; }
        
        .input-row { display: flex; gap: 10px; margin-bottom: 15px; }
        input, select { width: 100%; background: rgba(0,0,0,0.5); border: 1px solid #333; padding: 15px; border-radius: 12px; color: white; outline: none; }
        
        .label-mini { font-size: 9px; color: var(--gold); text-align: left; margin-bottom: 5px; letter-spacing: 1px; }

        .btn { width: 100%; padding: 18px; border-radius: 15px; border: none; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 10px; letter-spacing: 2px; transition: 0.4s; }
        .btn-gold { background: var(--gold); color: black; margin-top: 15px; }
        
        #result-box { margin-top: 25px; padding: 20px; border-radius: 20px; background: rgba(212, 175, 55, 0.1); border: 1px solid var(--gold); display: none; }
        .price { font-size: 28px; color: var(--gold); font-weight: 600; }
    </style>
</head>
<body>
    <div class="card">
        <h1>CALCULADORA DE PRECIOS DE TATUAJES</h1>
        
        <div class="label-mini">DIMENSIONES (CM)</div>
        <div class="input-row">
            <input type="number" id="w" placeholder="Ancho">
            <input type="number" id="h" placeholder="Alto">
        </div>
        
        <div class="label-mini">NIVEL DE COMPLEJIDAD (MOTOR)</div>
        <select id="motor">
            <option value="100">ALTA (Realismo / Detalle) - $100/h</option>
            <option value="80">MEDIA (Sombreado / Color) - $80/h</option>
            <option value="60">SIMPLE (Lettering / Línea) - $60/h</option>
        </select>
        
        <button class="btn btn-gold" onclick="calcular()">CALCULAR PRESUPUESTO</button>
        
        <div id="result-box">
            <div style="font-size: 10px; color: #888;">INVERSIÓN ESTIMADA</div>
            <div class="price" id="final-price">$0.00</div>
            <div style="font-size: 9px; margin-top: 10px; color: var(--gold);">*Calculado bajo el sistema Oasis</div>
        </div>
    </div>

    <script>
        function calcular() {
            const w = document.getElementById('w').value;
            const h = document.getElementById('h').value;
            const tarifaHora = document.getElementById('motor').value;
            
            if(!w || !h) { alert("Ingresa las medidas"); return; }

            // ALGORITMO: (Área / factor_de_velocidad) * Tarifa_Hora
            // Estimamos que en 1 hora se tatúan aprox 50cm2 de complejidad media.
            const area = w * h;
            const horasEstimadas = area / 50; 
            const total = horasEstimadas * tarifaHora;

            // Precio mínimo de mesa: $80 (puedes ajustarlo)
            const precioFinal = total < 80 ? 80 : total;

            document.getElementById('final-price').innerText = "$" + Math.round(precioFinal).toLocaleString();
            document.getElementById('result-box').style.display = "block";
        }
    </script>
</body>
</html>
"""

components.html(oasis_logic, height=850)
