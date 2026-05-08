'''
Crea una lista con 5 nombres

Usa random.choice() para elegir uno al azar

Usa random.shuffle() para mezclar la lista

Muestra ambos resultados
'''
import random

nombres = ["juan","felipe","alejandro","raul","esteban"]

lista_random = random.choice(nombres)

print(lista_random)

random.shuffle(nombres)

print(nombres)