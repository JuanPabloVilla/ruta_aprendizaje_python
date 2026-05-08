#Añade un contador a un objeto iterable (Datos que permiten recorrer sus elementos uno por uno)

#enumerate en un str
palabra = ("String")
for i, j in enumerate(palabra):
    print(f"{i}.{j}")

print("")

#Enumerate en una lista
lista = [4,6,7,23,5,4]
for i, j in enumerate(lista):
    print(f"Numero {i}: {j}")

print("")

#Enumerate en una lista tipo tupla
lista1 = ("a","b","c")
enum = list(enumerate(lista1))
print(enum)