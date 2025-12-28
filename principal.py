import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración del Oasis
st.set_page_config(page_title="Oasis | Presupuesto Pro", layout="wide")

# 2. Estética Impecable
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    body {background-color: #0a0a0a;}
    </style>
    """, unsafe_allow_html=True)

# 3. La Interfaz con Motor de Cálculo Real
# He configurado un precio base de ejemplo para que veas el dinero moverse.
oasis_interface = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --gold: #d4af37; --ink: #0a0a0a; --glass: rgba(255,255,255,0.05); }
        body { margin: 0; background: var(--ink); color: white; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        
        .card { background: var(--glass); backdrop-filter: blur(20px); padding: 40px; border-radius: 40px; border: 1px solid rgba(255,255,255,0.1); width: 340px; text-align: center; box-shadow: 0 40px 100px rgba(0,0,0,0.7); }
        h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-style: italic; margin: 0; font-weight: 200; }
        .tagline { letter-spacing: 6px; text-transform: uppercase; font-size: 9px; color: var(--gold); margin-bottom: 35px; }
        
        .input-row { display: flex; gap: 10px; margin-bottom: 15px; }
        input { width: 100%; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.1); padding: 15px; border-radius: 15px; color: white; outline: none; text-align: center; font-size: 16px; }
        
        .btn { width: 100%; padding: 18px; border-radius: 15px; border: none; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 10px; letter-spacing: 2px; transition: 0.4s; }
        .btn-gold { background: var(--gold); color: black; margin-top: 15px; }
        .btn-outline { background: transparent; border: 1px solid rgba(255,255,255,0.2); color: #888; }
        
        #result-box { margin-top: 25px; padding: 20px; border-radius: 20px; background: rgba(212, 175, 55, 0.1); border: 1px solid var(--gold); display: none; }
        .price { font-size: 24px; color: var(--gold); font-weight: 600; margin-top: 5px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Oasis</h1>
        <div class="tagline">Microanálisis Visual</div>
        
        <div class="input-row">
            <input type="number" id="width" placeholder="Ancho cm">
            <input type="number" id="height" placeholder="Alto cm">
        </div>
        
        <button class="btn btn-outline" onclick="document.getElementById('file-up').click()">📸 CARGAR REFERENCIA</button>
        <input type="file" id="file-up" hidden accept="image/*">
        
        <button class="btn btn-gold" onclick="calcular()">CALCULAR PRESUPUESTO</button>
        
        <div id="result-box">
            <div style="font-size: 10px; letter-spacing: 2px; color: #aaa;">INVERSIÓN ESTIMADA</div>
            <div class="price" id="final-price">$0.00</div>
            <div style="font-size: 9px; margin-top: 10px; color: var(--gold); cursor: pointer;" onclick="window.open('https://wa.me/Oasis-writer')">➔ AGENDAR CITA</div>
        </div>
    </div>

    <script>
        function calcular() {
            const w = document.getElementById('width').value;
            const h = document.getElementById('height').value;
            
            if(!w || !h) {
                alert("Por favor, ingresa las dimensiones para que el Director analice.");
                return;
            }

            // Lógica de Negocio: Área * Tarifa (Ejemplo $10 por cm2)
            const area = w * h;
            const tarifa = 10; 
            const total = area * tarifa;

            document.getElementById('final-price').innerText = "$" + total.toLocaleString();
            document.getElementById('result-box').style.display = "block";
        }
    </script>
</body>
</html>
"""

components.html(oasis_interface, height=900)
