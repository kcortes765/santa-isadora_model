import pytest
import datetime
from agente_gerente_operaciones.core import tools_vehiculos, tools_documentos, tools_reservas, tools_pagos, tools_comunicacion

def test_consulta_estado_vehiculo():
    r = tools_vehiculos.consulta_estado_vehiculo('XY1012')
    assert isinstance(r, str)
    assert 'Patente' in r

def test_alertar_vencimientos():
    r = tools_documentos.alertar_vencimientos('XY1012', 30)
    assert isinstance(r, str)

def test_listar_documentos_faltantes_o_vencidos():
    r = tools_documentos.listar_documentos_faltantes_o_vencidos()
    assert isinstance(r, str)

def test_registrar_reserva():
    # Debe fallar si fechas mal
    r = tools_reservas.registrar_reserva(1, 2, '2025-05-25', '2025-05-20', 'Test')
    assert 'Error' in r

def test_vehiculos_disponibles():
    r = tools_reservas.vehiculos_disponibles('2025-05-20', '2025-05-25')
    assert isinstance(r, str)

def test_consultar_reservas_vehiculo():
    r = tools_reservas.consultar_reservas_vehiculo(1)
    assert isinstance(r, str)

def test_cancelar_reserva():
    r = tools_reservas.cancelar_reserva(9999)
    assert 'No existe' in r or 'ya está cancelada' in r or 'No hay reservas' in r

def test_consultar_pagos_cliente():
    r = tools_pagos.consultar_pagos_cliente(2)
    assert isinstance(r, str)

def test_listar_pagos_pendientes():
    r = tools_pagos.listar_pagos_pendientes()
    assert isinstance(r, str)

def test_generar_reporte_utilizacion():
    hoy = datetime.date.today()
    r = tools_pagos.generar_reporte_utilizacion(str(hoy), str(hoy))
    assert isinstance(r, str)

def test_reporte_ingresos():
    hoy = datetime.date.today()
    r = tools_pagos.reporte_ingresos(str(hoy), str(hoy))
    assert isinstance(r, str)

def test_enviar_notificacion():
    r = tools_comunicacion.enviar_notificacion('Test', 'test@correo.com')
    assert 'Notificación' in r

def test_enviar_recordatorio_vencimiento():
    r = tools_comunicacion.enviar_recordatorio_vencimiento('XY1012', 'test@correo.com')
    assert isinstance(r, str)

def test_derivar_problema_mecanico():
    r = tools_comunicacion.derivar_problema_mecanico('XY1012', 'No parte', 'mecanico@correo.com')
    assert 'derivado' in r
