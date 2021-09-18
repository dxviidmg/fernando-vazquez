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
#    total_utilidad = 0
#    total_impuesto = 0
#    total_precio_venta = 0
    
    
    for articulo in articulos:
        precio_total = articulo['cantidad'] * articulo['precio_unitario']
        articulo['precio_total'] = precio_total
#        impuesto = (utilidad + articulo['costo_produccion']) * 0.15
#        precio_venta = utilidad + articulo['costo_produccion'] + impuesto
        

#        articulo['utilidad'] = utilidad
#        articulo['impuesto'] = impuesto
#        articulo['precio_venta'] = precio_venta

        subtotal += precio_total
#        total_utilidad += utilidad
#        total_impuesto += impuesto
#        total_precio_venta += precio_venta

    impuesto = subtotal * 0.15
    total = subtotal + impuesto
    articulos.append({'articulo': '', 'cantidad': '', 'precio_unitario': 'Subtotal', 'precio_total': subtotal})
    articulos.append({'articulo': '', 'cantidad': '', 'precio_unitario': 'Impuesto', 'precio_total': impuesto})
    articulos.append({'articulo': '', 'cantidad': '', 'precio_unitario': 'Total', 'precio_total': total})
    print_table(articulos, headers=['Articulo', 'Cantidad', 'Precio unitario', 'Total'])


def main():
    articulos = input_articulos()
    calculo(articulos)


main()