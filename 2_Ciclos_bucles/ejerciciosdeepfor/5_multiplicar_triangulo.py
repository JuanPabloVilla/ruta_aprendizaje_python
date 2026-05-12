'''
Haz un programa que genere la tabla de multiplicar del 1 al 10, 
pero con un formato de triángulo numérico:
1
2   4
3   6   9
4   8   12  16
5   10  15  20  25
...
10  20  30  ... 100
'''

numero = 10

for i in range(1, numero+1):        
    for j in range(1, i+1):        
        print(i*j, end=" ")
    print()                          
