'''
La computadora genera un número aleatorio entre 1-100

El usuario intenta adivinarlo

El programa da pistas: "Mayor" o "Menor"

Cuenta los intentos

si el intento supera los 5 intentos pierde

Usa while con break cuando adivine
'''

import random
numero_aleatorio = random.randint(1,100)
contador = 0
while True:
    intento = int(input("Ingrese el numero que crea correcto: "))
    if intento == numero_aleatorio:
        print(f"-"*50)
        print(f"Usaste {contador} intentos para advinar el numero, felicidades!!")
        break
    if intento < numero_aleatorio:
        print("El numero es mas alto, intenta otra vez")
    else:
        print("El numero es mas bajo, intenta otra vez")
    if intento != numero_aleatorio:
        contador += 1
    if contador == 5:
        print(f"-"*50)
        print("Gastaste todos los intentos.")
        break
print("-"*50)
