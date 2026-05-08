
#Los modulos son archivos .py que contienen funciones, variables y clases que puedes reutilizar

'''
-NO reinventas la rueda
-Organizas mejor tu codigo
-Accedes a funcionalidades avanzadas facilmente
'''

#forma 1: importar todo el modulo
import math
print(math.sqrt(25)) #Con sqrt se saca la raiz cuadrada

#Fomra 2: importar elmenetos en especifico
from math import sqrt
print(sqrt(80))

#Forma 3: importar con alias
import math as m #es como ponerle un nombre a el modulo 
print(m.sqrt(34))

#Forma 4: importar todo (NO recomendable)
from math import *
print(sqrt(69))

#================================================================================

#Metodos libreria math

import math

#Constantes
print(math.pi)
print(math.e)

#Funciones basicas

print(math.sqrt(25)) #Raiz cuadrada
print(math.pow(2,3))  #Potencia (El primer numero elevado a el segundo )
print(math.fabs(-5)) #Valor absoluto

#Redondeo
print(math.ceil(4.2)) #Redondeo arriba 
print(math.floor(4.8)) #Redondeo abajo

#Trigonometria
print(math.sin(math.pi/2)) #Investigar
print(math.degrees(math.pi)) #Investigar

#================================================================================

#Metodos libreria random

import random
lista = ["rojo","verde","azul"]

print(random.random()) #NUmero entre 0 y 1 (incluye decimales)
print(random.randint(1,10)) #numero entero entre un cierto rango
print(random.uniform(1,10)) #Numero decimal entre cierto rango
print(random.choice(lista)) #Escoge un elemento de una lista
random.shuffle(lista) #Mezcla los elementos de una lista
print(lista)

#================================================================================

#Metodos libreria datetime

import datetime

ahora = datetime.datetime.now() #fecha y hora actual
print(ahora) #actualidad completa
print(ahora.year) #año actual
print(ahora.month) #mes actual
print(ahora.day) #Dia actual

hoy = datetime.date.today() #Solo fecha actual
print(hoy)

fecha = datetime.date(2025,5,20) #Crear fecha especicifica
print(fecha)

#Diferencias entre fechas por dias

fecha1 = datetime.date(2025,1,1)
fecha2 = datetime.date(2025,12,31)
diferencia = fecha2 - fecha1
print(diferencia.days)

#================================================================================

#Metodo libreria OS

import os

print(os.getcwd()) #obtener directorio actual (ruta en la cual nos encontramos en los archivos)
print(os.listdir()) #Lista los archivos principales de la ruta actual

#os.mkdir("Nueva carpeta") #Crea una nueva carpeta que ocupa espacio en la ruta actual

if os.path.exists("README.MD"):
    print(True)

ruta = os.path.join("Mini_proyectos","Proyectos") #Unir rutas (no entiendo como funciona)

#================================================================================

#Metodos libreria sys

import sys

print(sys.version) #Version de python
print(sys.argv) #argumentos de linea de comando (no entendi como funciona)
sys.exit(0) #termina el programa actual
print(sys.path) #ruta de busqueda de modulo (tampoco entendi este)

