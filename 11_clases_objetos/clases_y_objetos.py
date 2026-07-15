
#================================================================================

#Que es

'''
La programacion orientada a objetos o POO. Consiste en la generacion de codigo pensando en objetos, tales como vehiculos, tablas, botones, etc. Estos objetos pueden ser reutilizados a lo largo del codigo. Los conceptos se podrian dividir en

    -Clases
        Las clases se podrian describir como el concepto abstracto de un objeto, por ejemplo un vehiculo se entiende como, por ejemplo, un automovil con cuatro llantas, un manubrio, puertas y ventanas y demas factores. Este seria el concepto abstracto de el objeto, con lo cual seria una clase, esto se puede aplicar a un sinfin de areas, resalto principalmente botones, figuras geometricas, etc
    -Atributos
        Volvemos al caso del coche, tenemos el concepto abstracto, pero tenemos comprension de que el mismo automovil puede tener un diferente color, diferente tamaño, una placa que lo diferencia, una marca o un modulo y otra cantidad de caracteristicas que los diferencia con unos y los une con otros. Esto serian los atributos, las caracteristicas que hace que un objeto se separe de una clase como concepto abstracto y se pueda convertir en un objeto ya con caracteristicas.
    -Metodos
        Los automoviles tienen particuliaridades, se pueden encender, pueden mover sus ruedas para definir el camino que toman, puedan emitir ruido por medio de la bocina y otra cantidad de funciones que se puede realizar con el vehiculo. Esto serian los metodos, las funcionalidades o cosas que puede realizar dicho objeto
    -Objetos
        Una vez separados los terminos, se puede determinar que un objeto es un derivado de una clase que posee atributos y metodos especificos y que cada objeto puede llegar a tener diferencias entre si, incluso derivando de una misma clase.
'''

#Conceptos

'''
instancia = el objeto que se crea apartir de la clase 
__init__ = el metodo que inicializa la instancia creada apartir de la clase y ayuda a configurar los atributos, este se ejecuta de forma automatica al crear un objeto 
self = la instancia especifica de una clase, permite que cada objeto creado apartir de una clase posea sus propios atributos de forma independiente
'''

#Estructura base

class persona: #Creamos la clase
    def __init__(self,nombre,edad): #atributo base de la clase, las instancias tendran los suyos propios
        self.nombre = nombre  #atributo
        self.edad = edad #atributo

    def saludar(self): #La funcion que usaremos 
        print(f"hola soy {self.nombre} y tengo {self.edad} años")

juan = persona("juan",21) #Creacion de la instancia a base de la clase
juan.saludar() #uso de la funcion que creamos para usar  los atributos


#================================================================================

#Ejemplos

#Comparacion entre atributos de clase y atributos de instancia

class auto:
    cantidad_ruedas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

auto1 = auto("toyota", "Corrolla")
auto2= auto("honda","civic")

print(auto1.cantidad_ruedas) #atributo compartido por la clase
print(auto2.cantidad_ruedas)  

print(auto1.marca) #atributo de la instancia (unico)
print(auto2.marca)


#Mejor vistaso a los metodos y su uso

class Auto: #Generacion de la clase
    def __init__(self, marca, modelo): 
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
    
    def acelerar(self, incremento): #Metodo acelerar
        self.velocidad += incremento
        print(f"Auto Acelerando a {self.velocidad} km/h")
    
    def frenar(self, decremento): #metodo frenar
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"Auto Frenando a {self.velocidad} km/h")
    
    def mostrar_info(self): #metodo mostrar informacion
        print(f"Auto: {self.marca} {self.modelo}")
        print(f"Velocidad: {self.velocidad} km/h")

# Uso
mi_auto = Auto("Toyota", "Corolla")
mi_auto.acelerar(30)   # Acelerando a 30 km/h
mi_auto.frenar(10)     # Frenando a 20 km/h
mi_auto.mostrar_info()


#Uso de los metodos con return

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

r = Rectangulo(5, 3)
print(f"Área: {r.area()}")   
print(f"Perímetro: {r.perimetro()}")  

#Modificar parametros

class Banco:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (con __)
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"✅ Depósito de ${cantidad} realizado")
        else:
            print("❌ Cantidad inválida")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado")
        else:
            print("Fondos insuficientes")
    
    def consultar_saldo(self):
        print(f"Saldo: ${self.__saldo}")

# Uso
cuenta = Banco("Juan", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.consultar_saldo() 


#Metodo __str__ en metodos

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Persona: {self.nombre} ({self.edad} años)"

p = Persona("Juan", 20)
print(p) 

