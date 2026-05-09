'''
Crea una lista con 5 números

Pide al usuario un índice

Muestra el elemento en ese índice

Maneja IndexError si el índice no existe

Maneja ValueError si no ingresa un número
'''


try:
    numeros = [1,2,3,4,5,6]
    indice = int(input("Ingrese una posicion: \n"))
    print(numeros[indice])
except (ValueError, IndexError) as error:
    print(f"Error: {error}")