from ejercicio9 import get_reporte


def main():
    while True:
        get_reporte()
        pregunta = input('Si desea atender otro cliente oprima 1: ')

        if pregunta != '1':
            break
    
if __name__ == "__main__":
    main()