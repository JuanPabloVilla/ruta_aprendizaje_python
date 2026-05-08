# registro_estudiantes.py
import string

estudiantes = set()

def mostrar_menu():
    print("\n=== SISTEMA DE REGISTRO DE ESTUDIANTES ===")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Ver todos los estudiantes")
    print("4. Buscar estudiante")
    print("5. Ver estadísticas")
    print("6. Comparar con otro curso")
    print("7. Salir")

def agregar_estudiante():
    nombre = input("Nombre del estudiante: ").strip().title()
    if nombre in estudiantes:
        print(f"❌ {nombre} ya está registrado")
    else:
        estudiantes.add(nombre)
        print(f"✅ {nombre} registrado exitosamente")

def eliminar_estudiante():
    nombre = input("Nombre del estudiante a eliminar: ").strip().title()
    if nombre in estudiantes:
        estudiantes.remove(nombre)
        print(f"✅ {nombre} eliminado")
    else:
        print(f"❌ {nombre} no está registrado")

def ver_todos():
    if not estudiantes:
        print("No hay estudiantes registrados")
    else:
        print(f"\n=== ESTUDIANTES ({len(estudiantes)}) ===")
        for i, estudiante in enumerate(sorted(estudiantes), start=1):
            print(f"{i}. {estudiante}")

def buscar_estudiante():
    nombre = input("Nombre a buscar: ").strip().title()
    if nombre in estudiantes:
        print(f"✅ {nombre} está registrado")
    else:
        print(f"❌ {nombre} no está registrado")
        print(f"Sugerencias:")
        sugerencias = [e for e in estudiantes if nombre.lower() in e.lower()]
        if sugerencias:
            print(f"  ¿Quizás quisiste decir: {', '.join(sugerencias)}?")

def ver_estadisticas():
    if not estudiantes:
        print("No hay estudiantes para mostrar estadísticas")
        return
    
    print(f"\n=== ESTADÍSTICAS ===")
    print(f"Total de estudiantes: {len(estudiantes)}")
    
    # Estudiantes por letra inicial
    print("\nEstudiantes por letra inicial:")
    letras = {}
    for estudiante in estudiantes:
        letra = estudiante[0].upper()
        if letra in string.ascii_uppercase:
            letras[letra] = letras.get(letra, 0) + 1
    
    for letra in sorted(letras.keys()):
        print(f"  {letra}: {letras[letra]} estudiante(s)")
    
    # Longitud promedio de nombres
    longitud_promedio = sum(len(e) for e in estudiantes) / len(estudiantes)
    print(f"\nLongitud promedio de nombres: {longitud_promedio:.1f} caracteres")
    
    # Nombres más largos y más cortos
    mas_largo = max(estudiantes, key=len)
    mas_corto = min(estudiantes, key=len)
    print(f"Nombre más largo: {mas_largo} ({len(mas_largo)} letras)")
    print(f"Nombre más corto: {mas_corto} ({len(mas_corto)} letras)")

def comparar_cursos():
    print("\nIngresa los estudiantes del segundo curso:")
    otro_curso = set()
    
    while True:
        nombre = input("Nombre (o 'listo' para terminar): ").strip().title()
        if nombre.lower() == 'listo':
            break
        if nombre:
            otro_curso.add(nombre)
    
    if not otro_curso:
        print("No se ingresaron estudiantes")
        return
    
    print(f"\n=== COMPARACIÓN DE CURSOS ===")
    print(f"Curso actual: {len(estudiantes)} estudiantes")
    print(f"Otro curso: {len(otro_curso)} estudiantes")
    
    comunes = estudiantes & otro_curso
    solo_actual = estudiantes - otro_curso
    solo_otro = otro_curso - estudiantes
    total_unicos = estudiantes | otro_curso
    
    print(f"\nEstudiantes en común ({len(comunes)}):")
    print(f"  {', '.join(sorted(comunes)) if comunes else 'Ninguno'}")
    
    print(f"\nSolo en curso actual ({len(solo_actual)}):")
    print(f"  {', '.join(sorted(solo_actual)) if solo_actual else 'Ninguno'}")
    
    print(f"\nSolo en otro curso ({len(solo_otro)}):")
    print(f"  {', '.join(sorted(solo_otro)) if solo_otro else 'Ninguno'}")
    
    print(f"\nTotal estudiantes únicos: {len(total_unicos)}")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        eliminar_estudiante()
    elif opcion == "3":
        ver_todos()
    elif opcion == "4":
        buscar_estudiante()
    elif opcion == "5":
        ver_estadisticas()
    elif opcion == "6":
        comparar_cursos()
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("❌ Opción inválida")