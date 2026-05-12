
#================================================================================

#Que es

'''
Es una estructura de control repetitiva. Permite ejecutar un bloque de codigo varias veces. Se usa cuando sabes (o puedes calcular) cuantas veces se repetira
'''

#================================================================================

#Estructura Base

'''
for variable in secuencia:
    #Codigo a repetir

#Variable: Toma cada valor de la secuencia (las secuencias son valores tales como str, listas, etc. Valores iterables, es decir contables)

#Secuencia: puede ser un range(), lista, cadena, etc. (valores iterables)
'''

#================================================================================

#Ejemplos

#numero del 0 al 4

for i in range(5):
    print(i)

#Sumar numeros en un range

suma = 0
for i in range(1,11):
    suma+=i
print(suma)

#Recorrer una lista

lista = [1,2,3,4,5]

for i in lista:
    print(i)

#Recorrer string

palabra = "python"
for i in palabra:
    print(i)

#Terminar bucle con break

cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)

#================================================================================