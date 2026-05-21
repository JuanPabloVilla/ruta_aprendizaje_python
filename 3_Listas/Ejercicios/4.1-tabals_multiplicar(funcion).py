#Ejercicio 4: Tabla de multiplicar completa
'''
1.Usa una lista anidada para almacenar todas las tablas del 1 al 10
2.Estructura: tablas [tabla][multiplicador]
3.Permite al usuario consultar cualquier tabla
4.muestra la tabla completa de forma ordenada
'''

def multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} X {i}:",numero*i)

multiplicar(int(input("Selecciona el numero del cual quieres ver la tabla: ")))



