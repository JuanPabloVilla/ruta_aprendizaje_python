'''
Lista de números: [3, 7, 2, 9, 5, 8, 1, 6, 4]

Usa comprehensions para:

Crear lista de números pares

Crear lista de números al cuadrado

Crear lista de "par" o "impar" para cada número

Usa filter() con lambda para obtener números > 5

Muestra todos los resultados
'''

numeros = [3, 7, 2, 9, 5, 8, 1, 6, 4]
print(f"Lista original {numeros}")

pares = [i for i in numeros if i % 2 == 0]
print(f"Los pares son: {pares}")

cuadrados = [i ** 2 for i in numeros]
print(f"Los numeros al cuadrado son: {cuadrados}")

par_impar = ["par" if i % 2 == 0 else "impar" for i in numeros]
print(par_impar)


mayores = list(filter(lambda i: i > 5, numeros))
print(f"Numeros mayores que 5: {mayores}")
