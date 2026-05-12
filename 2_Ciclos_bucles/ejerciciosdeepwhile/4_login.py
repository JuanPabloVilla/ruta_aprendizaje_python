'''
Simula un login simple:

Usuario y contraseña predefinidos (admin / 1234).

El usuario tiene 3 intentos para ingresar ambos correctamente.

Si falla, se le informa y termina el programa.

Si acierta, muestra "Acceso concedido".
'''

usuario_correcto = "admin"
contrasena_correcta = "1234"
intentos = 3
acceso = False

while intentos > 0 and not acceso:
    user = input("Usuario: ")
    pwd = input("Contraseña: ")
    
    if user == usuario_correcto and pwd == contrasena_correcta:
        acceso = True
        print("✅ Acceso concedido")
    else:
        intentos -= 1
        if intentos > 0:
            print(f"❌ Falló. Te quedan {intentos} intentos.")
        else:
            print("❌ Agotaste tus intentos. Acceso denegado.")