# Crea una función que cuente cuántas vocales tiene un texto

def contador_vocales(texto):
    vocales = "aeiou"
    contador = 0
    for i in texto:
        if i in vocales:
            contador +=1
    return(f"El texto tiene {contador} vocales")

texto = input("Ingrese un texto: ")

print(contador_vocales(texto))
