'''
Dada la lista numeros = [3, 8, 1, 9, 4, 7, 2], 
encuentra e imprime el número más grande sin usar max(). Usa un for.
'''

lista = [3,8,1,9,4,7,2]

mayor = 0

for i in lista:
    if i > mayor:
        mayor = i
print(mayor)