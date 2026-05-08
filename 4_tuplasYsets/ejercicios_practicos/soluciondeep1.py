# coordenadas.py
import math

print("=== SISTEMA DE COORDENADAS ===")

# Almacenar puntos
puntos = []

for i in range(5):
    print(f"\nPunto {i+1}:")
    x = float(input("  Coordenada X: "))
    y = float(input("  Coordenada Y: "))
    z = float(input("  Coordenada Z: "))
    
    punto = (x, y, z)
    puntos.append(punto)

print("\n=== ANÁLISIS DE PUNTOS ===")
for i, punto in enumerate(puntos, start=1):
    # Desempaquetado de tupla
    x, y, z = punto
    distancia = math.sqrt(x**2 + y**2 + z**2)
    print(f"Punto {i}: ({x}, {y}, {z}) - Distancia: {distancia:.2f}")

# Encontrar punto más cercano al origen
punto_mas_cercano = min(puntos, key=lambda p: math.sqrt(p[0]**2 + p[1]**2 + p[2]**2))
x, y, z = punto_mas_cercano
print(f"\nPunto más cercano al origen: ({x}, {y}, {z})")