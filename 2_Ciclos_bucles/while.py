
#================================================================================

#Que es

'''
Es una estructura de control repetitiva. Permite ejecutar un bloque de codigo varias veces mientras una condicion sea verdadera.
'''

#================================================================================

#Estructura completa

'''
# PLANTILLA WHILE - SIGUE ESTOS PASOS:

# PASO 1: ¿Qué variable controla el ciclo? INICIALÍZALA
variable_control = valor_inicial

# PASO 2: ¿Cuándo debe CONTINUAR el ciclo? ESCRIBE LA CONDICIÓN
while condicion_sobre_variable_control:
    
    # PASO 3: ¿Qué quieres hacer en cada repetición?
    # (Tu lógica aquí)
    
    # PASO 4: ¿Cómo CAMBIA la variable de control?
    # (Asegúrate que eventualmente la condición sea FALSA)
    variable_control = nuevo_valor

# PASO 5: ¿Qué pasa cuando termina el ciclo?
print("Ciclo terminado")
'''

'''
# A: VARIABLE DE CONTROL (inicializar)
numero = 0

# B: CONDICIÓN (cuándo continuar)
while numero < 3:
    
    # C: ACCIÓN (lo que quieres hacer)
    print(f"Número actual: {numero}")
    
    # D: ACTUALIZACIÓN (cómo cambia la variable)
    numero = numero + 1  # o numero += 1
'''

'''
# 1. INICIALIZACIÓN (antes del while)
contador = int(input("Ingrese numero entre 0 y 45: "))

# 2. CONDICIÓN (cuándo se ejecuta el ciclo)
while contador < 50:  # "Mientras contador sea menor que 5"
    
    # 3. CUERPO DEL CICLO (lo que se repite)
    print(f"Vuelta número: {contador}")
    
    # 4. ACTUALIZACIÓN (cómo cambia la condición)
    contador = contador+1# ¡IMPORTANTE! Sin esto, ciclo infinito

# 5. FUERA DEL CICLO (cuando la condición es falsa)
print("Ciclo terminado")
'''

#================================================================================

#Ejemplos

#Suma acumulativa

num = int(input("Ingrese un numero: "))
suma = 0
while num != 0:
    suma = suma+num
    print(f"el resultado de la suma es:", suma)
    num = int(input("Ingrese el siguiente numero: "))
print("Gracias por usar la calculadora")    

#Validacion de entrada

numero = -1 
while numero <=0:
    numero = int(input("Ingresa un numero positivo: "))
    if numero <= 0:
        print("Numero invalido. Intenta de nuevo")
print(f"has ingresado: {numero}")

#Terminar ciclo con break

x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("Fin del bucle")
    

#================================================================================