# Propuesta Integral de Tools para el Agente Gerente de Operaciones

Esta propuesta enumera todas las tools recomendadas para maximizar la utilidad y cobertura del agente en la gestión de operaciones, flota, reservas, clientes y pagos. Cada tool está pensada para exponer funciones críticas, minimizar alucinaciones y permitir automatización realista.

---

## 1. Gestión de Vehículos
- **consulta_estado_vehiculo(patente: str) -> str**
  - Consulta ficha técnica, estado y vencimientos de un vehículo.
- **vehiculos_disponibles(fecha_inicio: str, fecha_fin: str) -> str**
  - Lista vehículos sin reservas activas en el rango de fechas.
- **listar_vehiculos() -> str**
  - Devuelve la lista completa de vehículos registrados.
- **historial_vehiculo(patente: str) -> str**
  - Devuelve el historial de reservas, mantenimientos y eventos del vehículo.

## 2. Gestión de Reservas
- **registrar_reserva(id_vehiculo: int, id_cliente: int, fecha_reserva: str, fecha_devolucion: str, motivo: str) -> str**
  - Registra una nueva reserva validando solapamientos.
- **consultar_reservas_vehiculo(id_vehiculo: int) -> str**
  - Lista todas las reservas de un vehículo.
- **consultar_reservas_cliente(id_cliente: int) -> str**
  - Lista todas las reservas hechas por un cliente.
- **cancelar_reserva(id_reserva: int) -> str**
  - Cancela una reserva activa.

## 3. Gestión de Clientes
- **consultar_cliente(id_cliente: int) -> str**
  - Devuelve información de contacto y estado del cliente.
- **listar_clientes() -> str**
  - Lista todos los clientes registrados.
- **historial_cliente(id_cliente: int) -> str**
  - Devuelve historial de reservas, pagos y eventos del cliente.

## 4. Pagos y Facturación
- **consultar_pagos_cliente(id_cliente: int) -> str**
  - Estado de pagos, deudas y pagos realizados por un cliente.
- **registrar_pago(id_cliente: int, monto: float, fecha: str, metodo: str) -> str**
  - Registra un pago manualmente.
- **listar_pagos_pendientes() -> str**
  - Lista todos los pagos pendientes de la operación.

## 5. Documentos y Vencimientos
- **alertar_vencimientos(patente: str = None, dias_alerta: int = None) -> str**
  - Alerta sobre vencimientos de SOAP o revisión técnica en los próximos días.
- **listar_vencimientos_proximos(dias: int) -> str**
  - Lista todos los vehículos con vencimientos en los próximos X días.

## 6. Comunicación y Notificaciones
- **enviar_notificacion(destinatario: str, mensaje: str) -> str**
  - Envía una notificación por WhatsApp, SMS o email.
- **enviar_recordatorio_vencimiento(patente: str, medio: str) -> str**
  - Envía recordatorio automático de vencimiento a responsable.

## 7. Reportes y Analítica
- **generar_reporte_utilizacion(fecha_inicio: str, fecha_fin: str) -> str**
  - Reporte de utilización de flota en un rango de fechas.
- **reporte_ingresos(fecha_inicio: str, fecha_fin: str) -> str**
  - Reporte de ingresos por reservas y pagos.

## 8. Seguridad y Auditoría
- **auditar_eventos(tipo_evento: str = None, fecha_inicio: str = None, fecha_fin: str = None) -> str**
  - Devuelve registro de acciones críticas, cambios y accesos.

---

**Notas:**
- Todas las tools deben tener tipado explícito y docstring estándar.
- Se recomienda implementar primero las tools más consultadas (vehículos, reservas, pagos, vencimientos).
- El agente debe exponer solo las tools que tengan lógica y datos reales detrás para evitar alucinaciones.
- Se pueden agregar tools adicionales según las necesidades futuras del negocio.

---

**Fin de la propuesta.**
