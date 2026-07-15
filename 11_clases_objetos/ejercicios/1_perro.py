'''
Clase Perro con atributos: nombre, edad, raza

Método ladrar() que imprima "¡Guau!"

Método presentarse() que muestre nombre y edad

Crea 2 perros y prueba los métodos
'''

class perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print("guau!")

    def presentacion(self):
        print(f"mi perro se llama {self.nombre} y tiene {self.edad} años")

perro1 = perro("Max", 5, "Golden")
perro2 = perro("Paloma", 10, "Pibble")

perro1.ladrar()
perro1.presentacion()
perro2.presentacion()