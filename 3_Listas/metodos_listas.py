
#-----------------

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros2 = [9,8,7,6,5,4,3,2,1]

# Sintaxis: lista[inicio:fin:paso]
print(numeros[2:5])     # [2, 3, 4] (índices 2, 3, 4)
print(numeros[:4])      # [0, 1, 2, 3] (desde inicio hasta índice 3)
print(numeros[5:])      # [5, 6, 7, 8, 9] (desde índice 5 hasta final)
print(numeros[::2])     # [0, 2, 4, 6, 8] (todos, de 2 en 2)
print(numeros[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (invertida)
print(numeros[2:8:2])   # [2, 4, 6] (de 2 a 7, de 2 en 2)

#-----------------

#Metodos listas

print(len(numeros)) #Muestra el largo de la lista, tambien puede funcionar para rangos y en generla con objetos iterables

print(numeros+numeros2) #Concatena las dos listas mostrando una sola lista

print(numeros*3) #Multiplica el contenido de la lista 

print(2 in numeros) #True o False en caso de que exista en la lista

numeros.append(20) #añade un elemento al final de la lista

numeros.extend([3,15,"numeros"]) #añade mas de un elementos a la lista (es parecido a concatenar)

numeros.insert (2,99) #Antes de la coma selecciona el indice donde se añadira el numero que va despues de la coma

numeros.remove(1) #Eliminara el primer elemento que contenga el valor seleccionado 

numeros.pop() #eliminara el ultimo elemento de la lista 

numeros.pop(3) #elimina el elemento del indice seleccionado .pop(indice)

numeros.clear() #Vacia la lista

numeros.sort() #Ordena los elementos de forma ascendete

numeros.index(1) #Devuelve la posicion en la que esta el numero 

numeros_ordenados = sorted(numeros) #Mismo que sort pero en una nueva lista

numeros.reverse() #voltea el orden de la lista

numeros.count(1) #Muestra cuantas veces se repite un elemento

#-----------------