#Calcula el producto punto de dos listas (vectores) de la misma longitud.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

if len(lista1) != len(lista2):
    print("Longitudes diferentes")
else:
    suma = 0
    for i in range(len(lista1)):
        suma += lista1[i] * lista2[i]
    print(f"El producto punto es: {suma}")