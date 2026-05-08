# Crea una función que reciba un texto y un número, y devuelva el texto repetido esa cantidad de veces

def repetir(text, num1):
    return(text *num1)

texto = input("Ingresa una palabra: ")
contador = int(input("Ingrese el numero de veces que desea repetirla: "))

print(repetir(texto, contador))

