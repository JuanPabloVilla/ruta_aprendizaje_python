#Crea una función que reciba una lista y devuelva una nueva lista sin elementos duplicados.

lista = []
for i in range (1,6):
    lista.append(int(input("Ingrese un numero: ")))

def eliminar_duplicado(lista_original):
    lista_sin_duplicado = []
    for i in lista_original:
        if i not in lista_sin_duplicado:
            lista_sin_duplicado.append(i)
    return(lista_sin_duplicado)

print(eliminar_duplicado(lista))

