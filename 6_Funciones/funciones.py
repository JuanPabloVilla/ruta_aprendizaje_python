
#Que son las funciones
'''
Bloques de codigo reutilizables que realizan una tarea en especifico 

-Evita repetir codigo
-Organizas mejor tu programa
-Facilita encontrar y corregir errores
-Puedes usar la misam funcion muchas veces
'''

#Definir y llamar funciones

def saludar(): #esta es la forma en la que se define una funciona
    print("Hola")

saludar() #Al usar la funcion nos devolvera el contenido de adentro de la misma

#==========================================================================================

#Funciones con parametros

def saludar_persona(nombre): #(nombre) es el parametro que usaremos.
    print(f"hola {nombre}")

saludar_persona("Juan") 

#Pueden ser multiples parametros

def presentar(nombre,edad,ciudad):
    print(f"Soy {nombre}, tengo {edad} años y vivo en {ciudad}")

presentar("juan",21,"medellin")

#==========================================================================================

#Funciones con retorno (return)

def suma(a,b):
    resultado = a+b
    return(resultado)

print(suma(2,2))

total = suma(8,3)
print(total)

#Multiples return
def mayor(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"
    
print(mayor(21))

#==========================================================================================

#Parametros con valor por defecto

def saludo(nombre, mensaje = "hola"):
    print(f"{mensaje} {nombre}")
saludo("Juansito")

#Ejemplo "real"

def calcular_precio(precio, impuesto=0.19):
    return precio * impuesto
print(calcular_precio(100))

#==========================================================================================

#Parametros nombrados

def presente(nombre,edad,ciudad):
    print(f"Soy {nombre}, tengo {edad} años y vivo en {ciudad}")

#normal

presente("juan",21,"medellin")

#Parametros normbrados

presente(nombre="Juan", ciudad = "medellin", edad=21) #Orden no importa

#==========================================================================================

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

#==========================================================================================

#Documentacion de funciones (Docstring)

def sumar(c,d):
    #(Texto de IA) la informacion que le demos entre "" sera la que diga en la documentacion
    """
    Suma dos números y devuelve el resultado.
    
    Parámetros:
    a (int/float): Primer número
    b (int/float): Segundo número
    
    Retorna:
    int/float: La suma de a y b
    """
    return c+d

#Para ver la documentacion
help(sumar)
print(sumar.__doc__)

#==========================================================================================
