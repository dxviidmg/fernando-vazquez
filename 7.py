def main():
    articulos = [
        {
        'articulo': 'X',
        'cantidad_producida': 5,
        'factor_costo': 10,
        'costo_fijo': 10
    },
    {
        'articulo': 'Y',
        'cantidad_producida': 6,
        'factor_costo': 8,
        'costo_fijo': 7
    }
    ,{
        'articulo': 'Z',
        'cantidad_producida': 7,
        'factor_costo': 9,
        'costo_fijo': 12
    }
    ]
    print('articulo, cantidad_producida, factor_costo, costo_produccion')
    total_articulos = 0
    total_costo_produccion = 0
    for articulo in articulos:
        costo_produccion = articulo['cantidad_producida'] * (articulo['factor_costo'] + articulo['costo_fijo'])
        total_articulos += articulo['cantidad_producida']
        total_costo_produccion += costo_produccion
        print(articulo['articulo'], articulo['cantidad_producida'], articulo['factor_costo'], costo_produccion)

    
    print('Total productos', total_articulos)
    print('total costo produccion', total_costo_produccion)
    
main()