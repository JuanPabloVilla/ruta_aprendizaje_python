'''
Crea un diccionario con 3 contactos

Pide al usuario una clave (nombre)

Muestra el teléfono si existe

Maneja KeyError si la clave no existe
'''

contactos = {"juan":123,"esteban":3456,"pepe":34353}

try:
    cont = input("ingresa el contacto: \n")
    print(contactos[cont])
except KeyError:
    print("Clave no existe")