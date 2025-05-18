import pandas as pd
import datetime

VEHICULOS_XLSX = "C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/data/vehiculos.xlsx"

DEF_DIAS_ALERTA = 15

def listar_documentos_faltantes_o_vencidos() -> str:
    """
    Lista todos los vehículos con SOAP o revisión técnica faltantes o vencidos.

    Returns:
        str: Reporte de vehículos con documentación faltante o vencida, o mensaje si todo está al día.

    Ejemplo:
        >>> listar_documentos_faltantes_o_vencidos()
        'Patente XY1012: SOAP vencido el 2025-05-01\nPatente AB1234: FALTA fecha de revisión técnica.'
    """
    df = pd.read_excel(VEHICULOS_XLSX)
    hoy = datetime.date.today()
    reportes = []
    for _, row in df.iterrows():
        patente = row.get('patente', 'Sin patente')
        for doc, col in [('SOAP', 'vencimiento_soap'), ('revisión técnica', 'vencimiento_tecnica')]:
            valor = row.get(col)
            if not valor or pd.isna(valor):
                reportes.append(f"Patente {patente}: FALTA fecha de {doc}.")
                continue
            try:
                fecha = pd.to_datetime(valor).date()
                if (fecha - hoy).days < 0:
                    reportes.append(f"Patente {patente}: {doc} vencido el {fecha}.")
            except Exception:
                reportes.append(f"Patente {patente}: Error leyendo fecha de {doc} ({valor})")
    if not reportes:
        return "Toda la documentación de la flota está al día."
    return "\n".join(reportes)

def alertar_vencimientos(patente: str = None, dias_alerta: int = None) -> str:
    """
    Devuelve alerta si SOAP o revisión técnica están por vencer o vencidos en los próximos X días.
    Si patente es None, revisa toda la flota.

    Args:
        patente (str, optional): Patente del vehículo a consultar. Si es None, revisa todos.
        dias_alerta (int, optional): Días de anticipación para alerta. Si es None, usa DEF_DIAS_ALERTA.

    Returns:
        str: Mensaje de alerta de vencimientos o "No hay vencimientos próximos.".

    Ejemplo:
        >>> alertar_vencimientos('XY1012', 30)
        'Patente XY1012: SOAP por vencer en 12 días (2025-05-28)\nPatente XY1012: Técnica vencida hace 5 días (2025-05-11)'
    """
    df = pd.read_excel(VEHICULOS_XLSX)
    hoy = datetime.date.today()
    if dias_alerta is None:
        dias_alerta = DEF_DIAS_ALERTA
    alertas = []
    rows = df if patente is None else df[df['patente'] == patente]
    for _, row in rows.iterrows():
        patente_actual = row.get('patente', 'Sin patente')
        for doc, col in [('SOAP', 'vencimiento_soap'), ('Técnica', 'vencimiento_tecnica')]:
            valor = row.get(col)
            if not valor or pd.isna(valor):
                alertas.append(f"Patente {patente_actual}: FALTA fecha de vencimiento de {doc}.")
                continue
            try:
                fecha = pd.to_datetime(valor).date()
                dias = (fecha - hoy).days
                if dias < 0:
                    alertas.append(f"Patente {patente_actual}: {doc} vencida hace {-dias} días ({fecha})")
                elif dias <= dias_alerta:
                    alertas.append(f"Patente {patente_actual}: {doc} por vencer en {dias} días ({fecha})")
            except Exception:
                alertas.append(f"Patente {patente_actual}: Error leyendo fecha de {doc} ({valor})")
    if not alertas:
        return "No hay vencimientos próximos."
    return "\n".join(alertas)
