'''
Pide al usuario un número entero positivo n y calcula el factorial de n 
(ej: 5! = 5×4×3×2×1) usando un for.
'''

num = int(input("Ingrese un numero entero positivo: \n"))
factorial = 1
for i in range(1,num+1):
    factorial*=i
print(factorial)