def main():
    n = int(input('Con que numero deseas practicar?: '))

    aciertos = 0
    for i in range(1, 11):
        respuesta_correcta = n * i

        operacion = str(n) + '*' + str(i) + '='
        respuesta = int(input(operacion))

        if respuesta == respuesta_correcta:
            print('Valor correcto')
            aciertos += 1
        else:
            print('Lo siento se ha equivocado. La respuesta correcta era', respuesta_correcta)

        print('Has acertado ', aciertos, 'veces')
        

    
main()