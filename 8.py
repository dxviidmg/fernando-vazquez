def main():
    articulos = [
        {
        'articulo': 'X',
        'costo_produccion': 5,
    },
    {
        'articulo': 'Y',
        'costo_produccion': 6,
    }
    ,{
        'articulo': 'Z',
        'costo_produccion': 7,
    }
    ]
    print('articulo, utilidad, impuesto, precio_venta')
    total_utilidad = 0
    total_impuesto = 0
    total_precio_venta = 0
    for articulo in articulos:
        utilidad = articulo['costo_produccion'] * 1.2
        impuesto = (utilidad + articulo['costo_produccion']) * 0.15
        precio_venta = utilidad + articulo['costo_produccion'] + impuesto
        print(articulo['articulo'], utilidad, impuesto, precio_venta)

        total_utilidad += utilidad
        total_impuesto += impuesto
        total_precio_venta += precio_venta

    print('Total utilidad', total_utilidad)
    print('Total impuesto', total_impuesto)
    print('Total precio venta', total_precio_venta)                        

main()