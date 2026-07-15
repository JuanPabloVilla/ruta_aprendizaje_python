'''
Clase Estudiante con: nombre, edad, lista de calificaciones

Método agregar_calificacion(nota)

Método promedio() que calcule el promedio

Método aprobo() que retorne True si promedio >= 3.0

Crea un estudiante y prueba
'''

class estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_calificaciones(self,nota):
        self.calificaciones.extend(nota)

    def promedio(self):
        resultado = 0
        for i in self.calificaciones:
            float(i)
            resultado += i
        return resultado / len(self.calificaciones)


    def apruebaOreprueba(self):
        promedio = self.promedio()
        if promedio >= 3.0:
            return "aprobada"
        else:
            return "reprobada"

    def informacionCompleta(self):
        promedio = self.promedio()
        aprobo = self.apruebaOreprueba()
        print(f"El estudiante {self.nombre} tiene un promedio de {promedio} y su asignatura esta {aprobo}")

estudiante1 = estudiante("Juan", 21)
estudiante1.agregar_calificaciones([4.6,4.9,4.8,5.0])

estudiante1.informacionCompleta()

