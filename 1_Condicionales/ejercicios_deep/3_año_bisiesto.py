'''
Pide un año y determina si es bisiesto.
Un año es bisiesto si:

Es divisible por 4, pero

Si es divisible por 100, también debe ser divisible por 400.
'''

año = int(input("Ingrese el año: \n"))

if año % 4==0:
    print("Es bisiesto")
else:
    print("no es bisiesto")