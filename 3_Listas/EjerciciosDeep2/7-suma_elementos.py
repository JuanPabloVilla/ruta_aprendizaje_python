#Crea una lista con 5 números y calcula la suma de todos ellos (usa un bucle for).
#La forma estandar:

lista = [1,2,3,4,5]
suma = 0
for i in lista:
    suma+=i
print(suma)

#La forma en que yo lo haria
lista = []
suma = 0
for i in range(1,6):
    lista.append(int(input("Ingrese un numero: ")))
for i in lista:
    suma+=i
print(suma)

