from datetime import date


def calcular_dias_vividos(nacimiento):
    hoy = date.today()

    dias_vividos = (hoy - nacimiento).days

    return dias_vividos


def main():
    dia = int(input('Dia de nacimiento: '))
    mes = int(input('Mes de nacimiento: '))
    año = int(input('Año de nacimiento: '))

    nacimiento = date(año, mes, dia)
    dias_vividos = calcular_dias_vividos(nacimiento)
    print('dias_vividos', dias_vividos)
    
main()
