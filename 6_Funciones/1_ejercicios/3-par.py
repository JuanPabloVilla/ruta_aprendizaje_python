# Crea una función que reciba un número y devuelva True si es par, False si es impar

def par(numero):
    if numero % 2 == 0:
        return(True)
    else:
        return(False)
    
print(par(3))
print(par(20))
print(par(31))