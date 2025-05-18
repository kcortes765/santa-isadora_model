import os
import yaml
from agents import Agent, function_tool
from agente_gerente_operaciones.core.tools_vehiculos import consulta_estado_vehiculo
from agente_gerente_operaciones.core.tools_reservas import registrar_reserva, vehiculos_disponibles, consultar_reservas_vehiculo, cancelar_reserva
from agente_gerente_operaciones.core.tools_pagos import consultar_pagos_cliente, listar_pagos_pendientes, generar_reporte_utilizacion, reporte_ingresos
from agente_gerente_operaciones.core.tools_comunicacion import enviar_whatsapp, enviar_notificacion, enviar_recordatorio_vencimiento, derivar_problema_mecanico
from agente_gerente_operaciones.core.tools_documentos import alertar_vencimientos, listar_documentos_faltantes_o_vencidos

SETTINGS_PATH = "C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/config/settings.yaml"
openai_api_key = None
if os.path.exists(SETTINGS_PATH):
    with open(SETTINGS_PATH, 'r', encoding='utf-8') as f:
        settings = yaml.safe_load(f)
        openai_api_key = settings.get('openai_api_key')
if not openai_api_key:
    openai_api_key = os.environ.get('OPENAI_API_KEY')

# Decorar las tools para exponerlas al agente
consulta_estado_vehiculo_tool = function_tool(consulta_estado_vehiculo)
registrar_reserva_tool = function_tool(registrar_reserva)
vehiculos_disponibles_tool = function_tool(vehiculos_disponibles)
consultar_reservas_vehiculo_tool = function_tool(consultar_reservas_vehiculo)
cancelar_reserva_tool = function_tool(cancelar_reserva)
consultar_pagos_cliente_tool = function_tool(consultar_pagos_cliente)
listar_pagos_pendientes_tool = function_tool(listar_pagos_pendientes)
generar_reporte_utilizacion_tool = function_tool(generar_reporte_utilizacion)
reporte_ingresos_tool = function_tool(reporte_ingresos)
alertar_vencimientos_tool = function_tool(alertar_vencimientos)
listar_documentos_faltantes_o_vencidos_tool = function_tool(listar_documentos_faltantes_o_vencidos)
enviar_notificacion_tool = function_tool(enviar_notificacion)
enviar_recordatorio_vencimiento_tool = function_tool(enviar_recordatorio_vencimiento)
derivar_problema_mecanico_tool = function_tool(derivar_problema_mecanico)

tools = [
    consulta_estado_vehiculo_tool,
    registrar_reserva_tool,
    vehiculos_disponibles_tool,
    consultar_reservas_vehiculo_tool,
    cancelar_reserva_tool,
    consultar_pagos_cliente_tool,
    listar_pagos_pendientes_tool,
    generar_reporte_utilizacion_tool,
    reporte_ingresos_tool,
    alertar_vencimientos_tool,
    listar_documentos_faltantes_o_vencidos_tool,
    enviar_notificacion_tool,
    enviar_recordatorio_vencimiento_tool,
    derivar_problema_mecanico_tool,
]

agente = Agent(
    name="GerenteOperaciones",
    instructions="Eres un asistente experto en gestión de operaciones, control documental y automatización para flotas y maquinaria. Siempre pide confirmación antes de ejecutar acciones críticas. Responde en español. Utiliza las herramientas disponibles para consultar, registrar y alertar sobre vehículos, reservas, clientes y pagos.",
    tools=tools,
    model="gpt-4.1-mini-2025-04-14"
)
