'''
Pide al usuario 3 contactos (nombre y teléfono)

Guarda cada contacto en una línea: "nombre,teléfono"

Usa el modo "a" para no sobrescribir
'''

lista = []

for i in range(3):
    nombre = input("Ingrese nombre de contacto\n")
    telefono = int(input("Ingrese el numero telefonico \n"))
    lista.append([nombre,telefono])

with open("8_manejo_archivos/ejercicios_deep/0_nombres.txt","a") as name:
    for i,j in lista:
        print(f"{i}: {j}")
        name.write(f"{i}: {j}\n")