#Encuentra el número más grande y el más pequeño en la lista [45, 23, 89, 12, 67, 34].

#================================================================================

#Numero mayor

#Con la funcion max
numero = [99,45, 23, 89, 12, 67, 34]
print(max(numero))

#Sin funcion
mayor = 0
for i in numero:
    if i > mayor:
        mayor=i
print(mayor)

#================================================================================

#Numero menor

#Sin funcion

menor = numero[0]
for i in numero:
    if i < menor:
        menor = i
print(menor)

#Con funcion

print(min(numero))