import pandas as pd

PAGOS_XLSX = "C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/data/pagos.xlsx"
CLIENTES_XLSX = "C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/data/clientes.xlsx"

def consultar_pagos_cliente(id_cliente: int) -> str:
    """
    Devuelve el estado de pagos del cliente por su ID.

    Args:
        id_cliente (int): ID del cliente.

    Returns:
        str: Resumen de pagos del cliente o mensaje de error.

    Ejemplo:
        >>> consultar_pagos_cliente(2)
        'Cliente 2: 3 pagos realizados, 1 pendiente, 0 atrasados. Total pagado: $500.000, Total adeudado: $120.000'
    """
    import pandas as pd
    import os
    if not os.path.exists(PAGOS_XLSX):
        return "No existe base de pagos."
    pagos = pd.read_excel(PAGOS_XLSX)
    cliente_pagos = pagos[pagos['id_cliente'] == id_cliente]
    if cliente_pagos.empty:
        return f"El cliente con ID {id_cliente} no tiene pagos registrados."
    resumen = cliente_pagos.groupby('estado').size().to_dict()
    total_pagado = cliente_pagos[cliente_pagos['estado']=='Pagado']['monto'].sum()
    total_adeudado = cliente_pagos[cliente_pagos['estado']!='Pagado']['monto'].sum()
    return (
        f"Cliente {id_cliente}: {resumen.get('Pagado', 0)} pagos realizados, "
        f"{resumen.get('Pendiente', 0)} pendientes, {resumen.get('Atrasado', 0)} atrasados. "
        f"Total pagado: ${total_pagado:,.0f}, Total adeudado: ${total_adeudado:,.0f}"
    )


def listar_pagos_pendientes() -> str:
    """
    Lista todos los pagos pendientes y atrasados de todos los clientes.

    Returns:
        str: Pagos pendientes/atrasados o mensaje si todo está al día.

    Ejemplo:
        >>> listar_pagos_pendientes()
        'Cliente 2: $120.000 pendiente (Reserva 5)\nCliente 3: $80.000 atrasado (Reserva 7)'
    """
    import pandas as pd
    import os
    if not os.path.exists(PAGOS_XLSX):
        return "No existe base de pagos."
    pagos = pd.read_excel(PAGOS_XLSX)
    pendientes = pagos[pagos['estado'].isin(['Pendiente', 'Atrasado'])]
    if pendientes.empty:
        return "No hay pagos pendientes ni atrasados."
    salida = []
    for _, row in pendientes.iterrows():
        salida.append(f"Cliente {row['id_cliente']}: ${row['monto']:,.0f} {row['estado'].lower()} (Reserva {row.get('id_reserva','-')})")
    return '\n'.join(salida)


def generar_reporte_utilizacion(fecha_inicio: str, fecha_fin: str) -> str:
    """
    Genera un reporte de utilización de vehículos entre dos fechas, basado en reservas.

    Args:
        fecha_inicio (str): Fecha inicial (YYYY-MM-DD).
        fecha_fin (str): Fecha final (YYYY-MM-DD).
    Returns:
        str: Resumen de utilización por vehículo.

    Ejemplo:
        >>> generar_reporte_utilizacion('2025-05-01', '2025-05-31')
        'ID 1 - Patente XY1012: 5 días reservados\nID 3 - Patente AB1234: 0 días reservados'
    """
    import pandas as pd
    import os
    from agente_gerente_operaciones.core.tools_vehiculos import VEHICULOS_XLSX
    from agente_gerente_operaciones.core.tools_reservas import RESERVAS_XLSX
    try:
        ini = pd.to_datetime(fecha_inicio).date()
        fin = pd.to_datetime(fecha_fin).date()
        if fin < ini:
            return "Error: La fecha final no puede ser anterior a la inicial."
    except Exception:
        return "Error: Formato de fechas inválido. Use YYYY-MM-DD."
    if not os.path.exists(VEHICULOS_XLSX) or not os.path.exists(RESERVAS_XLSX):
        return "No existe base de vehículos o reservas."
    dfv = pd.read_excel(VEHICULOS_XLSX)
    dfr = pd.read_excel(RESERVAS_XLSX)
    resumen = []
    for _, v in dfv.iterrows():
        idv = v['id']
        total_dias = 0
        reservas = dfr[(dfr['id_vehiculo'] == idv) & (dfr['estado'] == 'Activa')]
        for _, r in reservas.iterrows():
            try:
                r_ini = pd.to_datetime(r['fecha_reserva']).date()
                r_fin = pd.to_datetime(r['fecha_devolucion']).date()
            except Exception:
                continue
            # Calcular solapamiento con el rango pedido
            ini_sol = max(ini, r_ini)
            fin_sol = min(fin, r_fin)
            dias = (fin_sol - ini_sol).days + 1
            if dias > 0:
                total_dias += dias
        resumen.append(f"ID {v['id']} - Patente {v['patente']}: {total_dias} días reservados")
    return '\n'.join(resumen)


def reporte_ingresos(fecha_inicio: str, fecha_fin: str) -> str:
    """
    Genera un reporte de ingresos por pagos realizados entre dos fechas.

    Args:
        fecha_inicio (str): Fecha inicial (YYYY-MM-DD).
        fecha_fin (str): Fecha final (YYYY-MM-DD).
    Returns:
        str: Total de ingresos y detalle por cliente.

    Ejemplo:
        >>> reporte_ingresos('2025-05-01', '2025-05-31')
        'Total ingresos: $500.000\nCliente 2: $300.000\nCliente 5: $200.000'
    """
    import pandas as pd
    import os
    if not os.path.exists(PAGOS_XLSX):
        return "No existe base de pagos."
    try:
        ini = pd.to_datetime(fecha_inicio).date()
        fin = pd.to_datetime(fecha_fin).date()
        if fin < ini:
            return "Error: La fecha final no puede ser anterior a la inicial."
    except Exception:
        return "Error: Formato de fechas inválido. Use YYYY-MM-DD."
    pagos = pd.read_excel(PAGOS_XLSX)
    pagos = pagos[(pagos['estado'] == 'Pagado') & (pd.to_datetime(pagos['fecha_pago']).dt.date >= ini) & (pd.to_datetime(pagos['fecha_pago']).dt.date <= fin)]
    if pagos.empty:
        return "No hay ingresos registrados en ese rango."
    total = pagos['monto'].sum()
    detalle = pagos.groupby('id_cliente')['monto'].sum()
    salida = [f"Total ingresos: ${total:,.0f}"]
    for idc, monto in detalle.items():
        salida.append(f"Cliente {idc}: ${monto:,.0f}")
    return '\n'.join(salida)
