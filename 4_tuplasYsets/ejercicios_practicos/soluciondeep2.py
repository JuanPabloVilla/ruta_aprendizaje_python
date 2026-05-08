# sin_duplicados.py
print("=== ELIMINADOR DE DUPLICADOS ===")

numeros_originales = []
numeros_unicos_set = set()

for i in range(15):
    while True:
        try:
            num = int(input(f"Ingresa el número #{i+1}: "))
            numeros_originales.append(num)
            numeros_unicos_set.add(num)
            break
        except ValueError:
            print("❌ Debes ingresar un número válido")

# Convertir set a lista ordenada
numeros_unicos_ordenados = sorted(numeros_unicos_set)

print(f"\n=== RESULTADOS ===")
print(f"Números originales: {numeros_originales}")
print(f"Cantidad total: {len(numeros_originales)}")
print(f"Números únicos: {numeros_unicos_ordenados}")
print(f"Cantidad de números únicos: {len(numeros_unicos_ordenados)}")
print(f"Números duplicados eliminados: {len(numeros_originales) - len(numeros_unicos_ordenados)}")