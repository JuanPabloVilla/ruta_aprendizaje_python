#Pide al usuario 5 palabras, guárdalas en una lista y muéstralas en orden inverso.

#Con funcion reverse

palabras = []

for i in range(1,6):
    palabras.append(input("Ingrese una palabra: "))
palabras.reverse()
print(palabras)

#Sin funcion reverse

for i in range(1,6):
    palabras.append(input("Ingrese una palabra: "))
print(palabras[::-1])