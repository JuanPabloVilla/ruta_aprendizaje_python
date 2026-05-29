'''
#Estrategia

-variable "palabra" para que el usuario ingrese por teclado
-usar un diccionario para contar cada letra
-mostrar el resultado

Ejemplo
Palabra: "python"
Resultado: {'p':1, 'y':1, 't':1, 'h':1, 'o':1, 'n':1}
'''

#solucion

#Un diccionario vacio para almacenar los datos
cuenta_letras = {}

#El usuario ingresa la palabra
palabra = input("Ingresa una palabra \n")

for i in palabra:
    if i in cuenta_letras:
        cuenta_letras[i]+=1
    else:
        cuenta_letras[i] = 1

print(cuenta_letras)