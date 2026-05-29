'''
Crea un diccionario con 5 palabras en español y su traducción al inglés

Pide al usuario una palabra en español

Muestra su traducción si existe, o "Palabra no encontrada" si no
'''

diccionario_español = {"hola":"hello","amor":"love","arma":"gun","adios":"goodbye","odio":"hate"}

palabra_usuario = input("Ingresa una palabra\n")

if palabra_usuario in diccionario_español:
    print(diccionario_español[palabra_usuario])
else:
    print("palabra no disponible")

