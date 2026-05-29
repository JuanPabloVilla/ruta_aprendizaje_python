'''
Pide dos números al usuario

Intenta dividir el primero entre el segundo

Maneja ZeroDivisionError y ValueError

Muestra mensajes de error apropiados
'''

#Solución

try:
    num1 = int(input("Ingresa un numero: \n"))
    num2 = int(input("Ingresa un numero: \n"))
    resultado = num1/num2
except (ValueError, ZeroDivisionError) as er:
    print(f"error: {er}")
else:
    print(resultado)
finally:
    print("Fin del programa")