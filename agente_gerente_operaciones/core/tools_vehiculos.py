# Herramientas para gestión de vehículos
import pandas as pd

VEHICULOS_XLSX = "C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/data/vehiculos.xlsx"

def consulta_estado_vehiculo(patente: str) -> str:
    """
    Devuelve el estado actual, vencimientos y alertas del vehículo por patente.
    Incluye validación de campos faltantes y alerta de documentos vencidos o próximos a vencer.

    Args:
        patente (str): Patente del vehículo a consultar.

    Returns:
        str: Información detallada del vehículo, estado documental y alertas.

    Ejemplo:
        >>> consulta_estado_vehiculo('XY1012')
        'Patente: XY1012\nTipo: SUV\nMarca: Chevrolet\nModelo: Accent\nAño: 2023\nEstado: Disponible\nKm: 135662\nSOAP vence: 2025-11-22 (vigente)\nTécnica vence: 2025-07-31 (por vencer en 75 días)\nALERTA: Revisión técnica por vencer en menos de 90 días.'
    """
    import datetime
    df = pd.read_excel(VEHICULOS_XLSX)
    row = df[df['patente'] == patente]
    if row.empty:
        return f"No se encontró el vehículo con patente {patente}."
    info = row.iloc[0].to_dict()
    hoy = datetime.datetime.now().date()
    alertas = []
    # Validación y formato de vencimientos
    venc_soap = info.get('vencimiento_soap')
    venc_tecnica = info.get('vencimiento_tecnica')
    def analizar_vencimiento(valor, nombre):
        if not valor or pd.isna(valor):
            alertas.append(f"FALTA fecha de vencimiento de {nombre}.")
            return "No informado"
        try:
            fecha = pd.to_datetime(valor).date()
            dias = (fecha - hoy).days
            if dias < 0:
                alertas.append(f"{nombre} VENCIDO hace {-dias} días.")
                return f"{valor} (vencido)"
            elif dias <= 30:
                alertas.append(f"{nombre} por vencer en {dias} días.")
                return f"{valor} (por vencer en {dias} días)"
            else:
                return f"{valor} (vigente)"
        except Exception:
            alertas.append(f"Error leyendo fecha de {nombre}.")
            return str(valor)
    soap_str = analizar_vencimiento(venc_soap, "SOAP")
    tecnica_str = analizar_vencimiento(venc_tecnica, "revisión técnica")
    # Formato de salida
    salida = (
        f"Patente: {info.get('patente', 'No informado')}\n"
        f"Tipo: {info.get('tipo', 'No informado')}\n"
        f"Marca: {info.get('marca', 'No informado')}\n"
        f"Modelo: {info.get('modelo', 'No informado')}\n"
        f"Año: {info.get('anio', 'No informado')}\n"
        f"Estado: {info.get('estado', 'No informado')}\n"
        f"Km: {info.get('km', 'No informado')}\n"
        f"SOAP vence: {soap_str}\n"
        f"Técnica vence: {tecnica_str}"
    )
    if alertas:
        salida += "\nALERTA: " + "; ".join(alertas)
    return salida
