
'''
#Estrategia

-Diccionario vacio "agenda"
-agregar 3 contactos
    -clave = nombre
    -valor = telefono
-mostrar el valor de una de las claves (el numero de un contacto)
-cambiar el valor de una de las claves (cambion el numero)
-eliminar un contacto
-mostrar todos los contactos
'''

#Solucion

#Variable. Diccionario vacio

agenda = {}

#añadimos 3 contactos al diccionario vacio "agenda"
agenda["juan"] = 123
agenda["luis"] = 456
agenda["jose"] = 789

#mostramos el valor de una clave
print(agenda["juan"])

#cambiamos un numero de una clave
agenda["jose"] = 301

#mostramos que se modifico el valor
print(agenda["jose"])

#Eliminamos uno de los contactos
del agenda["juan"]

#Mostramos la lista con todos los contacto (debido a que borarmos el contacto de "juan" este ya no saldra)
for i,j in agenda.items():
    print(f"{i}: {j}")