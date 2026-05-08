#Son la version inmutable de un set

fs = frozenset([1, 2, 3, 4, 5])

#Llave de diccionario
diccionario = {fs: "valor"}

#No se puede modificar 
#fs.add() #Genera un error en la consola

#Soporta operaciones de conjunto (comparacion con otro set)
fs2 = frozenset([4,5,6,7,8])
print(fs & fs2)