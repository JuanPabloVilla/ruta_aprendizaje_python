#Las matrices son estructuras con filas y columnas, tambien llamada listas anidadas; estas son fundamentales para el calculo y la manipulacion de datos.

#Esto es una matriz:
matriz1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print(matriz1) #Si usamos solo print normal, en consola se vera tal cual se ve en el codigo

print("")

#usando el ciclo for se recorre toda la lista y se mostrara por filas y columnas

for i in matriz1:
    print(i)

print("")

#De la siguiente manera podemos acceder a el elemento que queramos, el primer '[]' es para seleccionar la fila, mientras que el segundo '[]' es para definir de cual columna sacara la informacion. Debemos tener presente que sigue la misma estructura del indice, comienza en 0 hasta el final, en este caso vamos a la tercera fila y la segunda columna, con cual nos saltara '8' que es el numero que ocupa esta posicion

print(matriz1[2][1])
