import datetime

class OasisBot:
    def __init__(self, artist_name="Víctor"):
        self.artist_name = artist_name
        self.base_rate = 150  # Tarifa base por hora (ejemplo)
        
    def analizar_solicitud(self, cliente, idea, zona, tamano_cm):
        """
        Esta función actúa como tu filtro de 'Resolución Rápida'.
        Analiza la complejidad y te da una estimación automática.
        """
        
        # 1. Determinación de Complejidad (Simulada)
        complejidad = "Media"
        factor_tiempo = 1.0
        
        keywords_complejas = ["cobertura", "cover up", "realismo", "manga", "espalda", "bio"]
        keywords_rapidas = ["flash", "letras", "linea", "minimalista", "simbolo"]

        if any(word in idea.lower() for word in keywords_complejas):
            complejidad = "Alta (Requiere Diseño Custom)"
            factor_tiempo = 2.5
        elif any(word in idea.lower() for word in keywords_rapidas):
            complejidad = "Baja (Flash / Fast Design)"
            factor_tiempo = 0.5

        # 2. Calculo de Tiempo Estimado (Horas)
        # Formula simple: (Tamaño / 10) * Factor Complejidad
        tiempo_estimado = (tamano_cm / 10) * factor_tiempo
        if tiempo_estimado < 1: tiempo_estimado = 1 # Mínimo 1 hora

        # 3. Generar Cotización Preliminar
        precio_estimado = tiempo_estimado * self.base_rate

        return {
            "estado": "✅ Solicitud Procesada",
            "cliente": cliente,
            "analisis_ia": f"Detecté una complejidad {complejidad}.",
            "tiempo_sugerido": f"{round(tiempo_estimado, 1)} horas",
            "cotizacion_minima": f"${round(precio_estimado)} USD",
            "accion_sugerida": "Agendar Consultoría" if complejidad.startswith("Alta") else "Agendar Directo"
        }

# --- SIMULACIÓN DE USO (Lo que verás en tu consola) ---

bot = OasisBot()

# Caso 1: Cliente con idea compleja (Tu especialidad)
solicitud_compleja = bot.analizar_solicitud(
    cliente="Lauren",
    idea="Quiero tapar una cicatriz con un diseño biomecánico y neotribal",
    zona="Antebrazo",
    tamano_cm=20
)

# Caso 2: Cliente con idea rápida (Fast Cash)
solicitud_rapida = bot.analizar_solicitud(
    cliente="Cliente Nuevo",
    idea="Unas letras góticas pequeñas",
    zona="Muñeca",
    tamano_cm=8
)

print(f"--- REPORTE DE OASIS BOT PARA {bot.artist_name.upper()} ---")
print(solicitud_compleja)
print("\n")
print(solicitud_rapida)
