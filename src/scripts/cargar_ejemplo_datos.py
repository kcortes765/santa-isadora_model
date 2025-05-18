import pandas as pd
import os

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))

def cargar_vehiculos():
    archivo = os.path.join(DATA_DIR, 'vehiculos.xlsx')
    import random
    import datetime
    tipos = ['Camioneta', 'Camión Pluma', 'Furgón', 'Minibús', 'Camión', 'SUV']
    marcas = ['Toyota', 'Mercedes', 'Hyundai', 'Nissan', 'Renault', 'Ford', 'Chevrolet']
    modelos = ['Hilux', 'Arocs', 'H1', 'Navara', 'Master', 'Ranger', 'D-Max']
    estados = ['Disponible', 'En mantención', 'Reservado', 'Disponible', 'Disponible']
    choferes = ['Pedro', 'Juan', 'Luis', 'Ana', 'Carlos', 'Sofía', 'María']
    ejemplo = {
        'id': list(range(1, 26)),
        'tipo': [random.choice(tipos) for _ in range(25)],
        'marca': [random.choice(marcas) for _ in range(25)],
        'modelo': [random.choice(modelos) for _ in range(25)],
        'año': [random.randint(2016, 2023) for _ in range(25)],
        'patente': [f"{chr(65+random.randint(0,25))}{chr(65+random.randint(0,25))}-{random.randint(1000,9999)}" for _ in range(25)],
        'estado': [random.choice(estados) for _ in range(25)],
        'chofer_asignado': [random.choice(choferes) for _ in range(25)],
        'fecha_ultimo_servicio': [(datetime.date(2025,1,1) + datetime.timedelta(days=random.randint(0,150))).isoformat() for _ in range(25)],
        'km_actual': [random.randint(10000,120000) for _ in range(25)],
        'permiso_circulacion_venc': [(datetime.date(2026,1,1) + datetime.timedelta(days=random.randint(0,365))).isoformat() for _ in range(25)],
        'revision_tecnica_venc': [(datetime.date(2025,6,1) + datetime.timedelta(days=random.randint(0,180))).isoformat() for _ in range(25)],
        'soap_venc': [(datetime.date(2026,1,1) + datetime.timedelta(days=random.randint(0,365))).isoformat() for _ in range(25)],
        'decreto_60_venc': [(datetime.date(2026,1,1) + datetime.timedelta(days=random.randint(0,365))).isoformat() for _ in range(25)],
        'mantencion_venc': [(datetime.date(2025,6,1) + datetime.timedelta(days=random.randint(0,180))).isoformat() for _ in range(25)],
        'observaciones': [random.choice(['-', 'Cambio aceite', 'Falla menor', 'Listo para entrega', 'Revisión urgente']) for _ in range(25)],
        'proveedor': [random.choice(['-', 'Subcontratado', 'Propio']) for _ in range(25)],
        'fecha_alta': [(datetime.date(2018,1,1) + datetime.timedelta(days=random.randint(0,2000))).isoformat() for _ in range(25)],
        'fecha_baja': [None for _ in range(25)]
    }
    df_ejemplo = pd.DataFrame(ejemplo)
    df_ejemplo.to_excel(archivo, index=False, engine='openpyxl')
    print('Ejemplo de vehículos cargado (25 registros).')

def cargar_reservas():
    archivo = os.path.join(DATA_DIR, 'reservas.xlsx')
    try:
        df = pd.read_excel(archivo, engine='openpyxl')
        vacio = df.shape[0] == 0
    except Exception:
        vacio = True
    import random
    import datetime
    ejemplo = {
        'id': list(range(1, 31)),
        'fecha_solicitud': [(datetime.date(2025,5,1) + datetime.timedelta(days=random.randint(0,30))).isoformat() for _ in range(30)],
        'fecha_inicio': [(datetime.date(2025,5,10) + datetime.timedelta(days=random.randint(0,30))).isoformat() for _ in range(30)],
        'fecha_fin': [(datetime.date(2025,5,11) + datetime.timedelta(days=random.randint(0,30))).isoformat() for _ in range(30)],
        'vehiculo_id': [random.randint(1,25) for _ in range(30)],
        'solicitado_por': [random.choice(['Pedro', 'Luis', 'Ana', 'Juan', 'Sofía', 'Carlos']) for _ in range(30)],
        'cliente_obra': [random.choice(['Faena Norte', 'Cliente Sur', 'Obra Centro', 'Cliente A', 'Faena Este']) for _ in range(30)],
        'destino': [random.choice(['Calama', 'Copiapó', 'Antofagasta', 'Iquique', 'Tocopilla', 'La Serena']) for _ in range(30)],
        'chofer': [random.choice(['Pedro', 'Luis', 'Ana', 'Juan', 'Sofía', 'Carlos']) for _ in range(30)],
        'estado': [random.choice(['Activa', 'Pendiente', 'Finalizada']) for _ in range(30)],
        'motivo': [random.choice(['Traslado de materiales', 'Entrega maquinaria', 'Transporte personal', 'Revisión técnica', 'Inspección']) for _ in range(30)],
        'observaciones': [random.choice(['-', 'Requiere GPS', 'Llevar extintor', 'Urgente', '']) for _ in range(30)]
    }
    df_ejemplo = pd.DataFrame(ejemplo)
    df_ejemplo.to_excel(archivo, index=False, engine='openpyxl')
    print('Ejemplo de reservas cargado (30 registros).')

def cargar_servicios():
    archivo = os.path.join(DATA_DIR, 'servicios.xlsx')
    try:
        df = pd.read_excel(archivo, engine='openpyxl')
        vacio = df.shape[0] == 0
    except Exception:
        vacio = True
    import random
    import datetime
    ejemplo = {
        'id': list(range(1, 21)),
        'fecha': [(datetime.date(2025,5,1) + datetime.timedelta(days=random.randint(0,30))).isoformat() for _ in range(20)],
        'vehiculo_id': [random.randint(1,25) for _ in range(20)],
        'chofer': [random.choice(['Pedro', 'Luis', 'Ana', 'Juan', 'Sofía', 'Carlos']) for _ in range(20)],
        'cliente_obra': [random.choice(['Faena Norte', 'Cliente Sur', 'Obra Centro', 'Cliente A', 'Faena Este']) for _ in range(20)],
        'origen': [random.choice(['Antofagasta', 'Copiapó', 'Iquique', 'La Serena']) for _ in range(20)],
        'destino': [random.choice(['Calama', 'Tocopilla', 'Antofagasta', 'Iquique', 'La Serena']) for _ in range(20)],
        'km_inicio': [random.randint(10000,120000) for _ in range(20)],
        'km_fin': [random.randint(10001,121000) for _ in range(20)],
        'duracion': [f"{random.randint(1,5)}h" for _ in range(20)],
        'estado': [random.choice(['Completado', 'En curso', 'Pendiente']) for _ in range(20)],
        'observaciones': [random.choice(['Sin novedades', 'Demora por desvío', 'Entrega puntual', '']) for _ in range(20)]
    }
    df_ejemplo = pd.DataFrame(ejemplo)
    df_ejemplo.to_excel(archivo, index=False, engine='openpyxl')
    print('Ejemplo de servicios cargado (20 registros).')

def cargar_pagos():
    archivo = os.path.join(DATA_DIR, 'pagos.xlsx')
    try:
        df = pd.read_excel(archivo, engine='openpyxl')
        vacio = df.shape[0] == 0
    except Exception:
        vacio = True
    import random
    import datetime
    ejemplo = {
        'id': list(range(1, 26)),
        'fecha_emision': [(datetime.date(2025,5,1) + datetime.timedelta(days=random.randint(0,30))).isoformat() for _ in range(25)],
        'fecha_vencimiento': [(datetime.date(2025,5,10) + datetime.timedelta(days=random.randint(0,30))).isoformat() for _ in range(25)],
        'cliente_proveedor': [random.choice(['Cliente A', 'Proveedor B', 'Cliente C', 'Cliente Z', 'Proveedor Q']) for _ in range(25)],
        'monto': [random.randint(200000, 2500000) for _ in range(25)],
        'concepto': [random.choice(['Arriendo camioneta', 'Mantención pluma', 'Transporte personal', 'Compra repuestos', 'Pago honorarios']) for _ in range(25)],
        'pagado': [random.choice(['Sí', 'No']) for _ in range(25)],
        'fecha_pago': [random.choice([None, (datetime.date(2025,5,15) + datetime.timedelta(days=random.randint(0,30))).isoformat()]) for _ in range(25)],
        'forma_pago': [random.choice([None, 'Transferencia', 'Cheque', 'Efectivo']) for _ in range(25)],
        'observaciones': [random.choice(['-', 'Pendiente de abono', 'Requiere factura', 'Pagado en caja', '']) for _ in range(25)]
    }
    df_ejemplo = pd.DataFrame(ejemplo)
    df_ejemplo.to_excel(archivo, index=False, engine='openpyxl')
    print('Ejemplo de pagos cargado (25 registros).')

def cargar_personal():
    archivo = os.path.join(DATA_DIR, 'personal.xlsx')
    try:
        df = pd.read_excel(archivo, engine='openpyxl')
        vacio = df.shape[0] == 0
    except Exception:
        vacio = True
    import random
    import datetime
    nombres = ['Pedro', 'Juan', 'Luis', 'Ana', 'Sofía', 'Carlos', 'María', 'José', 'Valentina', 'Ignacio', 'Camila']
    licencias = ['B', 'A2', 'A4', 'C', 'D']
    estados = ['Activo', 'Inactivo']
    ejemplo = {
        'id': list(range(1, 21)),
        'nombre': [random.choice(nombres) for _ in range(20)],
        'rut': [f"{random.randint(10,25)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(0,9)}" for _ in range(20)],
        'licencia': [random.choice(licencias) for _ in range(20)],
        'fecha_venc_licencia': [(datetime.date(2026,1,1) + datetime.timedelta(days=random.randint(0,365))).isoformat() for _ in range(20)],
        'contacto': [f"+569{random.randint(10000000,99999999)}" for _ in range(20)],
        'estado': [random.choice(estados) for _ in range(20)],
        'observaciones': [random.choice(['-', '', 'Licencia suspendida', 'Nuevo ingreso', '']) for _ in range(20)]
    }
    df_ejemplo = pd.DataFrame(ejemplo)
    df_ejemplo.to_excel(archivo, index=False, engine='openpyxl')
    print('Ejemplo de personal cargado (20 registros).')

def cargar_proveedores():
    archivo = os.path.join(DATA_DIR, 'proveedores.xlsx')
    try:
        df = pd.read_excel(archivo, engine='openpyxl')
        vacio = df.shape[0] == 0
    except Exception:
        vacio = True
    import random
    import datetime
    tipos_servicio = ['Mantención', 'Repuestos', 'Reparación', 'Transporte', 'Consultoría']
    estados = ['Activo', 'Inactivo']
    ejemplo = {
        'id': list(range(1, 16)),
        'nombre': [f"Proveedor {chr(65+i)}" for i in range(15)],
        'rut': [f"{random.randint(50,99)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(0,9)}" for _ in range(15)],
        'contacto': [f"+569{random.randint(10000000,99999999)}" for _ in range(15)],
        'tipo_servicio': [random.choice(tipos_servicio) for _ in range(15)],
        'estado': [random.choice(estados) for _ in range(15)],
        'observaciones': [random.choice(['Contrato anual', 'Solo compras puntuales', 'Atención 24/7', '-', '']) for _ in range(15)]
    }
    df_ejemplo = pd.DataFrame(ejemplo)
    df_ejemplo.to_excel(archivo, index=False, engine='openpyxl')
    print('Ejemplo de proveedores cargado (15 registros).')

if __name__ == '__main__':
    cargar_vehiculos()
    cargar_reservas()
    cargar_servicios()
    cargar_pagos()
    cargar_personal()
    cargar_proveedores()
