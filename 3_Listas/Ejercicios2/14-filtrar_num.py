#De una lista de números, crea dos nuevas listas: una con los pares y otra con los impares.

numeros = []
for i in range(1,6):
    numeros.append(int(input("Ingrese un numero: ")))

pares = [i for i in numeros if i % 2 == 0]
impares = [i for i in numeros if i % 2 != 0]
print(pares)
print(impares)
