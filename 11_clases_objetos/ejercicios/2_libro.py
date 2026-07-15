'''
Clase Libro con atributos: título, autor, páginas

Método mostrar_info() que muestre todos los datos

Método es_largo() que retorne True si tiene más de 300 páginas

Crea un libro y prueba
'''

class libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        print(f"titulo: {self.titulo} \nautor: {self.autor} \npaginas: {self.paginas}")

    def es_largo(self):
        if self.paginas >= 300:
            print(True)
        else:
            print(False)

libro1 = libro("Pinocho", "Carlo Collodi", 120)

libro1.mostrar_info()
libro1.es_largo()