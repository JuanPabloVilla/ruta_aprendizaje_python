#================================================================================

#Que es

'''
Una coleccion de datos desordenada, nutable (que se puede modificar) y que no contiene elementos duplicados o repetidos. Los sets no garantizan que los elementos esten en orden pero no contiene duplicados y son rapidos en las busquedas.
'''

#================================================================================

#Estructura Base

set1 = {1,2,2,2,3,4,56,1}

#================================================================================

#comando basicos para usar

'''
set_vacio = set()  #Crear set vacio

lista1 = set([1,2,3,4]) #Crear set desde una lista

texto1 = set("programacion") #Crear set desde un str

set1.add(4) #añadir un elemento al set

set1.update([5,6,7]) #Agregar multiples elementos al set

set1.remove(4) #Se elimina el elemento seleccionado, si no existe genera un error

set.discard(10) #Elimina el elemento seleccionado sin generar error en caso de no existir

set1.pop() #Elimina un elemento aleatorio del set y lo imprime en la consola

set1.clear() #Vacia por completo el set


'''

'''

#OPERACIONES MATEMATICAS (conjuntos)
a = {1,2,3,4,5}
b = {4,5,6,7,8}

#Union: elementos en a o b
union = a | b
union = a.union(b)
print(union)

#intereseccion: elementos en ambos
inter = a & b 
inter = a.intersection(b)
print(inter)

#Diferencia: elementos en a pero no en b
diferencia = a - b
diferencia = a.difference(b)
print(diferencia)

#Diferencia simetrica: elementos en a o b pero no en ambos
dif_sim = a^b
dif_sim = a.symmetric_difference(b)
print(dif_sim)

#subconjunto: todos los elmentos de a estan en b?
print({1,2}.issubset(a))
print(a.issuperset({1,2}))

#Disjuntos: no tienen elementos en comun
print(a.isdisjoint({6,7}))
print(a.isdisjoint({4,5}))

'''

'''
#El frozen set se añadira al propios set

#Son la version inmutable de un set

fs = frozenset([1, 2, 3, 4, 5])

#Llave de diccionario
diccionario = {fs: "valor"}

#No se puede modificar 
#fs.add() #Genera un error en la consola

#Soporta operaciones de conjunto (comparacion con otro set)
fs2 = frozenset([4,5,6,7,8])
print(fs & fs2)
'''
#================================================================================

#Ejemplos


'''Ver ejercicios'''