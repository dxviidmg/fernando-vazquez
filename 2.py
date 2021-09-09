from utils import get_sample

def contar_calificaciones(calificaciones):
    contador_1 = 0
    contador_2 = 0
    contador_3 = 0
    contador_4 = 0

    for calificacion in calificaciones:
        if 0 <= calificacion < 50:
            contador_1 += 1
        elif 50 <= calificacion < 70:
            contador_2 += 1
        elif 70 <= calificacion < 80:
            contador_3 += 1
        else:
            contador_4 += 1

    c = {'<50': contador_1, '50-70': contador_2, '70-80': contador_3, '>80': contador_4}
    return c

def main():
    rango_minimo_de_calificacion = 0
    rango_maximo_de_calificacion = 100
    numero_de_alumnos = 10
    calificaciones = get_sample(rango_minimo_de_calificacion, rango_maximo_de_calificacion, numero_de_alumnos)

    calificaciones = sorted(calificaciones)
    print('Calificaciones', calificaciones)
    contador = contar_calificaciones(calificaciones)
    print('Contador', contador)

main()