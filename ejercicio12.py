def main():
    alumnos = [
        {
            'Nombre': 'David', 
            'Sexo': 'M', 
            'Edad': 29, 
            'Peso': 69, 
            'Estatura': 1.71, 
            'Ojos': 2,
            'Cabello': 1
        },
       {
            'Nombre': 'Arely', 
            'Sexo': 'F', 
            'Edad': 29, 
            'Estatura': 1.70, 
            'Peso': 54,
            'Ojos': 1,
            'Cabello': 2
        },

    ]

    lista_1 = []
    lista_2 = []
    for alumno in alumnos:
        if alumno['Sexo'] == 'F' and alumno['Cabello'] == 2 and alumno['Ojos'] == 1 and 1.65 <= alumno['Estatura'] < 1.75 and alumno['Peso'] < 55:
            lista_1.append(alumno)
        elif alumno['Sexo'] == 'M' and alumno['Ojos'] == 2 and 1.70 < alumno['Estatura'] and 60 <= alumno['Peso'] < 70:
            lista_2.append(alumno)

    
    print('Lista 1')
    for alumno in lista_1:
        print(alumno)

    print('Lista 2')
    for alumno in lista_2:
        print(alumno)
        
if __name__ == "__main__":
    main()