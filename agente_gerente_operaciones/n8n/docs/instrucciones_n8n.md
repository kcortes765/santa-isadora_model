# Instrucciones para flujos n8n

Esta carpeta contiene los flujos visuales exportados desde n8n para la integración con el agente Python.

## ¿Cómo usar?
1. Importa los archivos JSON de la carpeta `n8n/workflows` en tu instancia de n8n.
2. Configura los disparadores (ejemplo: Webhook, WhatsApp, Email) según tus credenciales y entorno.
3. Ajusta los nodos HTTP para apuntar a la URL del agente Python (por ejemplo, http://localhost:8000/consulta).
4. Personaliza los flujos según los procesos de tu operación.

## Ejemplos incluidos
- `whatsapp_to_agente.json`: Recibe mensajes de WhatsApp y consulta al agente Python.
- `alerta_vencimiento.json`: Flujo de alerta automática de vencimientos.
- `reporte_pago.json`: Envío automático de reportes de pago.

## Buenas prácticas
- Documenta cada flujo y su propósito.
- Usa nodos de log para registrar eventos importantes.
- Mantén los endpoints del agente Python protegidos y autenticados si es necesario.
