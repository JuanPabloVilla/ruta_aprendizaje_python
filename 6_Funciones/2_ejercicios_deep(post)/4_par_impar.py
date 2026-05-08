'''
Función es_par(numero) que retorne True si es par, False si es impar

Función es_impar(numero) que retorne lo opuesto

Prueba con varios números
'''

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def es_impar(numero):
    if numero % 2 != 0:
        return False
    else:
        return True
    
print(es_par(2))

print(es_impar(3))