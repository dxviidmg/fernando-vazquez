from utils import print_table


def input_articulos():
    articulos = []

    while True:
        articulo = input('Articulo (Si hay no hay mas articulos oprima 0): ')

        if articulo == "0":
            break

        costo_produccion = int(input('Costo produccion: '))

        data = {
            'articulo': articulo,
            'costo_produccion': costo_produccion,
        }

        articulos.append(data)

    return articulos

def calculo(articulos):
    total_costo_produccion = 0
    total_utilidad = 0
    total_impuesto = 0
    total_precio_venta = 0
    
    
    for articulo in articulos:
        utilidad = articulo['costo_produccion'] * 1.2
        impuesto = (utilidad + articulo['costo_produccion']) * 0.15
        precio_venta = utilidad + articulo['costo_produccion'] + impuesto
        

        articulo['utilidad'] = utilidad
        articulo['impuesto'] = impuesto
        articulo['precio_venta'] = precio_venta

        total_costo_produccion += articulo['costo_produccion']
        total_utilidad += utilidad
        total_impuesto += impuesto
        total_precio_venta += precio_venta


    articulos.append({'articulo': '', 'costo_produccion': total_costo_produccion, 'utilidad': total_utilidad, 'utilidad': total_utilidad, 'impuesto': total_impuesto, 'precio_venta': total_precio_venta})
    print_table(articulos, headers=['Articulo', 'Costo de produccion', 'Utilidad', 'Impuesto', 'Precio de venta'])

def main():
    articulos = input_articulos()
    calculo(articulos)                       
    
if __name__ == "__main__":
    main()