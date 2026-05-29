# Crea una función que reciba una lista de números y devuelva su promedio

numeros = [1,2,3,4,5]

def promedio(lista):
    if not lista:
        return(0)
    return sum(lista)/len(lista)

print(promedio(numeros))