
'''
edad = int(input("Ingresa tu edad: "))
if edad < 13:
    print("Eres un niño")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
'''
'''
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
'''
'''
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
    '''
'''
num = int(input("Ingrese un numero del 1 al 7: "))
if num == 1:
    print("Lunes")
elif num == 2:
    print("Martes")
elif num == 3:
    print("Miercoles")
elif num == 4:
    print("Jueves")
elif num == 5:
    print("Viernes")
elif num == 6: 
    print("Sabado")
elif num == 7: 
    print("Domingo")
else:
    print("Numero no valido")
'''
'''
raiz = 0.5
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operacion = int(input("1.Suma 2.Resta 3.Multiplicacion 4.Division 5.Divison_Entera 6.Residuo 7.Potencia 8.Raiz_Cuadrada : "))
if operacion == 1:
    print(f"El resultado de la suma es: {num1+num2}")
elif operacion == 2:
    print(f"La resta es: {num1-num2}")
elif operacion == 3:
    print(f"La multiplicacion es: {num1*num2}")
elif operacion == 4:
    if num1 != 0 and num2 != 0:
        print(f"El resultado de la divison es: {num1/num2}")
    else:
        print("No se puede dividir por 0")
elif operacion == 5:
    if num1 != 0 and num2 != 0:
        print(f"La division entera es: {num1//num2}")
    else:
        print("No se puede dividir por 0")
elif operacion == 6:
    if num1 != 0 and num2 != 0:
        print(f"El residuo es: {num1%num2}")
    else:
        print("NO se puede dividir por 0")    
elif operacion == 7:
    print(f"La potencia es: {num1**num2}")
elif operacion == 8:
    print(f"La raiz cuadrada del primer numero es: {num1**raiz} y la del segundo es {num2**raiz}")
else:
    print("Operacion no valida")
'''