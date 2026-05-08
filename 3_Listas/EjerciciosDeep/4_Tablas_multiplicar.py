#Ejercicio 4: Tabla de multiplicar completa
'''
1.Usa una lista anidada para almacenar todas las tablas del 1 al 10
2.Estructura: tablas [tabla][multiplicador]
3.Permite al usuario consultar cualquier tabla
4.muestra la tabla completa de forma ordenada
'''

tablas = [[0],[1,2,3,4,5,6,7,8,9,10],[2,4,6,8,10,12,14,16,18,20],[3,6,9,12,15,18,21,24,27,30],[4,8,12,16,20,24,28,32,36,40],[5,10,15,20,25,30,35,40,45,50],[6,12,18,24,30,36,42,48,54,60],[7,14,21,28,35,42,49,56,63,70],[8,16,24,32,40,48,56,64,72,80],[9,18,27,36,45,54,63,72,81,90],[10,20,30,40,50,60,70,80,90,100]]

while True:
    opcion = int(input("1. Mostrar tabla 2.Salir \n"))
    for i in tablas:
        if opcion == 1:
            numero_tabla = int(input("Seleccione la tabla que desea que desea por indice (1 al 10): "))
            if numero_tabla == 1:
                print(tablas[1])
            elif numero_tabla == 2:
                print(tablas[2])
            elif numero_tabla == 3:
                print(tablas[3])
            elif numero_tabla == 4:
                print(tablas[4])
            elif numero_tabla == 5:
                print(tablas[5])
            elif numero_tabla == 6:
                print(tablas[6])
            elif numero_tabla == 7:
                print(tablas[7])
            elif numero_tabla == 8:
                print(tablas[8])
            elif numero_tabla == 9:
                print(tablas[9])
            elif numero_tabla == 10:
                print(tablas[10])