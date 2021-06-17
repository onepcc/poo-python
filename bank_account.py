# La clase también debe tener los siguientes métodos:

# deposit(self, cantidad) : aumenta el saldo de la cuenta en la cantidad dada
# withdraw(self, cantidad) : disminuye el saldo de la cuenta en la cantidad dada si hay fondos suficientes; si no hay suficiente dinero, imprima un mensaje "Fondos insuficientes: cobrar una tarifa de $ 5" y deduzca $ 5
# display_account_info(self) - imprime en la consola: ej. "Saldo: $ 100"
# yield_interest(self) : aumenta el saldo de la cuenta en el saldo actual * la tasa de interés (siempre que el saldo sea positivo)
		# tu código aqui

#  Crea una clase de BankAccount con los atributos tasa de interés y saldo
#  Agrega un método de depósito a la clase BankAccount
#  Agrega un método de retiro a la clase BankAccount
#  Agrega un método display_account_info a la clase BankAccount
#  Agrega un método yield_interest a la clase BankAccount
#  
# Crea 2 cuentas
#  En la primera cuenta, realice 3 depósitos y 1 retiro, luego calcule los intereses y muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)
#  En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)
import logging
logging.basicConfig(filename='cuenta.txt', filemode='a', format='%(message)s a las %(asctime)s',datefmt='%d-%m-%Y %H:%M:%S')
class CuentaBancaria:
    def __init__(self, intereses=0.01, saldo=0):
        self.saldo=saldo
        self.intereses=intereses

    def deposito(self, cantidad):
        self.saldo += cantidad	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        print(f"Deposito de: ${cantidad}")
        # self.printlog(str(self))
        self.printlog(f"Deposito de: ${cantidad}")
        return self

    def retiro(self, cantidad):
        if self.saldo < cantidad:
            self.saldo -= 5
            print(f"Operacion no realizada, saldo insuficiente cobrar una tarifa de $5 - Saldo restante:{self.saldo} ")
            self.printlog(f"Operacion no realizada, saldo insuficiente cobrar una tarifa de $5 - Saldo restante:{self.saldo}")
            return self
        self.saldo -= cantidad
        print(f"Retiro de: ${cantidad}")
        self.printlog(f"Retiro de: ${cantidad}")
        return self
    
    def informacion_cuenta(self):
        print(f"Saldo en cuenta: ${self.saldo}")
        self.printlog(f"Saldo en cuenta: ${self.saldo}")
        return self
    
    def intereses_ganados(self):
        if self.saldo > 0:
            self.saldo += self.saldo * self.intereses
            print(f"Intereses ganados = {self.saldo*self.intereses}")
            self.printlog(f"Intereses ganados = {self.saldo*self.intereses}")
        return self
    
    def printlog(self,operacion):
        logging.warning(operacion)

juan=CuentaBancaria()
pedro=CuentaBancaria()

juan.deposito(200).deposito(100).retiro(80).intereses_ganados().informacion_cuenta()
pedro.deposito(200).deposito(100).retiro(80).retiro(80).retiro(20).retiro(80).intereses_ganados().informacion_cuenta()
logging.warning("Fin ejecucion ")
