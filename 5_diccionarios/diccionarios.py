
#================================================================================

#Que es

'''
Los diccionarios son colecciones de datos, no estan ordenados y son mutables. 
Los diccionarios cuentan con una clave-valor, cada elemento tiene una clave unica y un valor agregado a la clave.
'''

#================================================================================

#Estructura Base

diccionario = {"nombre":"juan","edad":20}

#================================================================================

#comando basicos para usar

'''
variable = dict(nombre="variable",tipo="diccionario") #Crear diccionario en variable

print(dict(tupla)) #convierte una tupla o lista a un diccionario

print(diccionario["nombre"]) #Accede a la clave. Si la clave no existe genera error

print(diccionario.get("altura")) #Accede a la clave sin generar error (none  o 0 por defecto)

diccionario["Ciudad"] = "medellin" #Agrega al diccionario una nueva clave con valor

diccionario["edad"] = 21 #Modifica el valor en caso de que la clave exista

diccionario.pop("edad") #elimina la clave seleccionada

diccionario.popitem() #Eliminar la ultima clave

del diccionario["nombre"] #Elimina por clave

diccionario.clear() #Vacia el diccionario

for i in diccionario.keys(): #Devuelve todas las claves
    print(i)

for i in diccionario.values(): #Devuelve todos los valores
    print(i)

for i,j in diccionario.items(): #Devuelve pares (clave, valor)
    print(f"{i}: {j}")

if "nombre" in diccionario: #Verificar existencia de clave
    print("La clave existe")

if "juan" in diccionario.values(): #Verificar existencia de valor
    print("El valor existe")
'''

#Diccionario anidados

'''
tarea = {"descripcion":{"Trabajo":"Esta es una tarea"},"status":{"Estado":False}} #Crear un diccionario anidado

tarea["status"]["Estado"] = True #Cambiar un dato anidado

print(tarea)
'''

#================================================================================

#Ejemplos

'''Ver Ejercicios'''