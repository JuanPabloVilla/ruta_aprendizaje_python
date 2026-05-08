#Ejercicio 3: Buscador de Palabras
'''
1.Pide una frase al usuario
2.conviertela a lista de palabras
3.pide una palabra a buscar
4.muesta todas las posiciones donde aparece
5.Muestra estadisticas: veces que aparece, primera posicion, ultima posicion
'''


frase = input("Ingrese una frase: ")
frase_minus = frase.lower()
frase_lista = frase_minus.split()
palabra_a_buscar = input("Ingrese la palabra que quiere buscar: ")
contador = 0

for i in frase_lista:
    if palabra_a_buscar.lower() in i:
        contador += 1

print(f"la palabra aparece un total de: {contador} veces. La primera posicion en la que aparece es en: {frase_lista.index(palabra_a_buscar)}")
