'''
Genera un número aleatorio entre 1 y 20

Da al usuario 3 intentos para adivinarlo

Después de cada intento, da pistas ("más alto" o "más bajo")

Si adivina: "¡Ganaste!"

Si no: "Perdiste, el número era X"
'''

import random

numero_azar = random.randint(1,20)

intentos = 0

while intentos < 3:
    adivinar = int(input("Ingrese un numero del 1 al 20: \n"))
    if adivinar == numero_azar:
        print("Acertaste")
        break
    elif adivinar < numero_azar:
        print("El numero es mayor")
        intentos +=1
    elif adivinar > numero_azar:
        print("El numero es menor") 
        intentos +=1
    else:
        print("Opcion no valida")
    if intentos == 3:
        print("Demasiados intentos, fallaste.")