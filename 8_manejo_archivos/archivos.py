
#================================================================================

#nombre.txt sera una referencia

#Abrir archivos

archivo = open('nombre.txt','r') #Abrira el archivo (ver modo abajo)
archivo.close() #cerrara el archivo

#modos
'''
"r" #Read - solo lectura
"r+" #Leer y escribir
"w" #sobreescribe
"a" #agregar al final 
"x" #crear (solo si no existe)
'''

#================================================================================

#Escribir en archivos

#Modo "w" Sobreescribe todo

archivo = open('nombre.txt','w')
archivo.write("hola mundo\n")
archivo.write("Segunda linea\n")
archivo.close()

#Modo "a" agrega al final (sin borrar)

archivo = open('nombre.txt','a')
archivo.write("Esta linea se agrega al final")
archivo.close()

#================================================================================

#Leer archivos

#Leer todo el archivo

archivo = open('nombre.txt','r')
contenido = archivo.read()
print(contenido)
archivo.close()

#Leer linea por linea

archivo = open('nombre.txt','w')
for i in archivo:
    print(i.strip()) #Strip() quita el salto de linea
archivo.close()

#Leer todas las lineas en una lista

archivo = open('nombre.txt','r')
lineas = archivo.readlines() #Lista de lineas
print(lineas)
archivo.close()

#================================================================================

#bloque with (Abre y cierra automatica (sin necesidad del .close()))

with open('nombre.txt','w') as archivo:
    archivo.write("Esto es mas seguro\n")
    archivo.write("No olvido cerrrar el archivo\n")

#================================================================================

#Ejemplos

#Guardar lista 

compras = [1,2,3,4]

with open('nombre.txt','w') as archivo:
    for i in compras:
        archivo.write(f"{i}\n")

#leer y procesar datos

with open('nombre.txt','r') as archivo:
    for i in archivo:
        productos = i.strip()
        print(f"- {productos}")

#Contar lineas de un archivo

with open('nombres.txt','r') as archivo:
    lineas = archivo.readlines()
    print(f"El archivo tiene {len(lineas)} lineas")

#================================================================================

