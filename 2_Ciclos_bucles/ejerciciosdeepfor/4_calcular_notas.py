'''
Crear un programa que reciba x cantidad de notas y calcule el promedio
'''

cantidad_notas = int(input("Ingrese la cantidad de notas que desea ingresar: "))
total = 0

for i in range(0, cantidad_notas):
    notas = float(input("Ingrese su nota: "))
    total+=notas
    print(total)
promedio = total/cantidad_notas
if promedio >= 3.0:
    print("Su promedio fue de: ",promedio, " Aprobo")
else:
    print("Reprobo")