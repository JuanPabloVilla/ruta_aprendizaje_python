#Pide 10 números al usuario, guárdalos en una lista y muéstralos ordenados de menor a mayor.

numeros = []
for  i in range (1,11):
    numeros.append(int(input("Ingrese un numero: ")))
numeros.sort()
print(numeros)

