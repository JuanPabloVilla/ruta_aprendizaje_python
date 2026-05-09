'''
Pide al usuario su edad y muestra si es mayor de edad (18 o más) o menor de edad.
'''

#Solucion

edad = int(input("Ingrese su edad: \n"))
if edad < 18:
    print("Es menor de edad")
else:
    print("Es mayor de edad")