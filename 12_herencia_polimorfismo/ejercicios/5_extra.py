'''
Clase Empleado con nombre, salario_base

Clase Vendedor que herede y tenga comisiones (5% de ventas)

Clase Programador que herede y tenga horas_extra (pago extra por hora)

Método calcular_salario() para cada uno

Crea lista de empleados y muestra el salario de todos
'''

class Empleado:
    def __init__(self,nombre,salario_base):
        self.nombre = nombre
        self.salario = salario_base

    def calcular_salario(self):
        return self.salario

class Vendedor(Empleado):
    def calcular_salario(self, comision):
        self.salario += comision*80000
        return self.salario

class Programador(Empleado):
    def calcular_salario(self, horas_extra):
        self.salario += horas_extra * 15000
        return self.salario

ElVendedor = Vendedor("Pablo",2800000)
ElVendedor.calcular_salario(10)
ElPrograma = Programador("Juan", 3800000)
ElPrograma.calcular_salario(5)

Empleados = [ElVendedor, ElPrograma]
for i in Empleados:
    print(f"{i.nombre}: ${i.salario}")