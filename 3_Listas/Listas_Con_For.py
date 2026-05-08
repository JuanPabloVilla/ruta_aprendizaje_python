#Recorer listas con el ciclo for

lista1 = [1,2,3,4,5,6,7]
for i in lista1:
    print(i)
    
#Recorrer lista con indice

lista2 = [1,2,3,4,5,6,7,8,9,1]
for i in range(len(lista2)):
    print(f"posicion {i}: {lista2[i]}")

print("")

lista3 = ["manzana",3,65,"uva","abominacion"]
for i in range(len(lista3)):
    print(f"posicion {i}: {lista3[i]}")

print("")

#Recorrer con funcion enumerate ()

lista4 = [1,2,3,4,5]
for i, list in enumerate(lista4):
    print(f"Orden {i}: {list}")

print("")

lista5 = ["Manzana", "Banano","Tomate"]
for i, list in enumerate(lista5):
    print(f"Orden {i}: {list}")

#Crear listas desde ciclos 

#Usando el metodo append() (esta seria la forma tradicional)
print("")


lista6 = []
for i in range(6):
    lista6.append(i ** 2)
print(lista6)

print("")

#con el metodo append() tambien podemos añadir elementos mas simples a listas con elementos

lista7 = ["manzana","mango","uva"]
lista7.append("tomate")
lista7.append(["madura","guayaba"])
print(lista7)

print("")

lista8 = []
for i in range(11):
    lista8.append(i*2)
print(lista8)

print("")

#Nuevamente creamos una lista desde una vacia
lista9 = []
for i in range(5):
    lista9.append(i**2)
    print(lista9)