'''
Usa datetime para obtener el año actual

Pide al usuario su año de nacimiento

Calcula y muestra su edad actual
'''

import datetime

años = datetime.datetime.now()

print(años.year)

edad = int(input("Ingrese su año de nacimiento: \n"))

calculo_edad = años.year - edad

print(f"tu edad es de {calculo_edad}")