def main():
    print('1 Pequeña')
    print('2 Mediada')
    print('3 Grande')
    tamaño = int(input('Tamaño: '))
    ingredientes = int(input('Numero de ingredientes extra: '))
    costo_ingrediente_adicional = 2

    costo_adicional = ingredientes * costo_ingrediente_adicional

    if tamaño == 1:
        costo_variable = 10
    elif tamaño == 2:
        costo_variable = 12
    elif tamaño == 3:
        costo_variable = 6
    else:
        main()

    costo_fijo = 10
    costo = costo_fijo + costo_variable + costo_adicional
    precio_venta = costo * 1.5

    print('Precio', precio_venta)
    
main()