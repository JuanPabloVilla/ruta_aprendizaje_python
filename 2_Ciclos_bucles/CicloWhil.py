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
num = int(input("Ingrese un numero: "))
suma = 0
while num != 0:
    suma = suma+num
    print(f"el resultado de la suma es:", suma)
    num = int(input("Ingrese el siguiente numero: "))
print("Gracias por usar la calculadora")    
'''


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
✓ ¿INICIALICÉ todas las variables ANTES del while?

✓ ¿La CONDICIÓN eventualmente puede ser FALSA?

✓ ¿ACTUALIZO la variable de control DENTRO del ciclo?

✓ ¿Hay SALIDA (print) para ver qué está pasando?
'''
'''
import random
numero_aleatorio = random.randint(1,100)
contador = 0
while True:
    intento = int(input("Ingrese el numero que crea correcto: "))
    if intento == numero_aleatorio:
        print(f"-"*50)
        print(f"Usaste {contador} intentos para advinar el numero, felicidades!!")
        break
    if intento < numero_aleatorio:
        print("El numero es mas alto, intenta otra vez")
    else:
        print("El numero es mas bajo, intenta otra vez")
    if intento != numero_aleatorio:
        contador += 1
    if contador == 5:
        print(f"-"*50)
        print("Gastaste todos los intentos.")
        break
print("-"*50)
'''
      