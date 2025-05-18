"""
Script para poblar archivos .xlsx con datos simulados alineados para pruebas del agente de operaciones.
"""
import pandas as pd
import random
import datetime

# Vehículos
vehiculos = pd.DataFrame([
    {
        'id': i+1,
        'patente': f"XY{i+1000:04d}",
        'tipo': random.choice(['Camioneta', 'Camión', 'Auto', 'Furgón', 'SUV']),
        'marca': random.choice(['Toyota', 'Chevrolet', 'Hyundai', 'Nissan', 'Ford']),
        'modelo': random.choice(['Hilux', 'D-Max', 'Accent', 'NP300', 'Ranger']),
        'anio': random.randint(2015, 2024),
        'estado': random.choice(['Disponible', 'En mantención', 'Reservado']),
        'km': random.randint(5000, 150000),
        'vencimiento_soap': (datetime.date.today() + datetime.timedelta(days=random.randint(5, 300))).isoformat(),
        'vencimiento_tecnica': (datetime.date.today() + datetime.timedelta(days=random.randint(10, 365))).isoformat(),
    }
    for i in range(50)
])
vehiculos.to_excel('C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/data/vehiculos.xlsx', index=False)

# Clientes
clientes = pd.DataFrame([
    {
        'id': i+1,
        'nombre': f"Cliente {i+1}",
        'rut': f"{random.randint(10000000, 25000000)}-{random.randint(0,9)}",
        'email': f"cliente{i+1}@mail.com",
        'telefono': f"+569{random.randint(10000000,99999999)}",
        'estado': random.choice(['Activo', 'Inactivo']),
    }
    for i in range(30)
])
clientes.to_excel('C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/data/clientes.xlsx', index=False)

# Reservas
reservas = pd.DataFrame([
    {
        'id': i+1,
        'id_vehiculo': random.randint(1, 50),
        'id_cliente': random.randint(1, 30),
        'fecha_reserva': (datetime.date.today() + datetime.timedelta(days=random.randint(-15, 30))).isoformat(),
        'fecha_devolucion': (datetime.date.today() + datetime.timedelta(days=random.randint(16, 60))).isoformat(),
        'estado': random.choice(['Activa', 'Finalizada', 'Cancelada']),
        'motivo': random.choice(['Trabajo', 'Emergencia', 'Mantenimiento', 'Otro'])
    }
    for i in range(60)
])
reservas.to_excel('C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/data/reservas.xlsx', index=False)

# Pagos
pagos = pd.DataFrame([
    {
        'id': i+1,
        'id_cliente': random.randint(1, 30),
        'monto': random.randint(50000, 500000),
        'fecha_pago': (datetime.date.today() - datetime.timedelta(days=random.randint(1, 120))).isoformat(),
        'estado': random.choice(['Pagado', 'Pendiente', 'Atrasado'])
    }
    for i in range(80)
])
pagos.to_excel('C:/Seba/Proyectos paralelos/santa-isadora_model/agente_gerente_operaciones/data/pagos.xlsx', index=False)

print('Datos simulados cargados exitosamente.')
