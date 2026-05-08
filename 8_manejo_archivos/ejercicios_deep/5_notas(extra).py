'''
Menú simple:
1. Agregar nota
2. Ver todas las notas
3. Salir
Al agregar nota, pide texto y guárdalo en notas.txt (cada nota en una línea)

Al ver notas, muestra todas las líneas numeradas

Usa with y modos apropiados ("a" para agregar, "r" para leer)
'''

menu = True

while menu == True:
    print("1. Agregar nota")
    print("2. Ver todas las notas")
    print("3. Salir")
    opcion = int(input(""))
    match opcion:
        case 1: 
            with open("8_manejo_archivos/ejercicios_deep/0_notas.txt","a") as notes:
                nota = input("Ingresa la nota que desea agregar:\n")
                notes.write(f"{nota}\n")
        case 2:
            with open("8_manejo_archivos/ejercicios_deep/0_notas.txt","r") as notes:
                lectura = notes.read()
                print(lectura)
        case 3:
            print("Gracias por usar el sistema")
            menu = False
            break       