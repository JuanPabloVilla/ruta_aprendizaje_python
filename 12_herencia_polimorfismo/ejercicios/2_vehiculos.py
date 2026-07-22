'''
Clase Vehiculo con marca, modelo y método mostrar_info()

Clase Auto que herede y agregue puertas

Clase Moto que herede y agregue cilindrada

Sobrescribe mostrar_info() en cada clase

Crea un auto y una moto
'''

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo}")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"puertas: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"cilindraje: {self.cilindrada}")

motito = Moto("Raider", 125, 124.8)
autito = Auto("BMW", "Competition", 4)

motito.mostrar_info()
autito.mostrar_info()