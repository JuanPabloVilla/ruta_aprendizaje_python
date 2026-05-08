#La funcion len() devuelve la cantidad de caracteres que tiene un elemento, desde un str hasta una lista
'''    
#en str
palabra = "hola"
print(len(palabra))

#en lista
lista = [1,2,3,4,5]
print (len(lista))

#en tuplas
tupla = (10,20,30,40,50,60)
print(len(tupla))

#en diccionarios
diccionario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print(len(diccionario))

#longitud de una palabra dada por el usuario
palabra_user = input("Ingrese una palabra: ")
print(f"La palabra seleccionada es '{palabra_user}' y cuenta con {len(palabra_user)} caracateres")

#usar len() en condicionales
word1 = input("Type the first word: ")
word2 = input("Type the second word: ")

if len(word1) > len(word2):
    print(f"{word1} is longer than {word2}")
elif len(word1) < len(word2):
    print(f"{word2} is longer than {word1}")
else:
    print("both words have the same lenght")
'''    
#len() en ciclos for
   
#Para recorrer por indice
lista = ["Banano","Pera","Manzana","Tomate"]
for i in range(len(lista)):
    print(f"Indice {i}: {lista[i]}")
    
print("")

#Modificar los elementos de una lista
lista2 = [3,1,4,1,5,1,6]
for i in range(len(lista2)):
    lista2[i] = lista2[i]*2
print(lista2)

print("")

#Buscar un elemento y su posicion
lista3 = ["rojo","blanco","morado","azul","verde","negro","rosado","naranja"]
color_buscado = "morado"
for i in range(len(lista3)):
    if color_buscado == lista3[i]:
        print(f"Encontre '{color_buscado}' en la posicion {i}")

        
