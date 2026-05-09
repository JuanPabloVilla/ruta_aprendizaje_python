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