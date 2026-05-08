#Eliminador de Duplicados
'''
Pide al usuario ingresar 15 números

Usa un set para eliminar duplicados automáticamente

Muestra cuántos números únicos ingresó

Convierte el set a lista ordenada y muéstrala

Muestra los números originales y los únicos
'''

numeros = list()

for i in range(1,16):
    numeros.append(int(input(f"Ingrese el numero {i}: ")))
set1 = set(numeros)
lista1 = list(set1)
print(f"Los numeros originales son: {numeros}")
print(f"La lista con los numeros unicos es: {lista1}")





