# agents_config.py
from .core import AgentBase
from .tools import consulta_disponibilidad

class AgenteDisponibilidad(AgentBase):
    def __init__(self):
        super().__init__(
            name="Agente de Disponibilidad",
            description="Responde consultas sobre disponibilidad de maquinaria."
        )

    def run(self, tipo_maquinaria: str):
        return consulta_disponibilidad(tipo_maquinaria)
