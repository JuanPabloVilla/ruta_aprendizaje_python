
#Ciclo For
'''
lista = [2,4,6,7,8,675,5,7564,]
for i in lista:
    print(i)
'''
'''
palabra = "python"
for letras in palabra:
    print(letras)
'''
'''
tuplas = 1,"hola",34
for tulp in tuplas:
    print(tulp)
'''
'''
persona = {"Nombre":"Juan","edad":"20","ciudad":"medellin"}

for clave in persona:
    print(clave)
'''
'''
for valor in persona.values():
    print(valor)
'''
'''
for clave, valor in persona.items():
    print(f"{clave}:{valor}")
'''
'''
lista = 1,2,3,4,5,6,7,8,9,10
for i in lista:
    print(i)
'''
'''
numeros = 1,2,3,4,5,6,7,8
suma = 0
for num in numeros:
    suma += num
print(suma)
'''
'''
palabra = "Hola mi nombre es juan tengo 20 y me gusta el banano"
palabra_minus = palabra.lower()
vocales = "aeiou"
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
print(f"Hay un total de {contador} vocales") 
'''
'''
numeros = [49,30,7]
for numero in numeros:
    print(f"\nTabla del {numero}")
    for elemento in range(1,11):
      print(f"{numero} * {elemento} = {numero*elemento}")
'''
'''
numeros = [8,4,7,9,2,5]
valor_mas_alto = numeros[0]
for numero in numeros:
    if numero > valor_mas_alto:
        valor_mas_alto = numero
print(f"El valor mas alto es {valor_mas_alto}")
'''
'''
#Imprime todos los numeros del 20 al 30
for i in range(20,31):
    print(i)
'''
#Dada la lista [5, 8, 12, 3, 9, 7], calcula e imprime el promedio de sus elementos.
'''
lista = [5, 8, 12, 3, 9, 7]
suma = 0
for i in lista:
    suma+=i
    print(suma)
    promedio = suma/i
print(f"El promedio de la lista es {promedio}")
'''
#Crea un programa que pida al usuario una palabra y cuente cuántas veces aparece cada vocal (a, e, i, o, u).
'''
palabra = input("Ingrese una palabra que contennga vocales (a e i o u): ")
palabra_minus = palabra.lower()
vocales = ("aeiou")
contador = 0
for i in palabra_minus:
    if i in vocales:
        contador+=1
print(f"La palabra tiene {contador} vocales")
'''
#Dada una lista de números, crea una nueva lista que contenga solo los números que son mayores que el número anterior en la lista original.Ejemplo: [3, 7, 2, 8, 5, 10] → [7, 8, 10]
'''
numeros = [3,5,3,8,6,10,2,1,3,1,6]
mayor = []
for i in range(1,len(numeros)):
    if numeros[i] > numeros[i-1]:
        mayor.append(numeros[i])
print(mayor)
'''
#Ejercicio 5: Crea un programa que imprima el siguiente patrón:
'''
1
22
333
4444
55555
'''
'''
for i in range(1,6):
    print(str(i)*i)
'''
#Ejercicio 6: Dada una lista de listas (matriz), calcula la suma de cada fila y guárdalas en una nueva lista.
'''
lista = [[1,2,3], [4,5,6], [7,8,9]]
suma = 0
for i in lista:
    for j in i:
        suma += j
    print(suma)
'''
'''
while True:
    pregunta = input("Estas bien?: ")
    pregunta_low = pregunta.lower()
    if pregunta_low == "si":
        print("Me alegra que estes bien ahora mismo, era tu momento de estar mejor")
        break
    if pregunta_low == "no":
        print("No te te preocupes, esto pasara y todo estara bien")
    else:
        print("Al final todo estara bien, y si no esta bien es porque no es el final")
print("Fin")
'''
'''
cantidad_notas = int(input("Ingrese la cantidad de notas que desea ingresar: "))
contador = 0
suma = 0
for i in range(0,(cantidad_notas)):
    if contador < cantidad_notas:
        contador+=1
        nota = float(input("Ingrese la nota: "))
        suma+= nota
    promedio = suma/cantidad_notas
    print("-"*80)
if promedio >= 3.0:
    print(f"Tus notas dan {suma} y tu promedio total es de {promedio}, estas aprovado")
elif promedio < 3.0:
    print(f"Tus notas dan {suma} y tu promedio es de {promedio}, has reprobado")
print("-"*80)
'''
'''
altura = int(input("Digite la altura de la piramide: "))
for i in range(1,(altura+1)):
    for j in range(1, i+1):
        print(j, end="")
    print()
'''
'''
frase = input("escribe una frase cualquiera: ")
frase_minus = frase.lower()
vocales = ("aeiou")
contador = 0
for i in frase_minus:
    if i in vocales:
        contador+=1
print(f"Tu frase es: '{frase}' y tiene '{contador}' vocales")
'''
#Ejemplo sebas
'''
lista = "Hola sebas" #La lista en si misma es un elemento

for i in lista:
    print(i)
'''

cantidad_notas = int(input("Ingrese la cantidad de notas que desea ingresar: "))
total = 0

for i in range(0, cantidad_notas):
    notas = float(input("Ingrese su nota: "))
    total+=notas
    print(total)
promedio = total/cantidad_notas
if promedio >= 3.0:
    print("Su promedio fue de: ",promedio, " Aprobo")
else:
    print("Reprobo")