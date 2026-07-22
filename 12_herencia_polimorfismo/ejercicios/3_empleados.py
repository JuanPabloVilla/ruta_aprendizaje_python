'''
Clase Empleado con nombre, salario_base

Clase Gerente que herede y agregue bonificacion (10%)

Clase Desarrollador que herede y agregue proyectos

Método calcular_salario() que en Gerente sea salario + bonificación

Crea un gerente y un desarrollador
'''

class empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario = salario_base
    def calcular_salario(self):
        print(self.salario)

class gerente(empleado):
    def __init__(self, nombre, salario_base, bonificacion):
        super().__init__(nombre, salario_base)
        self.bonificacion = bonificacion
    def calcular_salario(self):
        self.salario += self.bonificacion
        print(f"salario Gerente: {self.salario}")

class desarrollador(empleado):
    def __init__(self, nombre, salario_base, proyectos):
        super().__init__(nombre, salario_base)
        self.proyectos = proyectos
    def calcular_salario(self):
        self.salario += (self.proyectos * 200000)
        print(f"salario desarrollador: {self.salario}")

ElGerente = gerente("Manuel", 3800000, 700000)
ElDesarrollador = desarrollador("Juan", 2600000, 5)

ElGerente.calcular_salario()
ElDesarrollador.calcular_salario()