#Sistema de coordenadas
'''
Crea una tupla coordenada con (x, y, z)

Pide al usuario 3 coordenadas

Calcula la distancia desde el origen (0,0,0): sqrt(x² + y² + z²)

Usa desempaquetado para asignar valores

Almacena 5 puntos en una lista de tuplas
'''

import math
#Solucion: 

coordenada = 0,0,0 #Definimos la tupla con (x,y,z)

#Le pedimos al usuario que ingrese 3 coordenadas
lista = []
for i in range (1,4):
    lista.append(float(input(f"Ingrese la coordenada {i}: "))**2) #Tambien elevamos las coordenadas dadas a la potencia de 2 para hacer la formula de distancia
lista1 = tuple(lista) #Transformamos la lista a tupla
listacoords = sum(lista1)

puntos_guardados = [(320,40,23),(10,49,20),(50,40,30),(8000,30,50),(20,305,90)]

print(f"la distancia es de: {math.sqrt(listacoords)} metros")



