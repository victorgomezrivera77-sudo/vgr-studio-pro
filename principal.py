import streamlit as st
import streamlit.components.v1 as components

# Piso 0: Configuración de la Administración
st.set_page_config(page_title="Oasis | Microanálisis", layout="wide")

# El Paquete (La interfaz que diseñamos con sus 10 categorías)
# Metemos TODO el código HTML/JS aquí adentro, entre las comillas triples
oasis_interface = """
<!DOCTYPE html>
<html>
<head>
    <style>
        :root { --ink: #0a0a0a; --gold: #d4af37; }
        body { background: #ffffff; font-family: 'Inter', sans-serif; margin: 0; }
        .main-title { text-align: center; margin-top: 20vh; }
        h1 { font-style: italic; font-weight: 200; font-size: 3rem; }
        #oasis-launcher { position: fixed; bottom: 40px; right: 40px; width: 70px; height: 70px; border-radius: 50%; background: var(--ink); color: white; border: none; cursor: pointer; font-size: 24px; }
        #oasis-window { position: fixed; bottom: 120px; right: 40px; width: 350px; height: 500px; background: white; border-radius: 25px; display: none; flex-direction: column; box-shadow: 0 20px 50px rgba(0,0,0,0.1); border: 1px solid #eee; overflow: hidden; }
        #header { padding: 20px; background: var(--ink); color: white; text-align: center; font-size: 12px; letter-spacing: 2px; }
        #feed { flex: 1; padding: 20px; background: #fafafa; overflow-y: auto; }
        #footer { padding: 20px; display: flex; flex-direction: column; gap: 10px; }
        .btn { width: 100%; padding: 12px; border-radius: 10px; border: 1px solid #eee; cursor: pointer; font-weight: 600; font-size: 11px; }
        .primary { background: var(--ink); color: white; border: none; }
    </style>
</head>
<body>
    <div class="main-title"><h1>Oasis</h1><p>MICROANÁLISIS</p></div>
    <button id="oasis-launcher" onclick="toggle()">✧</button>
    <div id="oasis-window">
        <div id="header">SISTEMA DE PRECISIÓN</div>
        <div id="feed">Sube una imagen para calcular presupuesto.</div>
        <div id="footer">
            <button class="btn primary" onclick="alert('Iniciando Supervisor...')">📸 SUBIR DISEÑO</button>
        </div>
    </div>
    <script>
        function toggle() { 
            const w = document.getElementById('oasis-window');
            w.style.display = w.style.display === 'flex' ? 'none' : 'flex';
        }
    </script>
</body>
</html>
"""

# Piso 1: El Director entrega el paquete a la web
components.html(oasis_interface, height=800)
