#Sistema de Registro de Estudiantes
'''
Usa un set para almacenar estudiantes inscritos

Menú: Agregar, Eliminar, Ver todos, Buscar, Ver estadísticas

Cada operación debe usar métodos de set

Muestra estadísticas: total, estudiantes que empiezan con cada letra

Permite operaciones entre conjuntos (intersección con otro curso)
'''

estudiantes = set()

while True:
    menu = int(input(" 1. Agregar \n 2. Eliminar \n 3. Ver Todos \n 4. Buscar \n 5. Estadisticas \n 0.Salir \n"))
    match menu:
        case 1:
            estudiantes.add(input("Escriba el nombre del estudiante: "))
        case 2:
            estudiantes.remove(input("Escriba el nombre del alumno que desea eliminar: "))
        case 3:
            print(estudiantes)
        case 4:
            estudiante_buscado = input("Ingrese el nombre del estudiante que desea buscar: ")
            if estudiante_buscado in estudiantes:
                print("El estudiante esta en la institucion")
            else:
                print("El estudiante no se encuentra en la institucion.")
        case 5:
            print("El total de estudiantes actuales es de ", len(estudiantes))
        case 0:
            print("Gracias por usar el sistema")
            break