'''
Usa el módulo math para obtener π

Función area_circulo(radio) que retorne π * radio²

Función area_cuadrado(lado) que retorne lado²

Prueba ambas funciones
'''

import math

p = math.pi

def area_circulo(radio):
    return p * math.pow(radio,2)
def area_cuadrado(lado):
    return math.pow(lado,2)

print(area_circulo(30))

print(area_cuadrado(20))