
#-----------------

#Las tulpas son colecciones ordenadas de elementos que no se pueden modificar
'''
-Ordenadas
-Inmutables
-Diferentes tipos de datos
-Mas rapidas que las listas
'''

''''''
#LAS TUPLAS USAN EL MISMO INDICE QUE LAS LISTAS

#A LAS TUPLAS NO SE LES PUEDE AÑADIR ELEMENTOS NUEVOS (CON POR EJEMPLO .APPEND)
''''''

#-----------------

lista = [1,2,3,"hola","buenas",True]
tupla = (4,5,6,"como","estas",False)
tupla2 = (7,8,9,"bien",True)

#Metodos Tuplas

tuple() #Crea una lista (o convierte una lista/set a tupla)

tupla_larga = tupla+tupla2 #Combina las dos tuplas en una sola

tupla_multiplicada = tupla*3 #Repite X veces el contenido de la lista

tupla.count(2) #Muestra cuantas veces se repite el elemento

tupla.index(4) #Muestra la primera vez que aparece en indice

len(tupla) #Largo de la tupla

print(1 in tupla) #True o False si esta o no en la tupla

num1,num2,num3,nombre,booleano = tupla2 #Asignar claves a los elementos de la tupla (num1 == 7)

a = 5 
b = 10
a,b = b,a #intercambia el valor 


