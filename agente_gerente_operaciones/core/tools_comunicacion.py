# Herramientas de comunicación (WhatsApp, email)

def enviar_whatsapp(mensaje, destinatario):
    """
    Envía un mensaje de WhatsApp usando Twilio.
    Args:
        mensaje (str): Texto a enviar.
        destinatario (str): Número en formato internacional.
    Returns:
        str: Confirmación simulada.
    Ejemplo:
        >>> enviar_whatsapp('Hola', '+56912345678')
        'Mensaje enviado a +56912345678: Hola'
    """
    # TODO: Implementar integración real
    return f"Mensaje enviado a {destinatario}: {mensaje}"


def enviar_notificacion(mensaje: str, destinatario: str) -> str:
    """
    Envía una notificación genérica (simulada) por WhatsApp o email.
    Args:
        mensaje (str): Texto a enviar.
        destinatario (str): Contacto (email o número).
    Returns:
        str: Confirmación simulada.
    Ejemplo:
        >>> enviar_notificacion('Recordatorio de pago', 'usuario@email.com')
        'Notificación enviada a usuario@email.com: Recordatorio de pago'
    """
    # Aquí se podría integrar con otros canales
    return f"Notificación enviada a {destinatario}: {mensaje}"


def enviar_recordatorio_vencimiento(patente: str, destinatario: str) -> str:
    """
    Envía un recordatorio de vencimiento de documentos de un vehículo.
    Args:
        patente (str): Patente del vehículo.
        destinatario (str): Contacto del responsable.
    Returns:
        str: Mensaje de confirmación simulada.
    Ejemplo:
        >>> enviar_recordatorio_vencimiento('XY1012', '+56912345678')
        'Recordatorio enviado a +56912345678: Patente XY1012 - SOAP por vencer en 5 días (2025-05-21)'
    """
    from agente_gerente_operaciones.core.tools_documentos import alertar_vencimientos
    alerta = alertar_vencimientos(patente, dias_alerta=10)
    if 'No hay vencimientos' in alerta:
        return f"No hay vencimientos próximos para {patente}."
    # Aquí se simula el envío
    return f"Recordatorio enviado a {destinatario}: {alerta}"


def derivar_problema_mecanico(patente: str, descripcion: str, responsable: str) -> str:
    """
    Deriva (simulado) un problema mecánico a mantenimiento.
    Args:
        patente (str): Patente del vehículo.
        descripcion (str): Descripción del problema.
        responsable (str): Contacto a notificar.
    Returns:
        str: Confirmación de derivación simulada.
    Ejemplo:
        >>> derivar_problema_mecanico('XY1012', 'No parte', 'mecanico@email.com')
        'Problema de XY1012 derivado a mecanico@email.com: No parte'
    """
    # Simulación de workflow
    return f"Problema de {patente} derivado a {responsable}: {descripcion}"
