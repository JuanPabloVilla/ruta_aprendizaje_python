#Ejercicio 2: Estadisticas de Numeros
'''
1.Pide al usuario ingresar 10 numeros
2.Almacenalos en una lista
3.calcula: suma, promedio, maximo, minimo
4.Encuentra los numeros mayores al promedio
'''

numero = []
suma = 0
promedio = 0
maximo = 0
minimo = 1000000000000000000000
for i in range(1,11):
    numero_nuevo = int(input("Ingrese un numero: "))
    numero.append(numero_nuevo)
    for i in numero:
        if i > maximo:
            maximo=i
    for i in numero:
        if i < minimo:
            minimo=i
    print (numero)
    suma += numero_nuevo
    promedio = suma/10
print(f"La suma de los numeros es: {suma}, el promedio es de {promedio}. El numero mayor es {maximo} y el menor es {minimo}")

