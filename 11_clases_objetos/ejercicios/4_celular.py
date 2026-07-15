'''
Clase Celular con: marca, modelo, batería (0-100)

Método cargar(cantidad) que aumente la batería

Método usar(minutos) que consuma 1% por minuto

Método mostrar_bateria()

Crea un celular y simula usarlo y cargarlo
'''

class celular:
    def __init__(self, marca, modelo,bateria):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria

    def cargar(self, aumento):
        self.bateria += aumento
    
    def usoCelular(self, disminucion):
        self.bateria -= disminucion
    
    def mostrarBateria(self):
        print(self.bateria)
    
celular1 = celular("Tecno","Spark",60)

celular1.cargar(20)

celular1.mostrarBateria()

celular1.usoCelular(10)

celular1.mostrarBateria()