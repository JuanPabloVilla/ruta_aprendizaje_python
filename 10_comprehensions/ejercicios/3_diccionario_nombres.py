'''
Crea una lista de nombres: ["Juan", "Ana", "Carlos", "María"]

Usa dict comprehension para crear un diccionario donde la clave es el nombre y el valor es la longitud del nombre

Muestra el diccionario
'''

nombres = ["Juan","Ana","Carlos","Maria"]

diccionario = {i: len(i) for i in nombres}
print(diccionario)