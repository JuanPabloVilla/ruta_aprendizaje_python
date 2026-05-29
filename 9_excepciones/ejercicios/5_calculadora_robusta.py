'''
Función dividir(a, b) que maneje división por cero

Función obtener_elemento(lista, indice) que maneje índices fuera de rango

Función leer_archivo(nombre) que maneje archivos no encontrados

Prueba cada función con casos que causen errores
'''

lista = [1,2,3,4,5,6,7,8]

def dividir(a,b):
    try:
        return a/b
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}")

def obtener_elementos(lista,indice):
    try:
        print(lista[indice])
    except IndexError:
        print("Excediendo el indice")

def leer_archivo(nombre):
    try:
        with open(nombre+".txt","r") as arch:
            leer = arch.read()
            print(leer)
    except (FileExistsError,FileNotFoundError) as error:
        print(f"error: {error}")

dividir (1,0)
obtener_elementos(lista,10)
leer_archivo("pepe")