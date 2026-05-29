'''
Función celsius_a_fahrenheit(celsius): retorna (celsius * 9/5) + 32

Función fahrenheit_a_celsius(fahrenheit): retorna (fahrenheit - 32) * 5/9

Prueba ambas funciones
'''

def celsius_a_fahrenheit(celsius):
    return (celsius*9/5) + 32

def fahrenheit_a_celsius(fahrenheit): 
    return (fahrenheit - 32) * 5/9

print(celsius_a_fahrenheit(200))

print(fahrenheit_a_celsius(120))