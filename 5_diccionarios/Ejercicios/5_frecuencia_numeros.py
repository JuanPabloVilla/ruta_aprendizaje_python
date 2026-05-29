'''
Genera una lista de 20 números aleatorios entre 1 y 10

Usa un diccionario para contar cuántas veces aparece cada número

Muestra la frecuencia de cada número

Muestra qué número aparece más veces
-----
# Pista: usa random.randint(1, 10) para números aleatorios
import random
'''

import random

lista = []
frecuencia = {}

for i in range(20):
    lista.append(random.randint(1,10))

#Pa la Frecuencia de numero

for i in lista:
    if i in frecuencia:
        frecuencia[i] += 1
    else:
        frecuencia[i] = 1

for i in frecuencia.items():
    print(i)


#Pa el numero con mas veces
mas_veces = None
repeticiones = 0

for i,j in frecuencia.items():
    if j > repeticiones:
        mas_veces = i
        repeticiones = j
print(f"Valor mas repetido: {mas_veces} con {repeticiones}")


'''
https://www.geeksforgeeks.org/python/python-count-dictionary-items/

https://es.stackoverflow.com/questions/601923/crear-un-diccionario-y-la-frecuencia-de-las-palabras

https://medium.com/data-science/3-ways-to-count-the-item-frequencies-in-a-python-list-89975f118899

https://docs.python.org/es/3/library/collections.html

https://www.askpython.com/python-modules/python-hashable-objects
'''