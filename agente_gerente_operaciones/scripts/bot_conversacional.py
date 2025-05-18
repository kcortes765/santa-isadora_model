import sys
import os
# Asegura que la raíz del proyecto esté en sys.path
PROYECTO_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROYECTO_RAIZ not in sys.path:
    sys.path.insert(0, PROYECTO_RAIZ)
from agente_gerente_operaciones.core import tools_vehiculos, tools_documentos, tools_reservas, tools_pagos, tools_comunicacion

MENU = '''\n=== Agente Gerente de Operaciones ===\nSeleccione una acción:\n1. Consultar estado de vehículo\n2. Listar vehículos disponibles\n3. Registrar reserva\n4. Consultar reservas de un vehículo\n5. Cancelar reserva\n6. Consultar pagos de cliente\n7. Listar pagos pendientes\n8. Enviar notificación\n9. Salir\n''' 

def main():
    while True:
        print(MENU)
        opcion = input('Ingrese el número de la acción: ').strip()
        if opcion == '1':
            patente = input('Ingrese la patente: ')
            print(tools_vehiculos.consulta_estado_vehiculo(patente))
        elif opcion == '2':
            inicio = input('Fecha inicio (YYYY-MM-DD): ')
            fin = input('Fecha fin (YYYY-MM-DD): ')
            print(tools_reservas.vehiculos_disponibles(inicio, fin))
        elif opcion == '3':
            id_vehiculo = int(input('ID del vehículo: '))
            id_cliente = int(input('ID del cliente: '))
            fecha_reserva = input('Fecha reserva (YYYY-MM-DD): ')
            fecha_devolucion = input('Fecha devolución (YYYY-MM-DD): ')
            motivo = input('Motivo: ')
            print(tools_reservas.registrar_reserva(id_vehiculo, id_cliente, fecha_reserva, fecha_devolucion, motivo))
        elif opcion == '4':
            id_vehiculo = int(input('ID del vehículo: '))
            print(tools_reservas.consultar_reservas_vehiculo(id_vehiculo))
        elif opcion == '5':
            id_reserva = int(input('ID de la reserva: '))
            print(tools_reservas.cancelar_reserva(id_reserva))
        elif opcion == '6':
            id_cliente = int(input('ID del cliente: '))
            print(tools_pagos.consultar_pagos_cliente(id_cliente))
        elif opcion == '7':
            print(tools_pagos.listar_pagos_pendientes())
        elif opcion == '8':
            mensaje = input('Mensaje: ')
            destinatario = input('Destinatario (email o WhatsApp): ')
            print(tools_comunicacion.enviar_notificacion(mensaje, destinatario))
        elif opcion == '9':
            print('¡Hasta luego!')
            sys.exit(0)
        else:
            print('Opción no válida. Intente nuevamente.')

if __name__ == '__main__':
    main()
