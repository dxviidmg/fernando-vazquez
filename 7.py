from utils import print_table


def calculo(articulos):
    total_articulos = 0
    total_costo_produccion = 0
    for articulo in articulos:
        costo_produccion = articulo['cantidad_producida'] * (articulo['factor_costo'] + articulo['costo_fijo'])
        articulo['costo_produccion'] = costo_produccion
        total_articulos += articulo['cantidad_producida']
        total_costo_produccion += costo_produccion

    articulos.append({'articulo': 'Total ' + str(total_articulos) + ' articulos', 'cantidad_producida': '', 'factor_costo': '','costo_fijo': '', 'costo_produccion': total_costo_produccion})

    print_table(articulos, headers=['Articulo', 'Cantidad producida', 'Factor costo', 'Costo fijo', 'Costo produccion'])


def input_articulos():
    articulos = []

    while True:
        articulo = input('Articulo (Si hay no hay mas articulos oprima 0): ')

        if articulo == "0":
            break

        cantidad_producida = int(input('Cantidad producida: '))
        factor_costo = int(input('Factor costo: '))
        costo_fijo = int(input('Costo fijo: '))

        data = {
            'articulo': articulo,
            'cantidad_producida': cantidad_producida,
            'factor_costo': factor_costo,
            'costo_fijo': costo_fijo
        }

        articulos.append(data)

    return articulos

def main():
    articulos = input_articulos()
    calculo(articulos)
    
main()