'''
Solicita un número entero e indica si es positivo, negativo o cero.
'''

numero=int(input("Ingrese un numero: \n"))
if numero > 0:
    print("Es positivo")
elif numero <0:
    print("Es negativo")
else:
    print("Es 0")