'''
Pide al usuario su nombre

Guarda el nombre en un archivo nombre.txt

Muestra "Nombre guardado"
'''

nombre_usuario = input("Ingrese su nombre:\n")

with open("8_manejo_archivos/ejercicios_deep/0_nombres.txt","a") as nombre:
    nombre.write(f"{nombre_usuario} \n")
    print("Nombre Guardado")