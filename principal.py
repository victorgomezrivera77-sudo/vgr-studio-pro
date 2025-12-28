<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OASIS | Sistema de Microanálisis</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&family=Playfair+Display:ital@1&display=swap" rel="stylesheet">
    
    <style>
        /* ESTÉTICA OASIS - CURADURÍA VISUAL */
        :root {
            --oasis-bg: #ffffff;
            --oasis-ink: #0a0a0a;
            --oasis-gold: #d4af37;
            --oasis-soft: #f9f9f9;
        }

        body, html {
            margin: 0; padding: 0; width: 100%; height: 100%;
            background-color: var(--oasis-bg); font-family: 'Inter', sans-serif;
            display: flex; align-items: center; justify-content: center; overflow: hidden;
        }

        .background-aura {
            position: absolute; width: 100%; height: 100%;
            background: radial-gradient(circle at 50% 50%, #ffffff 0%, #f4f4f4 100%);
            z-index: -1;
        }

        .main-title { text-align: center; z-index: 1; }
        .main-title h1 {
            font-family: 'Playfair Display', serif; font-size: 3.5rem; 
            font-weight: 200; font-style: italic; margin: 0;
        }
        .main-title p { letter-spacing: 5px; text-transform: uppercase; color: #999; font-size: 0.7rem; }

        /* INTERFAZ DE CHAT REVOLUCIONADA */
        #oasis-launcher {
            position: fixed; bottom: 40px; right: 40px;
            width: 75px; height: 75px; border-radius: 50%;
            background: var(--oasis-ink); color: white; border: none;
            cursor: pointer; font-size: 30px; z-index: 1000;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            transition: 0.5s cubic-bezier(0.19, 1, 0.22, 1);
        }

        #oasis-launcher:hover { transform: scale(1.1) rotate(90deg); }

        #oasis-window {
            position: fixed; bottom: 130px; right: 40px;
            width: 420px; height: 650px; background: white;
            border-radius: 35px; display: none; flex-direction: column;
            box-shadow: 0 30px 100px rgba(0,0,0,0.18);
            border: 1px solid rgba(0,0,0,0.04); overflow: hidden; z-index: 1000;
        }

        #oasis-header {
            padding: 35px; background: var(--oasis-ink); color: white;
            text-align: center; font-size: 0.8rem; letter-spacing: 4px;
        }

        #oasis-feed {
            flex: 1; padding: 30px; overflow-y: auto; background: var(--oasis-soft);
            display: flex; flex-direction: column; gap: 25px;
        }

        .bubble {
            max-width: 85%; padding: 18px 22px; border-radius: 22px;
            font-size: 14px; line-height: 1.6; animation: fadeIn 0.6s ease;
        }

        .bot { background: white; border: 1px solid #eee; color: #222; align-self: flex-start; }
        .log { font-style: italic; color: #aaa; font-size: 11px; text-align: center; width: 100%; }

        #oasis-footer { padding: 30px; background: white; display: flex; flex-direction: column; gap: 15px; }

        .btn-action {
            width: 100%; padding: 18px; border-radius: 18px; border: 1px solid #eee;
            background: white; cursor: pointer; font-weight: 600; font-size: 12px;
            letter-spacing: 1px; transition: 0.3s; text-transform: uppercase;
        }

        .btn-action.primary { background: var(--oasis-ink); color: white; border: none; }
        .btn-action:hover { background: #f0f0f0; transform: translateY(-2px); }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>

    <div class="background-aura"></div>
    <div class="main-title">
        <h1>Oasis</h1>
        <p>Microanálisis & Curaduría</p>
    </div>

    <div id="oasis-chat-container">
        <button id="oasis-launcher" onclick="toggleOasis()">✧</button>
        
        <div id="oasis-window">
            <div id="oasis-header">SISTEMA DE PRECISIÓN</div>
            <div id="oasis-feed">
                <div class="bubble bot">
                    Hola. Si tienes una <strong>IMAGEN</strong>, puedes calcular tu presupuesto. El sistema determinará automáticamente el estilo y la complejidad de tu diseño.
                </div>
            </div>
            <div id="oasis-footer">
                <input type="file" id="imageInput" hidden accept="image/*" onchange="runCerebro(event)">
                <button class="btn-action primary" onclick="document.getElementById('imageInput').click()">📸 SUBIR DISEÑO</button>
                <button class="btn-action">💬 CONSULTA TÉCNICA</button>
            </div>
        </div>
    </div>

    <script>
        // --- MOTOR DE GALERÍAS Y CEREBROS ---
        const GALERIAS = {
            "FINE_LINE": { base: 15, modo: "pulgada", ocupacion: "ALTA" },
            "LETTERING": { base: 12, modo: "pulgada", ocupacion: "ALTA" },
            "REALISMO_BG": { base: 150, modo: "sesion", ocupacion: "ALTA" },
            "TRADICIONAL": { base: 100, modo: "fijo", ocupacion: "ALTA" },
            "NEOTRADICIONAL": { base: 130, modo: "sesion", ocupacion: "ALTA" },
            "REALISMO_COLOR": { base: 180, modo: "sesion", ocupacion: "MEDIA" },
            "BLACKWORK": { base: 120, modo: "complejidad", ocupacion: "MEDIA" },
            "JAPONES": { base: 160, modo: "sesion", ocupacion: "MEDIA" },
            "BIOMECANICO": { base: 180, modo: "sesion", ocupacion: "BAJA" },
            "TRASH_POLKA": { base: 140, modo: "fijo", ocupacion: "BAJA" }
        };

        function toggleOasis() {
            const win = document.getElementById('oasis-window');
            win.style.display = (win.style.display === 'flex') ? 'none' : 'flex';
        }

        function addMessage(text, type = 'bot') {
            const feed = document.getElementById('oasis-feed');
            const msg = document.createElement('div');
            msg.className = `bubble ${type}`;
            msg.innerHTML = text;
            feed.appendChild(msg);
            feed.scrollTop = feed.scrollHeight;
        }

        function runCerebro(event) {
            const file = event.target.files[0];
            if(!file) return;

            // 1. EL SUPERVISOR ACTÚA
            addMessage("<em>SUPERVISOR: Limpiando ruido y validando microanálisis visual...</em>", "log");

            setTimeout(() => {
                // 2. EL DIRECTOR Y ANALISTA (Simulación de detección)
                const estilo = "FINE_LINE"; // Simulado
                const complejidad = "ALTA"; // Simulado
                const color = false;

                addMessage(`<strong>DIRECTOR:</strong> Detectado estilo ${estilo}.<br><strong>ANALISTA:</strong> Complejidad ${complejidad} confirmada.`);

                // 3. EL OBRERO DE COLOR Y ANALISTA FINANCIERO
                setTimeout(() => {
                    const data = GALERIAS[estilo];
                    let total = data.base;
                    if(complejidad === "ALTA") total *= 1.30;
                    if(color) total *= 1.20;

                    addMessage(`<strong>ANÁLISIS FINAL:</strong><br>Categoría de ocupación ${data.ocupacion}.<br>Cálculo basado en ${data.modo}: <strong>$${total.toFixed(2)}</strong>.`, "bot");
                    
                    const btn = document.createElement('button');
                    btn.className = "btn-action primary";
                    btn.style.marginTop = "15px";
                    btn.innerText = "📅 AGENDAR EN OASIS";
                    btn.onclick = () => window.open('https://wa.me/Oasis-writer', '_blank');
                    document.getElementById('oasis-feed').appendChild(btn);
                }, 1500);

            }, 2500);
        }
    </script>
</body>
</html>
