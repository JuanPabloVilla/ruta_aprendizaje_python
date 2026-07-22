'''
Clase Figura con método area() (que lance NotImplementedError)

Clase Cuadrado que herede y calcule área

Clase Triangulo que herede y calcule área

Crea una lista de figuras y calcula sus áreas
'''

class Figura:
    def __init__(self):
        pass

    def area(self):
        return NotImplementedError

class Cuadrado(Figura):
    def area(self, lado1, lado2):
        print(f"Area: {lado1*lado2}")

class Triagulo(Figura):
    def area(self, base, altura):
        print(f"Area: {(base*altura)/2}")

SeñorCuadrdado = Cuadrado()
SeñorTriangulo = Triagulo()

SeñorCuadrdado.area(7,7)
SeñorTriangulo.area(10,23)