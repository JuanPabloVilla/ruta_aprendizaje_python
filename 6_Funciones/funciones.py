
#================================================================================

#Que es

'''
Las funciones son bloques de codigo reutilizables que realizan una tarea en especifico. Con esto se evita repetir codigo, organizar mejor el codigo y facilitar la correcion de errores
'''

#================================================================================

#Estructura Base

def saludar(): #esta es la forma en la que se define una funciona
    print("Hola")

saludar() #Al usar la funcion nos devolvera el contenido de adentro de la misma

#================================================================================

#Ejemplos

#Funciones con parametros

def saludar_persona(nombre): #(nombre) es el parametro que usaremos.
    print(f"hola {nombre}")

saludar_persona("Juan") 

#Multiples parametros

def presentar(nombre,edad,ciudad):
    print(f"Soy {nombre}, tengo {edad} años y vivo en {ciudad}")

presentar("juan",21,"medellin")

#Funciones con retorno (return)

def suma(a,b):
    resultado = a+b
    return(resultado)

print(suma(2,2))

#Multiples return
def mayor(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"
    
print(mayor(21))

#Parametros con valor por defecto

def saludo(nombre, mensaje = "hola"):
    print(f"{mensaje} {nombre}")
saludo("Juan")


#Ambito de variables (Local y Global)

mensaje = "hello" #Variable global (fuera de la funcion)

def mostrar():
    local = "adentro" #Variable local (dentro de la funcion)
    print(mensaje)
    print(local)

mostrar()

#modificar una variable global

contador = 0

def incrimentar():
    global contador #"global" es palabra clave para modificar varibales globales
    contador += 1

incrimentar()
print(contador)
