# Plan de Generación de Tools — Fases y Prioridades (alineado a reunión José Magaña)

## Objetivo
Desarrollar las tools del agente siguiendo fases priorizadas según los dolores, tareas repetitivas y expectativas de José Magaña, asegurando impacto inmediato y alineación con la operación real.

---

## **Fase 1: Automatización de Información Crítica y Alertas**
- **Tools:**
  - consulta_estado_vehiculo
  - alertar_vencimientos (SOAP, revisión técnica, permisos)
  - listar_documentos_faltantes o vencidos
- **Motivación:** Reducir fallos por vencimientos, evitar problemas por falta de información clave.
- **Resultado esperado:** El usuario recibe alertas y puede consultar el estado documental y técnico de cualquier vehículo en segundos.

## **Fase 2: Gestión de Reservas, Disponibilidad y Uso**
- **Tools:**
  - registrar_reserva
  - vehiculos_disponibles (por fechas)
  - consultar_reservas_vehiculo / cliente
  - cancelar_reserva
- **Motivación:** Eliminar solapamientos, responder rápido a solicitudes, automatizar asignación y liberar tiempo en la gestión manual.
- **Resultado esperado:** Reservas y disponibilidades claras, sin errores manuales.

## **Fase 3: Pagos, Servicios y Reportes Automáticos**
- **Tools:**
  - consultar_pagos_cliente
  - listar_pagos_pendientes
  - generar_reporte_utilizacion
  - reporte_ingresos
- **Motivación:** Control de ingresos, servicios y pagos; reportes automáticos para auditoría y gestión financiera.
- **Resultado esperado:** Visibilidad total de pagos y servicios, reportes listos para inspección o gestión.

## **Fase 4: Comunicación y Derivación Automática**
- **Tools:**
  - enviar_notificacion (WhatsApp, email, SMS)
  - enviar_recordatorio_vencimiento
  - derivar_problema_mecanico (según gravedad)
- **Motivación:** Automatizar respuestas a clientes/proveedores, derivar problemas críticos sin intervención manual.
- **Resultado esperado:** Respuestas rápidas y derivación automática según reglas de negocio.

## **Fase 5: Análisis Avanzado, Auditoría y Evolución Dinámica**
- **Tools:**
  - top_clientes_por_ingresos
  - historial_vehiculo/cliente
  - auditar_eventos
  - meta-tools: crear/modificar tools
- **Motivación:** Análisis de datos, mejora continua, adaptación a nuevas necesidades.
- **Resultado esperado:** El agente evoluciona, genera nuevos análisis y se adapta a la operación.

---

## **Notas de implementación**
- Cada fase puede tener entregas parciales y debe ser validada con el usuario antes de avanzar.
- Priorizar siempre los dolores y tareas repetitivas identificadas en la reunión/preparación.
- Registrar avances y cambios en log.md y actualizar plan.md ante hitos o desvíos.

---

**Fin del plan por fases.**
