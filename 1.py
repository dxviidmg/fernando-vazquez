from utils import get_sample


def calcula_comision(venta):
    if 1000000 <= venta <3000000:
        porcentaje_comision = 3
    elif 3000000 <= venta <5000000:
        porcentaje_comision = 4
    elif 5000000 <= venta <7000000:
        porcentaje_comision = 5
    elif 7000000 <= venta:
        porcentaje_comision = 6
    else:
        porcentaje_comision = 0

    comision = venta * porcentaje_comision / 100

    return comision, porcentaje_comision

def main():
    rango_minimo_de_ventas = 0
    rango_maximo_de_ventas = 10000000
    numero_de_vendedores = 10
    ventas = get_sample(rango_minimo_de_ventas, rango_maximo_de_ventas, numero_de_vendedores)

    for venta in ventas:
        comision, porcentaje_comision = calcula_comision(venta)
        print('Venta:', venta, '. %Comision:', porcentaje_comision, '. Comision', comision)

main()


    
