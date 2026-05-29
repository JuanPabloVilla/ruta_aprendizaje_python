# Crea una función que reciba un número n y devuelva una lista con los números del 1 al n

def lista(n):
    new_list = [i for i in range(1,n+1)]
    return(new_list)

print(lista(30))

