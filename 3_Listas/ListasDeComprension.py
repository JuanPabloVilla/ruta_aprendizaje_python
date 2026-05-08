#Las listas de comprension ofrecen una manera de crear nuevas listas apartir de iterables existentes, se combinan con bucles for y en ciertos casos con condicionales (if)

lista = [i+2 for i in range(5)]
print(lista)

print("")

#Lista de comprension para numeros pares
numeros = [1,2,3,4,5,6,7,8,9]
pares = [i for i in numeros if i % 2 == 0]
print(numeros)
print("")
print(pares)
print("")

