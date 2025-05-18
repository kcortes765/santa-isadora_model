# tools.py
# Herramientas mock para agentes

def consulta_disponibilidad(tipo_maquinaria: str) -> dict:
    # Mock: siempre hay disponibilidad de 3 unidades
    return {
        "tipo_maquinaria": tipo_maquinaria,
        "disponible": 3,
        "mensaje": f"Hay 3 unidades de {tipo_maquinaria} disponibles."
    }