
#n_viajes = int(input('Numero de viajes'))

r = 1

personas_list = []
pesos_list = []
while r == 1:
    personas = int(input('Cantidad de personas: '))
    peso = int(input('Peso del viaje: '))

    personas_list.append(personas)
    pesos_list.append(peso)
    r = int(input('Si desea agregar otro viaje, oprima 1: '))


print()
print('Cantidad de viajes:', len(personas_list))
print('Cantidad de personas trasportadas:', sum(personas_list))
print('Peso transportado:', sum(pesos_list))
print('Promedio de personas por viaje: ', sum(personas_list)/len(personas_list))
print('Promedio de peso por viaje: ', sum(pesos_list)/len(pesos_list))