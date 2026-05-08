'''
Abre el archivo nombre.txt (del ejercicio anterior)

Lee el nombre

Muestra "Hola [nombre]"
'''

with open("8_manejo_archivos/ejercicios_deep/0_nombres.txt","r") as name:
    nombre = name.read()
    print(f"hola {nombre}")