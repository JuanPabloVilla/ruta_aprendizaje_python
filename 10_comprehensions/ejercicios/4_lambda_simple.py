'''
Usa lambda para crear una función que reciba un número y retorne su cubo

Usa esa lambda con map() en una lista de números

Muestra el resultado
'''

numeros = [1,2,3,4,5]

cubo_lambda = lambda a:a**2

solucion = list(map(cubo_lambda, numeros))
print(solucion)