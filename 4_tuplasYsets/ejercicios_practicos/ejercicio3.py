#Analizador de Texto Avanzado
'''
Pide un texto al usuario

Convierte a set para obtener palabras únicas

Muestra el número de palabras únicas
------------------------------------------------
Usa operaciones de conjuntos para:

Encontrar palabras que empiecen con vocal

Encontrar palabras que contengan más de 5 letras

Palabras comunes entre dos frases (segunda frase adicional)
'''

texto = input("Ingrese una frase: ").lower() #el usuario ingresa un texto
texto2 = input("Ingrese una segunda grase: ").lower()
texto_divido = texto.split() #hacemos que el texto se haga lista, separando cada valor entre espacio
texto_divido2 = texto2.split()
palabras_unicas = set(texto_divido)
palabras_unicas2 = set(texto_divido2) #convertimos la lista a set
contador = 0
contador2 = 0
for i in palabras_unicas:
    if i in texto_divido: #contamos la cantidad de palabras unicas
        contador += 1
print(f"el numero de palabras unicas es de: {contador}")

for i in palabras_unicas2:
    if i in texto_divido2: #contamos la cantidad de palabras unicas
        contador2 += 1
print(f"(Frase 2)el numero de palabras unicas es de: {contador2}")


vocales = "aeiouAEIOU"
cont_vocales = 0
cont_vocales2 = 0

palabra_vocal = []
for i in texto_divido:
    if i[0] in vocales:
        palabra_vocal.append(i)
        cont_vocales += 1
print(f"La cantidad de palabras que empiezan por vocal es de {cont_vocales} y son: {palabra_vocal}")

palabra_vocal2 = []
for i in texto_divido2:
    if i[0] in vocales:
        palabra_vocal2.append(i)
        cont_vocales2 += 1
print(f"(frase 2)La cantidad de palabras que empiezan por vocal es de {cont_vocales2} y son: {palabra_vocal2}")


palabras_largas = []
for i in palabras_unicas:
    if len(i) >= 5:
        palabras_largas.append(i)
print(f"las palabras con mas de 5 letras son: {palabras_largas}")

palabras_largas2 = []
for i in palabras_unicas2:
    if len(i) >= 5:
        palabras_largas2.append(i)
print(f"(Frase 2) las palabras con mas de 5 letras son: {palabras_largas2}")


print("Las palabras comunes en las dos frases son: ")
print(palabras_unicas & palabras_unicas2)