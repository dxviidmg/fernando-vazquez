from utils import print_table


def movimiento_saldo(saldo):
    print('Tipo movimiento:\n *1 Deposito\n *2 Retiro')
    tipo_movimiento = input('Tipo movimiento: ')



    if not tipo_movimiento in ['1', '2']:
        print('Error en seleccion de movimiento')
        calcula_nuevo_saldo(saldo)

    cantidad = float(input('Cantidad: '))

    if tipo_movimiento == '1':
        saldo = saldo + cantidad
        data = {'deposito': cantidad, 'retiro': '', 'saldo': saldo}
    else:
        saldo = saldo - cantidad
        data = {'deposito': '', 'retiro': cantidad, 'saldo': saldo}

    return data

def main():
    cuentahabiente = input('Cuentahabiente: ')
    saldo_inicial = float(input('Saldo inicial: '))
    saldo = saldo_inicial
    confirmacion_accion = input("Si desea hacer un movimiento oprima 1: ")
    movimientos = []
    numero_movimiento = 1

    while confirmacion_accion == '1':
        movimiento = movimiento_saldo(saldo)
        movimiento = {'numero_movimiento': numero_movimiento, **movimiento}
        numero_movimiento += 1
        movimientos.append(movimiento)
        saldo = movimiento['saldo']
        confirmacion_accion = input('Si desea hacer un movimiento oprima 1: ')

    print('Cuentahabiente', cuentahabiente)
    print('Saldo inicial', saldo_inicial)
    print_table(movimientos, headers=['Movimiento', 'Deposito', 'Abono', 'Saldo'])


if __name__ == "__main__":
    main()