
#================================================================================

#Que es

'''
Son estructuras de control que permite al programa tomar decisiones y ejecutar diferentes codigos segun una condicio logica sea verdadera o falsa
'''

#================================================================================

#Estructura completa

num = int(input("Ingrese edad: "))

if num < 0:
    print("Es negativo")
elif num > 0:
    print("Es positivo")
else:
    print("Es 0")

#================================================================================

#Ejemplos

#Definir edad

edad = int(input("Ingresa tu edad: "))
if edad < 13:
    print("Eres un niño")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

#imc

peso = float(input("Ingrese su peso: "))
altura = float(input("ingrese su altura: "))
imc = peso/(altura**2)
if imc < 18.5:
    print("Tienes peso bajo")
elif imc >= 18.5 and imc <=24.9:
    print("Tienes peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Tienes sobrePeso")
elif imc >= 30:
    print("Tienes obesidad")
else:
    print("Valor no valido")

#Login

user = "Theroderick"
pasword = "lamochilaXL"
usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

if user == usuario and pasword == contraseña:
    print(f"Acceso concedido. Bienvenido {user}")
elif user == usuario and pasword != contraseña:
    print("Contraseña incorrecta, intente nuevamente")
else:
    print("Acceso denegado")

#================================================================================