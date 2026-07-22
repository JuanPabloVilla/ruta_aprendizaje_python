
#================================================================================

#Que es

'''
La relacion es una manera en la cual una CLASE "hijo" puede obtener atributos y metodos de otra CLASE "padre"

Esta relacion se basa en "es-un"

    -un Perro (clase hijo) es un ANIMAL (Clase padre)
    -Un Auto (clase hijo) es un vehiculo (clase padre)
    -un Estudiantes (Clase hijo) es una persona (Clase padre)
'''

#Estructura Base

# Clase padre (base)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer(self):
        print(f"{self.nombre} está comiendo")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# Clase hija (hereda de Animal)
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Usos
perro = Perro("Rex")
perro.comer()   # Heredado de Animal
perro.dormir()  # Heredado de Animal
perro.ladrar()  # Propio de Perro

#================================================================================

#Ejemplos

#Sobreescribir metodos de clase padre en una clase hijo

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Uso
animal = Animal("Animal")
perro = Perro("Rex")
gato = Gato("Michi")

animal.hacer_sonido()  # Sonido genérico
perro.hacer_sonido()   # Rex dice: ¡Guau!
gato.hacer_sonido()    # Michi dice: ¡Miau!

#Metodo para llamar al padre con Super()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamar al constructor del padre
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def presentarse(self):
        # Llamar al método del padre y agregar más
        super().presentarse()
        print(f"Estudio {self.carrera}")

# Uso
estudiante = Estudiante("Juan", 20, "Ingeniería")
estudiante.presentarse()
# Hola, soy Juan y tengo 20 años
# Estudio Ingeniería


#Herencia multiple. Una clase hijo puede tener mas de un padre

class Volador:
    def volar(self):
        print("Volando")

class Nadador:
    def nadar(self):
        print("Nadando")

class Pato(Volador, Nadador):
    def hacer_sonido(self):
        print("¡Cuac!")

# Uso
pato = Pato()
pato.volar()   # Volando
pato.nadar()   # Nadando
pato.hacer_sonido()  # ¡Cuac!


#Jerarquia entre clases. Segun el orden de escritura sera el orden en que se muestre

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        print(f"{self.marca} {self.modelo} arrancó")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    def tocar_bocina(self):
        print("¡Piiiiii!")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    
    def hacer_ruido(self):
        print("¡Rum rum!")

# Uso
auto = Auto("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR", 600)

auto.arrancar()        # Toyota Corolla arrancó
auto.tocar_bocina()    # ¡Piiiiii!
moto.arrancar()        # Honda CBR arrancó
moto.hacer_ruido()     # ¡Rum rum!


#================================================================================

#Polimorfismo

#Que es 

'''
Diferentes clases responden al mismo metodo de diferente manera, en este caso el metodo es "hacer_sonido" y cada animal tiene una respuesta diferente segun la clase
'''

#Ejemplo

# Mismo método, diferentes comportamientos
class Perro:
    def hacer_sonido(self):
        return "¡Guau!"

class Gato:
    def hacer_sonido(self):
        return "¡Miau!"

class Vaca:
    def hacer_sonido(self):
        return "¡Muu!"

# Función polimórfica
def escuchar_sonido(animal):
    print(animal.hacer_sonido())

# Uso
animales = [Perro(), Gato(), Vaca()]
for animal in animales:
    escuchar_sonido(animal)
# ¡Guau!
# ¡Miau!
# ¡Muu!

#================================================================================


#Metodos abstractos (Concepto)

class Forma:
    def area(self):
        # Método que debe ser implementado por las hijas
        raise NotImplementedError("Las clases hijas deben implementar area()")

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2

class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

# Uso
formas = [Circulo(5), Rectangulo(4, 6)]
for forma in formas:
    print(f"Área: {forma.area():.2f}")
# Área: 78.54
# Área: 24.00