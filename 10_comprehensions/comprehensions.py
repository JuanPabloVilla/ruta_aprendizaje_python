
#================================================================================

#Que es

'''
Las comprehensiones son formas compactas de crear listas en una sola linea
'''

#Estructura Base

cuadrados = [i ** 2 for i in range(5)]

#================================================================================

#comando basicos para usar

'''
Expresiones Lambda

-Son funcionaes anonimas (sin nombre) de una sola linea
'''
#Funcion lambda

suma_lambda = lambda a,b:a+b
print(suma_lambda(2,5))

#Con map()

numeros = [1,2,3,4,5]

resultado = list(map(lambda x:x**2,numeros))
print(resultado)

#Con filter()

#Pares
pares = list(filter(lambda x: x%2==0, numeros))
print(pares)

#mayores a 5
mayores = list(filter(lambda x: x > 5, numeros))
print(mayores)

#Con sorted()

personas = [
    {"nombre":"juan","edad":20},
    {"nombre":"Ana","edad":22},
    {"nombre":"Carlos","edad":19}
    ]

#por edad

edad = sorted(personas, key=lambda p: p["edad"])
print(edad)

#por nombre alfabetico

nombre = sorted(personas, key=lambda n: n["nombre"])
print(nombre)

#================================================================================

#Ejemplos

#Con condicion

pares = [i for i in range(10) if i % 2 == 0]
print(pares)

#Aplicar funciones

palabras = {"hola","mundo","python"}
mayusculas = [palabras.upper() for i in palabras]
print(mayusculas)

#Operador ternario

numeros = [1,2,3,4,5]
par_impar = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(par_impar)

#Diccionarios

#Crear diccionarios

cuadrados = {i: i ** 2 for i in range(5)}
print(cuadrados) 

#Filtrar diccionarios

edades = {"Juan": 20, "Ana": 22, "Carlos": 19, "María": 25}
mayores = {nombre: edad for nombre, edad in edades.items() if edad >= 20}
print(mayores)

#Sets

#Set de numeros pares (sin duplicados)

pares = {i for i in range(10) if i % 2 == 0}
print(pares)

#Letras unicas en palabras

palabras = ["hola", "mundo", "python"]
letras = {letra for palabra in palabras for letra in palabra}
print(letras)

#Comprehensiones anidadas

#Matriz 3x3

matriz = [[j for j in range(3)] for i in range(3)]
print(matriz)

#Aplanar Matriz

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [num for fila in matriz for num in fila]
print(aplanada)

