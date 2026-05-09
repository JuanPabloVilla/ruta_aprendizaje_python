'''
Dados tres lados (números positivos), determina si forman un triángulo y de qué tipo:

Equilátero (tres lados iguales)

Isósceles (dos lados iguales)

Escaleno (todos diferentes)
Si no es un triángulo válido (desigualdad triangular), muéstralo.
'''

lado1 = float(input("ingrese lado 1: \n"))
lado2 = float(input("ingrese lado 2: \n"))
lado3 = float(input("ingrese lado 3: \n"))

#Equilatero
if lado1 == lado2 and lado1 == lado3:
    print("equilatero")
#Isosceles
elif lado1 == lado2 and lado1 != lado3:
    print("Isosceles")
elif lado2 == lado3 and lado2 != lado1:
    print("Isosceles")
elif lado3 == lado1 and lado3 != lado2:
    print("Isosceles")
#Escaleno
elif lado1 != lado2 and lado1 != lado3:
    print("Escaleno")
