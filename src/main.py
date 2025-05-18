# main.py
from fastapi import FastAPI
from agents.agents_config import AgenteDisponibilidad

app = FastAPI()
agente = AgenteDisponibilidad()

@app.get("/disponibilidad")
def disponibilidad(tipo_maquinaria: str):
    """Endpoint HTTP para consultar disponibilidad de maquinaria"""
    return agente.run(tipo_maquinaria)
