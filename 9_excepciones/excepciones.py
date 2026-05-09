
#================================================================================

#Que es

'''
Son errores que ocurren durante la ejecucion del programa. Normamente python detiene el programa cuando esto ocurre, bloqueandolo y evitando que continue. Al usar try y except evitamos que se detenga el flujo y podemos mostrar un mensaje en consola para saber que error esta ocurriendo sin necesidad de terminar el programa.
'''

#Tipos (comando basicos para usar)

'''
ValueError - error en el valor (int("hola"))
ZeroDivisionError - Tratar de dividir por 0
NameError - El nombre de la variable, funcion o modulo no existe o no se reconoce 
TypeError - Sumar str con int
IndexError - indice de una lista, diccionario, etc esta fuera del rango de la misma
KeyError - clave de diccionario no encontrada
FileNotFoundError - archivo (open) no encontrado
'''
#================================================================================

#Estructura Base

try:
    numero = int(input("Ingrese un numero: \n"))
    print(f"El numero es: {numero}")
except:
    print("Error, valor no valido")


#================================================================================

#Ejemplos

#Capturar error especificos

try:
    numero2 = int(input("Ingrese un numero: \n"))
except ValueError:
    print("error de valor")

#Estructura completa try-excepto-else-finally

try:
    numero3 = int(input("Ingrese el numero: \n"))
    resultado = 10/numero
except ValueError:
    print("Error de valor")
except ZeroDivisionError:
    print("No dividir por 0")
else: 
    print(resultado)
finally:
    print("Fin del programa")

#Capturar multiples excepciones en una linea

try:
    num = int(input("Ingresa el numero: \n"))
    resultado = 10/num
except (ValueError, ZeroDivisionError) as er:
    print(f"error: {er}")

#Generar excepciones con raise

def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    elif edad <18:
        print("Menor de edad")
    else:
        return "Mayor de edad"
    
try:
    edad = int(input("Ingrese su edad: \n"))
    resultado = verificar_edad(edad)
except ValueError as e:
    print(f"Error: {e}")
else:
    print("resultado")

#================================================================================