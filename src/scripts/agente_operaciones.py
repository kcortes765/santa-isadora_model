import pandas as pd
import os

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))

ARCHIVOS = {
    'vehiculos': 'vehiculos.xlsx',
    'reservas': 'reservas.xlsx',
    'servicios': 'servicios.xlsx',
    'pagos': 'pagos.xlsx',
    'personal': 'personal.xlsx',
    'proveedores': 'proveedores.xlsx',
}

def cargar_df(nombre):
    archivo = os.path.join(DATA_DIR, ARCHIVOS[nombre])
    return pd.read_excel(archivo, engine='openpyxl')

def consultar_disponibilidad(tipo=None):
    df = cargar_df('vehiculos')
    if tipo:
        df = df[df['tipo'].str.lower() == tipo.lower()]
    disponibles = df[df['estado'] == 'Disponible']
    print(f"\nVehículos disponibles{f' de tipo {tipo}' if tipo else ''}:")
    print(disponibles[['id','tipo','marca','modelo','patente','chofer_asignado']].to_string(index=False))

def ver_reservas(estado=None):
    df = cargar_df('reservas')
    if estado:
        df = df[df['estado'].str.lower() == estado.lower()]
    print("\nReservas:")
    print(df[['id','fecha_inicio','fecha_fin','vehiculo_id','solicitado_por','estado']].to_string(index=False))

def registrar_reserva():
    df_veh = cargar_df('vehiculos')
    disponibles = df_veh[df_veh['estado'] == 'Disponible']
    if disponibles.empty:
        print("No hay vehículos disponibles.")
        return
    print("Vehículos disponibles:")
    print(disponibles[['id','tipo','marca','modelo','patente']].to_string(index=False))
    vid = int(input("Ingrese ID de vehículo a reservar: "))
    nombre = input("Solicitado por: ")
    cliente = input("Cliente/Obra: ")
    destino = input("Destino: ")
    chofer = input("Chofer asignado: ")
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
    motivo = input("Motivo: ")
    obs = input("Observaciones: ")
    df_res = cargar_df('reservas')
    nuevo = {
        'id': df_res['id'].max() + 1 if not df_res.empty else 1,
        'fecha_solicitud': pd.Timestamp.now().date(),
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'vehiculo_id': vid,
        'solicitado_por': nombre,
        'cliente_obra': cliente,
        'destino': destino,
        'chofer': chofer,
        'estado': 'Activa',
        'motivo': motivo,
        'observaciones': obs,
    }
    df_res = pd.concat([df_res, pd.DataFrame([nuevo])], ignore_index=True)
    df_res.to_excel(os.path.join(DATA_DIR, ARCHIVOS['reservas']), index=False, engine='openpyxl')
    print("Reserva registrada.")

def alertas_vencimientos():
    df = cargar_df('vehiculos')
    hoy = pd.Timestamp.now().date()
    print("\nVehículos con documentos por vencer en los próximos 60 días:")
    for col in ['permiso_circulacion_venc','revision_tecnica_venc','soap_venc','decreto_60_venc','mantencion_venc']:
        vencimientos = df[pd.to_datetime(df[col], errors='coerce').dt.date.between(hoy, hoy + pd.Timedelta(days=60))]
        if not vencimientos.empty:
            print(f"\n- {col}:")
            print(vencimientos[['id','tipo','marca','modelo','patente',col]].to_string(index=False))

def menu():
    while True:
        print("\n--- AGENTE OPERACIONES ---")
        print("1. Consultar disponibilidad de vehículos")
        print("2. Ver reservas")
        print("3. Registrar nueva reserva")
        print("4. Alertas de vencimientos")
        print("5. Salir")
        op = input("Seleccione opción: ")
        if op == '1':
            tipo = input("Tipo de vehículo (opcional): ")
            consultar_disponibilidad(tipo if tipo else None)
        elif op == '2':
            estado = input("Estado reserva (opcional): ")
            ver_reservas(estado if estado else None)
        elif op == '3':
            registrar_reserva()
        elif op == '4':
            alertas_vencimientos()
        elif op == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()
