# Santa Isadora Model

## Visión y Propósito
Sistema inteligente para la gestión de flota, reservas y operaciones en empresas de transporte y arriendo de maquinaria. Automatiza tareas críticas, anticipa problemas y centraliza la información, integrando canales como WhatsApp, email y llamadas para máxima eficiencia.

---

## Características Destacadas
- **Alertas inteligentes** de vencimientos y mantenciones (con derivación automática a encargados, previa aprobación).
- **Gestión centralizada de reservas y disponibilidad** de vehículos y equipos.
- **Respuestas automáticas** a consultas frecuentes por WhatsApp o consola.
- **Reportes automáticos** de estados de pago, servicios y operaciones.
- **Control total y aprobación previa** de todas las acciones automáticas por parte del encargado.
- **Historial y trazabilidad** de todas las acciones y comunicaciones.

---

## Puntos de Dolor Resueltos
- Eliminación de la gestión manual de vencimientos y mantenciones.
- Centralización de documentos y datos críticos.
- Respuesta automática a requerimientos repetitivos.
- Reducción de errores por desorden o falta de información.
- Reportes y auditorías automáticas para pagos y servicios.

---

## Uso Rápido
1. Instala dependencias: `pip install -r requirements.txt`
2. Carga datos de ejemplo: `python src/scripts/cargar_ejemplo_datos.py`
3. Ejecuta el agente: `python src/scripts/agente_operaciones.py`

---

## Ejemplo de Flujo Inteligente
- El agente alerta sobre vencimientos próximos y sugiere acciones.
- Permite reservar vehículos y asignar choferes en segundos.
- Deriva automáticamente problemas al especialista correcto.
- Genera reportes mensuales de pagos y servicios.
- Todas las acciones requieren aprobación previa del encargado.

---

## Arquitectura
- **Scripts:** Automatización y carga de datos.
- **Agente:** Interfaz interactiva y lógica de negocio.
- **Integración futura:** WhatsApp, email, dashboards y agentes SDK inteligentes.

---

## Impresiona con...
- Alertas y derivación automática con control total.
- Respuestas inmediatas a consultas repetitivas.
- Reportes y auditoría en un clic.
- Preparado para escalar a IA conversacional y agentes inteligentes.

Proyecto de automatización y asistencia IA para transporte y arriendo de maquinaria.

## Estructura del repositorio
- `plan.md`: Objetivo, alcance y tareas actuales.
- `log.md`: Bitácora técnica.
- `punto_de_control.md`: Checkpoints.
- `src/`: Código fuente principal.
- `docs/`: Documentación técnica y funcional.

## Primer agente
El agente de disponibilidad responde consultas sobre disponibilidad de maquinaria vía endpoint HTTP (`/disponibilidad`).
