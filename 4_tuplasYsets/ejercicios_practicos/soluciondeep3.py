# analizador_avanzado.py
import string

print("=== ANALIZADOR DE TEXTO AVANZADO ===")

texto1 = input("Ingresa el primer texto: ").lower()
texto2 = input("Ingresa el segundo texto (para comparar): ").lower()

# Función para limpiar texto y obtener palabras
def obtener_palabras(texto):
    # Remover puntuación
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation))
    return set(texto_limpio.split())

palabras1 = obtener_palabras(texto1)
palabras2 = obtener_palabras(texto2)

# Palabras que empiezan con vocal
vocales = set('aeiou')
vocales_palabras = {p for p in palabras1 if p and p[0] in vocales}

# Palabras con más de 5 letras
palabras_largas = {p for p in palabras1 if len(p) > 5}

print(f"\n=== ANÁLISIS DEL PRIMER TEXTO ===")
print(f"Total de palabras únicas: {len(palabras1)}")
print(f"Palabras que empiezan con vocal ({len(vocales_palabras)}):")
print(f"  {', '.join(sorted(vocales_palabras))}")
print(f"\nPalabras con más de 5 letras ({len(palabras_largas)}):")
print(f"  {', '.join(sorted(palabras_largas))}")

print(f"\n=== COMPARACIÓN ENTRE TEXTOS ===")
print(f"Palabras en común: {palabras1 & palabras2}")
print(f"Palabras solo en primer texto: {palabras1 - palabras2}")
print(f"Palabras solo en segundo texto: {palabras2 - palabras1}")
print(f"Palabras únicas en total: {palabras1 | palabras2}")