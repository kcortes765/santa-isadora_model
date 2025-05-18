# plan.md

## Naturaleza y Propósito
Automatizar y digitalizar la operación interna de una pyme de transporte y arriendo de maquinaria (ejemplo: Santa Isadora), resolviendo dolores reales del equipo administrativo y de operaciones, priorizando simplicidad, usabilidad y registro.

## Dolor y Necesidad
- Pérdida de tiempo por registros manuales.
- Información dispersa (WhatsApp, correo, planillas).
- Errores en pagos, reservas, reportes y coordinación diaria.
- Falta de trazabilidad y control.

## Usuario Interno
- Gerente de operaciones (prioridad inicial), encargado de rutas, asignaciones y control diario.
- Equipo administrativo reducido (2–4 personas).

## Objetivos Técnicos
- Centralizar y automatizar reservas, seguimiento, reportes y pagos.
- Integrar con WhatsApp/correo, pero sin reemplazar rutinas actuales de golpe.
- Registrar y auditar cada acción y mejora.
- Simplicidad y adopción inmediata.

## Criterios de Éxito
- ¿El equipo siente que su día es más fácil y controlado?
- ¿Se reducen los errores y el tiempo perdido?
- ¿Todo queda registrado y es fácil de auditar?

## Agentes Iniciales Propuestos
1. **Agente de Operaciones (prioridad):**
   - Consulta y asignación rápida de vehículos/equipos.
   - Registro simple de reservas y cambios.
   - Seguimiento de servicios en curso/pasados.

## Integración de n8n + Agente Python

### Arquitectura Propuesta (Actualizada)
- **Agente Python (OpenAI Agents SDK):** Toda la lógica, automatización, validaciones y flujos principales estarán aquí. El agente centraliza la inteligencia y la toma de decisiones.
- **n8n:** Solo funcionará como puente/orquestador para conectar el agente Python con herramientas externas (WhatsApp, email, SMS, APIs de terceros, etc). No contendrá lógica de negocio, solo disparadores y reenvío de datos.
- **Ventajas:**
  - El código crítico es auditable, versionado y controlado en Python.
  - n8n facilita la integración y despliegue rápido de conectores externos, sin duplicar lógica.
  - Mayor robustez, trazabilidad y flexibilidad para evolucionar el sistema.

## Plantilla de Vehículos/Equipos

**Objetivo:** Tener un inventario completo y actualizado de todos los vehículos y equipos, propios y subcontratados, incluyendo control documental obligatorio según normativa chilena.

### Ejemplo de Inventario de Vehículos/Equipos

**Tabla 1: Datos Principales**

| id  | tipo      | marca    | modelo   | año  | patente   | estado        | chofer_asignado | fecha_ultimo_servicio | km_actual |
|-----|-----------|----------|----------|------|-----------|---------------|------------------|----------------------|-----------|
| 1   | Camioneta | Toyota   | Hilux    | 2022 | XX-1234   | Disponible    | Juan Pérez       | 2025-03-10           | 45.000    |
| 2   | Camión    | Mercedes | Actros   | 2020 | YY-5678   | En mantención | Pedro Soto       | 2025-02-15           | 120.000   |

**Tabla 2: Control Documental y Observaciones**

| id  | permiso_circulacion_venc | revision_tecnica_venc | soap_venc   | decreto_60_venc | mantencion_venc | observaciones   | proveedor (si es externo) | fecha_alta  | fecha_baja  |
|-----|--------------------------|----------------------|-------------|-----------------|-----------------|----------------|--------------------------|-------------|-------------|
| 1   | 2026-03-10               | 2025-09-10           | 2025-03-10  | 2025-12-10      | 2025-09-10      | Sin novedades  | -                        | 2022-01-01  | -           |
| 2   | 2025-05-15               | 2025-08-15           | 2025-05-15  | 2025-11-15      | 2025-08-15      | Falla motor     | Proveed. Externo S.A.    | 2020-05-01  | -           |

**Guía de Campos:**
- **id:** Identificador único (correlativo o patente).
- **tipo:** Ejemplo: Camioneta, Camión pluma, etc.
- **estado:** Disponible, reservado, en mantención, fuera de servicio, etc.
- **chofer_asignado:** Nombre del conductor habitual.
- **km_actual:** Kilometraje actual.
- **permiso_circulacion_venc, revision_tecnica_venc, etc.:** Fechas de vencimiento de documentos obligatorios.
- **proveedor:** Solo si es equipo externo.
- **fecha_alta/baja:** Alta o baja en el inventario.

> Si la tabla es muy ancha, divídela en dos o más secciones y usa ejemplos para facilitar la lectura.

- **id:** Identificador único (puede ser correlativo o la patente).
- **tipo:** Camioneta, camión pluma, etc.
- **marca/modelo/año:** Detalles técnicos.
- **patente:** Placa patente.
- **estado:** Disponible, reservado, en mantención, fuera de servicio, etc.
- **chofer_asignado:** Nombre del conductor habitual.
- **fecha_ultimo_servicio/km_actual:** Control de mantenciones.
- **permiso_circulacion_venc:** Fecha de vencimiento del permiso de circulación.
- **revision_tecnica_venc:** Fecha de vencimiento de la revisión técnica.
- **soap_venc:** Fecha de vencimiento del seguro obligatorio.
- **decreto_60_venc:** Fecha de vencimiento/cumplimiento de requisitos del Decreto 60.
- **mantencion_venc:** Fecha sugerida de próxima mantención.
- **proveedor:** Si es subcontratado.
- **fecha_alta/fecha_baja:** Para historial.
- **observaciones:** Cualquier detalle relevante.

## Tareas Pendientes (Backlog LLM + Agents SDK)
1. Integrar LLM y Agents SDK: definir agente, instrucciones y configuración.
2. Implementar tools Python para acceso y operación sobre Excel (vehículos, reservas, clientes, pagos).
3. Crear simulador de interacción por consola (imitando WhatsApp) conectado al agente LLM real.
4. Exponer el agente como API REST (FastAPI) para futura conexión con n8n.
5. Validar y testear los flujos principales y herramientas.
6. Documentar configuración, ejemplos y uso.
7. Dejar listo el endpoint para n8n (puente externo).

### Avance / Alcance Actual
- Arquitectura definida: agente Python centraliza lógica, n8n solo puente externo.
- Archivos Excel simulados generados y validados.
- Script de carga de datos corregido y funcional.
- Documentación y estructura base listas para desarrollo modular.
- Próximo foco: integración real del agente LLM y tools, simulador de chat por consola.

### Notas
- Toda modificación relevante será registrada en log.md y, si corresponde, en este plan.
- Revisión periódica de prioridades y tareas según feedback y avances.
- Siempre priorizar el dolor real, la simplicidad y el feedback del usuario interno.

## Ciclo Windsurf AI
- Cada avance se registra en `log.md`.
- Checkpoint en `punto_de_control.md` al cerrar cada iteración relevante.
