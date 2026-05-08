#Coleccion de datos desordenada, sin elementos duplicados y cambiable
'''
No ordenada
Mutable
Sin Duplicados
Rapidas para busquedas
'''

''''''

#CREACION DE SETS

#Set vacio
set_vacio = set() 

#Set con elementos
numeros = {1,2,3,4,5}
texto = {"rojo","verde","azul"}

#Elimina duplicados por defecto
set_dublicado = {1,2,2,2,3,4,56,1}
print(set_dublicado)

#Crear desde otros elementos contables (listas, str, )
lista = set([1,2,3,4])
texto2 = set("programacion")

print(lista)
print(texto2)

''''''

#OPERACIONES CON SETS

mineSet = {1,2,3}

#Agregar elementos (se usa el .add())
mineSet.add(4)
mineSet.add(8)

print(mineSet)

#Agregar elementos multiples (se usa el .update())
mineSet.update([5,6,7])

print(mineSet)

#Eliminar elementos (elimina el elemento seleccionado, genera error si no existe) (Se usa el .remove())
mineSet.remove(2)
print(mineSet)

#Mismo que el anterior, No genera error si no existe (Se usa el .discard())
mineSet.discard(10)
print(mineSet)

#Eliminar y obtener un elemento aleatorio (se usa el .pop())
mineSet.pop()
print(mineSet)

#Vacia un set
mineSet.clear()
print(mineSet)

''''''

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