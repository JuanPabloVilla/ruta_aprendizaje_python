'''
Crea una lista de 5 palabras

Usa list comprehension para crear una nueva lista solo con palabras de más de 4 letras

Muestra ambas listas
'''

palabras = ["Agropecuario","Pez","Python","Sion","silla"]

mayores = [i for i in palabras if len(i) > 4]
print(mayores)