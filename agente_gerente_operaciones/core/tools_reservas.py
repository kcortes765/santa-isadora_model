import pandas as pd
import datetime
import os

RESERVAS_XLSX = "C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/data/reservas.xlsx"


def registrar_reserva(id_vehiculo: int, id_cliente: int, fecha_reserva: str, fecha_devolucion: str, motivo: str) -> str:
    """
    Registra una nueva reserva en el archivo Excel.
    Valida solapamiento, existencia de vehículo y cliente, y formato de fechas.

    Args:
        id_vehiculo (int): ID del vehículo.
        id_cliente (int): ID del cliente.
        fecha_reserva (str): Fecha de inicio de la reserva (YYYY-MM-DD).
        fecha_devolucion (str): Fecha de devolución de la reserva (YYYY-MM-DD).
        motivo (str): Motivo de la reserva.

    Returns:
        str: Mensaje de éxito o error.

    Ejemplo:
        >>> registrar_reserva(1, 2, '2025-05-20', '2025-05-25', 'Renta por faena')
        'Reserva registrada exitosamente con ID 5.'
    """
    import pandas as pd
    import os
    from agente_gerente_operaciones.core.tools_vehiculos import VEHICULOS_XLSX
    from agente_gerente_operaciones.core.tools_pagos import CLIENTES_XLSX
    import datetime
    # Validar fechas
    try:
        fecha_ini = pd.to_datetime(fecha_reserva).date()
        fecha_fin = pd.to_datetime(fecha_devolucion).date()
        if fecha_fin < fecha_ini:
            return "Error: La fecha de devolución no puede ser anterior a la de reserva."
    except Exception:
        return "Error: Formato de fechas inválido. Use YYYY-MM-DD."
    # Validar existencia de vehículo
    if not os.path.exists(VEHICULOS_XLSX):
        return "Error: No existe base de vehículos."
    dfv = pd.read_excel(VEHICULOS_XLSX)
    if id_vehiculo not in dfv['id'].values:
        return f"Error: No existe el vehículo con ID {id_vehiculo}."
    # Validar existencia de cliente
    if not os.path.exists(CLIENTES_XLSX):
        return "Error: No existe base de clientes."
    dfc = pd.read_excel(CLIENTES_XLSX)
    if id_cliente not in dfc['id'].values:
        return f"Error: No existe el cliente con ID {id_cliente}."
    # Leer reservas
    if not os.path.exists(RESERVAS_XLSX):
        df = pd.DataFrame(columns=['id', 'id_vehiculo', 'id_cliente', 'fecha_reserva', 'fecha_devolucion', 'estado', 'motivo'])
    else:
        df = pd.read_excel(RESERVAS_XLSX)
    # Validación de solapamiento
    reservas_vehiculo = df[df['id_vehiculo'] == id_vehiculo]
    for _, row in reservas_vehiculo.iterrows():
        try:
            r_ini = pd.to_datetime(row['fecha_reserva']).date()
            r_fin = pd.to_datetime(row['fecha_devolucion']).date()
        except Exception:
            continue
        if (fecha_ini <= r_fin) and (fecha_fin >= r_ini) and row['estado'] == 'Activa':
            return f"Error: El vehículo ya está reservado del {r_ini} al {r_fin}."
    nueva_id = int(df['id'].max() + 1) if not df.empty else 1
    nueva = {
        'id': nueva_id,
        'id_vehiculo': id_vehiculo,
        'id_cliente': id_cliente,
        'fecha_reserva': fecha_reserva,
        'fecha_devolucion': fecha_devolucion,
        'estado': 'Activa',
        'motivo': motivo
    }
    df = pd.concat([df, pd.DataFrame([nueva])], ignore_index=True)
    df.to_excel(RESERVAS_XLSX, index=False)
    return f"Reserva registrada exitosamente con ID {nueva_id}."


def vehiculos_disponibles(fecha_inicio: str, fecha_fin: str) -> str:
    """
    Devuelve la lista de vehículos disponibles para reservar entre dos fechas.

    Args:
        fecha_inicio (str): Fecha de inicio (YYYY-MM-DD).
        fecha_fin (str): Fecha de fin (YYYY-MM-DD).

    Returns:
        str: Lista de IDs y patentes de vehículos disponibles.

    Ejemplo:
        >>> vehiculos_disponibles('2025-05-19', '2025-05-25')
        'ID 1 - Patente XY1012\nID 3 - Patente AB1234'
    """
    import pandas as pd
    from agente_gerente_operaciones.core.tools_vehiculos import VEHICULOS_XLSX
    import os
    try:
        ini = pd.to_datetime(fecha_inicio).date()
        fin = pd.to_datetime(fecha_fin).date()
        if fin < ini:
            return "Error: La fecha final no puede ser anterior a la inicial."
    except Exception:
        return "Error: Formato de fechas inválido. Use YYYY-MM-DD."
    # Leer vehículos y reservas
    if not os.path.exists(VEHICULOS_XLSX):
        return "Error: No existe base de vehículos."
    dfv = pd.read_excel(VEHICULOS_XLSX)
    if not os.path.exists(RESERVAS_XLSX):
        return '\n'.join([f"ID {row['id']} - Patente {row['patente']}" for _, row in dfv.iterrows()])
    dfr = pd.read_excel(RESERVAS_XLSX)
    disponibles = []
    for _, v in dfv.iterrows():
        idv = v['id']
        reservas = dfr[(dfr['id_vehiculo'] == idv) & (dfr['estado'] == 'Activa')]
        solapado = False
        for _, r in reservas.iterrows():
            try:
                r_ini = pd.to_datetime(r['fecha_reserva']).date()
                r_fin = pd.to_datetime(r['fecha_devolucion']).date()
            except Exception:
                continue
            if (ini <= r_fin) and (fin >= r_ini):
                solapado = True
                break
        if not solapado:
            disponibles.append(f"ID {v['id']} - Patente {v['patente']}")
    if not disponibles:
        return "No hay vehículos disponibles en ese rango."
    return '\n'.join(disponibles)


def consultar_reservas_vehiculo(id_vehiculo: int) -> str:
    """
    Lista todas las reservas activas y futuras de un vehículo por su ID.

    Args:
        id_vehiculo (int): ID del vehículo.
    Returns:
        str: Reservas activas/futuras o mensaje si no hay.

    Ejemplo:
        >>> consultar_reservas_vehiculo(1)
        'Reserva ID 5: 2025-05-20 a 2025-05-25, Cliente 2, Estado: Activa.'
    """
    import pandas as pd
    import os
    import datetime
    if not os.path.exists(RESERVAS_XLSX):
        return "No hay reservas registradas."
    df = pd.read_excel(RESERVAS_XLSX)
    hoy = datetime.date.today()
    reservas = df[(df['id_vehiculo'] == id_vehiculo) & (pd.to_datetime(df['fecha_devolucion']).dt.date >= hoy)]
    if reservas.empty:
        return "No hay reservas activas o futuras para este vehículo."
    salida = []
    for _, row in reservas.iterrows():
        salida.append(f"Reserva ID {row['id']}: {row['fecha_reserva']} a {row['fecha_devolucion']}, Cliente {row['id_cliente']}, Estado: {row['estado']}.")
    return '\n'.join(salida)


def cancelar_reserva(id_reserva: int) -> str:
    """
    Cancela una reserva activa por ID, cambiando su estado a 'Cancelada'.

    Args:
        id_reserva (int): ID de la reserva a cancelar.
    Returns:
        str: Mensaje de éxito o error.

    Ejemplo:
        >>> cancelar_reserva(5)
        'Reserva ID 5 cancelada exitosamente.'
    """
    import pandas as pd
    import os
    if not os.path.exists(RESERVAS_XLSX):
        return "No hay reservas registradas."
    df = pd.read_excel(RESERVAS_XLSX)
    idx = df[df['id'] == id_reserva].index
    if idx.empty:
        return f"No existe reserva con ID {id_reserva}."
    if df.loc[idx[0], 'estado'] == 'Cancelada':
        return f"La reserva ID {id_reserva} ya está cancelada."
    df.loc[idx[0], 'estado'] = 'Cancelada'
    df.to_excel(RESERVAS_XLSX, index=False)
    return f"Reserva ID {id_reserva} cancelada exitosamente."
