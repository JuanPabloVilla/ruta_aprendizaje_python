# Crea una función que reciba dos números y devuelva el mayor de ellos

def mayor_que(num1, num2):
    if num1 > num2:
        return(f"{num1} es mayor")
    elif num2 > num1:
        return(f"{num2} es mayor")
    else:
        return("Los numeros son iguales")
    
print(mayor_que(3, 1))