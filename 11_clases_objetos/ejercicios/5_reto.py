'''
Clase CuentaBancaria con:

Atributos: titular, saldo (inicia en 0)

Métodos: depositar(), retirar(), mostrar_saldo()

Validaciones:

No depositar cantidades negativas o cero

No retirar más del saldo disponible

Crea 2 cuentas y realiza operaciones
'''


class cuentaBancaria:
    def __init__(self,titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, aumento):
        if aumento > 0:
            self.saldo += aumento
        else:
            print("No puede depositar cantidades inferiores a 1") 
  
    def retirar(self, disminucion):
        if disminucion <= self.saldo:
            self.saldo -= disminucion
        else:
            print("Saldo insuficiente")

    def mostrarSaldo(self):
        print(self.saldo)
        
cuenta1 = cuentaBancaria("Juan")
cuenta1.depositar(30)
cuenta1.retirar(15)

cuenta1.mostrarSaldo()

cuenta2 = cuentaBancaria("Pablo")
cuenta2.depositar(0)
cuenta2.retirar(10)

cuenta2.mostrarSaldo()