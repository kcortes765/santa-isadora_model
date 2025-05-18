# Agente Gerente de Operaciones

**Enfoque principal: Rental y contratos.** El sistema está optimizado para la gestión de arriendo y subarriendo de vehículos, contratos y disponibilidad, con transporte de personal como área secundaria y de bajo volumen.

**Integración nativa con OpenAI Agents SDK:** Todas las herramientas están diseñadas y registradas como "tools" para agentes LLM, permitiendo automatización conversacional, integración multi-canal y orquestación inteligente.

**Canales recomendados:**
- WhatsApp: canal principal para clientes y notificaciones simples.
- Telegram: canal avanzado para operadores, mecánicos y como "segundo cerebro" para gestión interna, con soporte de menús y comandos.

**Automatización de mantenciones y soporte a decisiones:** El sistema prioriza alertas de vencimientos, derivación de problemas y registro de mantenciones, sirviendo como "segundo cerebro" para José Magaña y el equipo técnico.

**Traspaso a IA sucesora:**
- Todas las tools están documentadas y testeadas.
- El backend es modular y extensible.
- Se recomienda leer este README, los archivos de log, plan y punto de control, y los ejemplos de uso para onboarding de agentes IA.

## Arquitectura
- **n8n**: Orquestador visual de workflows, integración con WhatsApp, email, webhooks, etc.
- **Python (OpenAI Agents SDK)**: Inteligencia, lógica de negocio, validaciones, consulta y procesamiento de datos.

## Estructura de carpetas

```
agente_gerente_operaciones/
├── README.md
├── requirements.txt
├── config/
│   └── settings.yaml
├── core/
│   ├── agente_gerente.py
│   ├── tools_vehiculos.py
│   ├── tools_documentos.py
│   ├── tools_comunicacion.py
│   ├── tools_pagos.py
│   └── utils.py
├── workflows/
│   ├── flujo_alertas.py
│   ├── flujo_derivacion.py
│   └── flujo_reportes.py
├── data/
│   ├── ejemplo_vehiculos.xlsx
│   ├── ejemplo_reservas.xlsx
│   └── logs/
│       └── agente.log
├── tests/
│   ├── test_agente.py
│   └── test_tools.py
├── scripts/
│   └── run_agente.py
└── n8n/
    ├── workflows/
    │   ├── whatsapp_to_agente.json
    │   ├── alerta_vencimiento.json
    │   └── reporte_pago.json
    └── docs/
        └── instrucciones_n8n.md
```

## Flujo de ejemplo (WhatsApp + n8n + agente Python)
1. WhatsApp → n8n recibe mensaje.
2. n8n llama a la API REST del agente Python con el mensaje.
3. El agente procesa y responde.
4. n8n envía la respuesta por WhatsApp y registra el evento.

## Ventajas
- Permite automatizaciones visuales y lógica avanzada personalizada.
- Usuarios no técnicos pueden crear/modificar flujos en n8n.
- El agente Python mantiene la lógica de negocio y validaciones complejas.

## Próximos pasos
- Completar archivos base y plantillas.
- Definir los primeros flujos híbridos (ejemplo: alerta de vencimiento, consulta de estado, derivación de problemas).
- Integrar canales (WhatsApp, email) y asegurar trazabilidad de cada acción.

---

## Documentación de usuario y ejemplos de uso

### Ejecución de tests

Para validar el correcto funcionamiento de todas las herramientas, ejecuta:

```bash
pytest tests/test_tools.py
```

### Ejemplos de uso de las tools principales

#### Vehículos y documentación
```python
from agente_gerente_operaciones.core import tools_vehiculos, tools_documentos

print(tools_vehiculos.consulta_estado_vehiculo('XY1012'))
print(tools_documentos.alertar_vencimientos('XY1012', 15))
print(tools_documentos.listar_documentos_faltantes_o_vencidos())
```

#### Reservas
```python
from agente_gerente_operaciones.core import tools_reservas

print(tools_reservas.registrar_reserva(1, 2, '2025-05-20', '2025-05-25', 'Renta por faena'))
print(tools_reservas.vehiculos_disponibles('2025-05-20', '2025-05-25'))
print(tools_reservas.consultar_reservas_vehiculo(1))
print(tools_reservas.cancelar_reserva(5))
```

#### Pagos y reportes
```python
from agente_gerente_operaciones.core import tools_pagos

print(tools_pagos.consultar_pagos_cliente(2))
print(tools_pagos.listar_pagos_pendientes())
print(tools_pagos.generar_reporte_utilizacion('2025-05-01', '2025-05-31'))
print(tools_pagos.reporte_ingresos('2025-05-01', '2025-05-31'))
```

#### Comunicación y derivación
```python
from agente_gerente_operaciones.core import tools_comunicacion

print(tools_comunicacion.enviar_notificacion('Recordatorio de pago', 'usuario@email.com'))
print(tools_comunicacion.enviar_recordatorio_vencimiento('XY1012', '+56912345678'))
print(tools_comunicacion.derivar_problema_mecanico('XY1012', 'No parte', 'mecanico@email.com'))
```

### Integración con n8n y flujos externos

El agente está preparado para integrarse vía API REST con n8n y otros orquestadores. Consulta la carpeta `n8n/workflows/` para ejemplos de integración visual y disparadores automáticos.
