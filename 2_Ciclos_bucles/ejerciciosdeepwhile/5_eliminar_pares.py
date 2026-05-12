'''
Pide un número entero positivo y construye otro número con solo los dígitos impares, manteniendo el orden original.
Ejemplo: 483921 → 391 (el 4, 8, 2 son pares y se eliminan).
'''

num = int(input("Ingresa un número entero positivo: "))
original = num
nuevo = 0
posicion = 1  # Para reconstruir el número en orden

# Primero invertimos el número para procesar dígito por dígito sin perder orden
while num > 0:
    digito = num % 10
    if digito % 2 != 0:  # es impar
        nuevo = nuevo + digito * posicion
        posicion *= 10
    num //= 10

print(f"El número original {original} sin dígitos pares es: {nuevo}")