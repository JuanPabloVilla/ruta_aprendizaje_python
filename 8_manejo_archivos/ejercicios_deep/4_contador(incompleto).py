'''
Crea un archivo visitas.txt que guarde un número

Cada vez que ejecutes el programa, suma 1

Muestra "Has ejecutado este programa X veces"
'''

archivo_vistas = "8_manejo_archivos/ejercicios_deep/0_visitas.txt"

try:
    with open(archivo_vistas,"r") as visits:
        contenido = int(visits.read())
except ValueError:
    contenido = 0

contenido+=1

with open(archivo_vistas,"w") as visits:
    visits.write(str(contenido))

print(f"Has ejecutado este programa {contenido} veces\n")

