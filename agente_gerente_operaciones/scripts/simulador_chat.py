import sys
from agents import Runner
from agente_gerente_operaciones.core.agente_gerente import agente

print("Simulador de chat tipo WhatsApp (consola). Escribe 'salir' para terminar.")

while True:
    entrada = input("Tú: ")
    if entrada.lower() in ("salir", "exit", "quit"): 
        print("Fin del chat.")
        break
    resultado = Runner.run_sync(agente, entrada)
    print(f"Agente: {getattr(resultado, 'final_output', resultado)}")
