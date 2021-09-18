from utils import print_table


def input_alumnos():
    alumnos = []

    while True:
        alumno = input('Alumno (Si hay no hay mas alumnos oprima 0): ')

        if alumno == "0":
            break

        calificacion_1 = int(input('Calificacion primer parcial: '))
        calificacion_2 = int(input('Calificacion segundo parcial: '))
        calificacion_3 = int(input('Calificacion tercer parcial: '))

        

        data = {
            'alumno': alumno,
            'calificacion_1': calificacion_1,
            'calificacion_2': calificacion_2,
            'calificacion_3': calificacion_3,
        }

        alumnos.append(data)

    return alumnos

def main():
    alumnos = input_alumnos()
    
    for alumno in alumnos:
        promedio = (alumno['calificacion_1'] + alumno['calificacion_2'] + alumno['calificacion_3']) / 3
        alumno['promedio'] = promedio

        del alumno['calificacion_1']
        del alumno['calificacion_2']
        del alumno['calificacion_3']

#    print(alumnos)
    alumnos.append({'alumno': 'Total ' + str(len(alumnos)) + ' alumnos'})
    print_table(alumnos, headers=['Alumno', 'Promedio'])

if __name__ == "__main__":
    main()