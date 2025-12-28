import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import io

# 1. Configuración de Escena
st.set_page_config(page_title="Oasis | Studio Pro", layout="wide")

# 2. El Alma del Oasis (Interfaz Negra y Dorada)
# He corregido las comillas para que NADA se rompa.
oasis_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    <style>
        :root { --gold: #d4af37; --ink: #0a0a0a; --gray: #1a1a1a; }
        body { margin: 0; background: var(--ink); color: white; font-family: 'Inter', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
        
        .card { background: var(--gray); padding: 40px; border-radius: 40px; border: 1px solid rgba(255,255,255,0.05); width: 320px; text-align: center; box-shadow: 0 50px 100px rgba(0,0,0,0.8); }
        h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-style: italic; margin: 0; font-weight: 200; }
        .subtitle { letter-spacing: 6px; text-transform: uppercase; font-size: 10px; color: var(--gold); margin-bottom: 30px; }
        
        .input-row { display: flex; gap: 10px; margin-bottom: 15px; }
        input { width: 100%; background: #000; border: 1px solid #333; padding: 12px; border-radius: 12px; color: white; outline: none; text-align: center; }
        
        .btn { width: 100%; padding: 15px; border-radius: 12px; border: none; cursor: pointer; font-weight: 600; text-transform: uppercase; font-size: 10px; letter-spacing: 1px; transition: 0.3s; }
        .btn-gold { background: var(--gold); color: black; margin-top: 10px; }
        .btn-gold:hover { background: #fff; transform: translateY(-2px); }
        .btn-upload { background: transparent; border: 1px solid #444; color: #888; margin-bottom: 5px; }
        
        #status { font-size: 11px; color: var(--gold); margin-top: 10px; display: none; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Oasis</h1>
        <div class="subtitle">Microanálisis Visual</div>
        
        <div class="input-row">
            <input type="number" id="w" placeholder="Ancho cm">
            <input type="number" id="h" placeholder="Alto cm">
        </div>
        
        <input type="file" id="upload" hidden onchange="showStatus()">
        <button class="btn btn-upload" onclick="document.getElementById('upload').click()">📸 CARGAR REFERENCIA</button>
        
        <div id="status">DISEÑO LISTO PARA ANALIZAR</div>
        
        <button class="btn btn-gold" onclick="analizar()">CALCULAR PRESUPUESTO</button>
    </div>

    <script>
        function showStatus() {
            document.getElementById('status').style.display = 'block';
        }
        function analizar() {
            const w = document.getElementById('w').value;
            const h = document.getElementById('h').value;
            if(!w || !h) { alert('Ingresa medidas'); return; }
            alert('Director: Procesando ' + (w*h) + ' cm²...');
        }
    </script>
</body>
</html>
"""

# Renderizado del componente
components.html(oasis_html, height=800)
