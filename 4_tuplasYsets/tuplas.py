
#================================================================================

#Que es

'''
Son coleccion de datos (Como las listas) que no puede ser modificadas, es decir que no se les pueden añadir elmentos, eso las vuelve mas rapidas que las listas.
'''

#================================================================================

#Estructura Base

tupla1 = (4,5,6,"como","estas",False)
tupla2 = (7,8,9,"bien",True)

# Sintaxis: nombre_tupla[inicio:fin:paso]
print(tupla1[0])  
print(tupla1[2])   
print(tupla1[-1])   
print(tupla1[1:4]) 

#================================================================================

#comando basicos para usar

'''
tuple() #Crea una lista (o convierte una lista/set a tupla)

tupla_larga = tupla1+tupla2 #Combina las dos tuplas en una sola

tupla_multiplicada = tupla*3 #Repite X veces el contenido de la lista

tupla.count(2) #Muestra cuantas veces se repite el elemento

tupla.index(4) #Muestra la primera vez que aparece en indice

len(tupla) #Largo de la tupla

print(1 in tupla) #True o False si esta o no en la tupla

num1,num2,num3,nombre,booleano = tupla2 #Asignar claves a los elementos de la tupla (num1 == 7)

a = 5 
b = 10
a,b = b,a #intercambia el valor 

'''

#================================================================================

#Ejemplos

'''Mirar ejercicios tuplas'''