'''
La computadora genera un número aleatorio entre 1-100

El usuario intenta adivinarlo

El programa da pistas: "Mayor" o "Menor"

Usa while con break cuando adivine
'''

import random

num_aleatorio = random.randint(1,100)

while True:
    adivinar = int(input("Ingrese el numero que cree que es: \n"))
    if adivinar == num_aleatorio:
        print(f"Felicidades, acertaste, el numero era: {num_aleatorio}")
        break
    if adivinar > num_aleatorio:
        print("El numero es menor")
    elif adivinar < num_aleatorio:
        print("EL numero es mayor")