from utils import print_table


def input_articulos():
    articulos = []

    while True:
        articulo = input('Articulo (Si hay no hay mas articulos oprima 0): ')

        if articulo == "0":
            break

        cantidad = int(input('Cantidad: '))
        precio_unitario = int(input('Precio unitario: '))

        data = {
            'articulo': articulo,
            'cantidad': cantidad,
            'precio_unitario': precio_unitario
        }

        articulos.append(data)

    return articulos


def calculo(articulos):
    subtotal = 0    
    
    for articulo in articulos:
        precio_total = articulo['cantidad'] * articulo['precio_unitario']
        articulo['precio_total'] = precio_total

        subtotal += precio_total

    impuesto = subtotal * 0.15
    total = subtotal + impuesto
    articulos.append({'articulo': '', 'cantidad': '', 'precio_unitario': 'Subtotal', 'precio_total': subtotal})
    articulos.append({'articulo': '', 'cantidad': '', 'precio_unitario': 'Impuesto', 'precio_total': impuesto})
    articulos.append({'articulo': '', 'cantidad': '', 'precio_unitario': 'Total', 'precio_total': total})
    print_table(articulos, headers=['Articulo', 'Cantidad', 'Precio unitario', 'Total'])


def main():
    cliente = input('Nombre: ')

    articulos = input_articulos()
    print('Nombre del cliente: ', cliente)
    calculo(articulos)


main()