#Reto extra fuera de los ligeros
'''
1. Función calcular(a, b, operacion) donde:

Si operacion es "suma", retorna a + b

Si es "resta", retorna a - b

Si es "multiplica", retorna a * b

Si es "divide", retorna a / b (con validación)

Si es otra cosa, retorna "Operación no válida"

2. Prueba la función con todas las operaciones
'''

def calcular (a,b,operacion):
    match operacion:
        case "suma":
            return(a+b)
        case "resta":
            return(a-b)
        case "multiplica":
            return(a*b)
        case "divide":
            return(a/b)
        case _:
            return("Operacion no valida")
        
print(calcular(8,4,"suma"))
print(calcular(12,50,"resta"))
print(calcular(98,67,"multiplica"))
print(calcular(16,5,"divide"))
print(calcular(2,4,"hola"))