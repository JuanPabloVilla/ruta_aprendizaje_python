'''
Crea un diccionario con 3 estudiantes y sus calificaciones (lista de 3 notas)

Calcula y muestra el promedio de cada estudiante

Muestra el estudiante con el promedio más alto
'''

estudiantes = {"juan":[4.5,4.8,5.0],"ruperto":[3.0,3.7,4.0],"joakin":[2.0,5.0,3.5]}



promedio1 = sum(estudiantes.get("juan")) / len(estudiantes.get("juan"))
print(f"El promedio de Juan es: {promedio1}")

promedio2 = sum(estudiantes.get("ruperto")) / len(estudiantes.get("ruperto"))
print(f"El promedio de Ruperto es de: {promedio2}")

promedio3 = sum(estudiantes.get("joakin")) / len(estudiantes.get("joakin"))
print(f"El promedio de Joakin es de: {promedio3}")

if promedio1 >= promedio2 and promedio1 >= promedio3:
    print(f"El promedio mayor es el de Juan con {promedio1}")
elif promedio2 >= promedio1 and promedio2 >= promedio3:
    print(f"El promedio mayor es el de Ruperto con {promedio2}")
else:
    print(f"El promedio mayor es el de Joakin con {promedio3}")