'''
Pide al usuario un nombre de archivo

Intenta abrirlo y mostrar su contenido

Maneja FileNotFoundError

Usa finally para mostrar "Intento de lectura completado"
'''

try:
    archive_name = input("Ingrese el nombre del archivo que quiere buscar: \n")
    with open(archive_name+".txt","r") as archive:
        busqueda = archive.read()
        print("="*40)
        print(busqueda)
except (FileNotFoundError, FileExistsError) as error:
    print("="*40)
    print(f"Error: {error}")

