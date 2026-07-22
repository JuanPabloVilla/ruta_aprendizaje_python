'''
Clase Animal con atributo nombre y método comer()

Clase Perro que herede de Animal con método ladrar()

Clase Gato que herede de Animal con método maullar()

Crea un perro y un gato y prueba sus métodos
'''

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print("Ñom Ñom")

class Perro(Animal):
    def ladrar(self):
        print("Guau Guau")

class Gato(Animal):
    def maullar(self):
        print("Miau Miau")

perrito = Perro("Max")
gatito = Gato("Mia")

perrito.ladrar()
gatito.maullar()