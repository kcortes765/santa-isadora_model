# core.py
# Clases base y utilidades comunes para agentes IA

class AgentBase:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def run(self, *args, **kwargs):
        raise NotImplementedError
