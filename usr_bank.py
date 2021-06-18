import logging
logging.basicConfig(filename='usr_bk_log.txt', filemode='a', format='%(message)s ---- %(asctime)s',datefmt='%d-%m-%Y %H:%M:%S')

# Actualiza el metodo __init__ de la clase User
#  Actualiza el metodo make_deposit de la clase User
#  Actualiza el metodo make_withdrawal de la clase User
#  Actualiza el metodo display_user_balance de la clase User
#  SENSEI BONUS: Permite al usuario tener varias cuentas; actualiza los metodos para que el usuario pueda especificar de cual cuenta ellos quieren depositar o retirar
#  BONUS 2: Modificar la función "transfer_money" de la clase User

class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(0.02,0) #se elimina el atributo saldo por un atributo Cuenta de la calse BankAccount
    # agrega el método deposit
    def abrir_cuenta(self):
        pass
    
    def hacer_deposito(self, cantidad):	# toma un argumento que es el monto del depósito
        self.cuenta.deposito(cantidad)	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        print(f"{self.name} - Deposito de: ${cantidad}")
        # self.printlog(str(self))
        self.printlog(f"{self.name} - Deposito de: ${cantidad}")
        return self

    def hacer_retiro(self,cantidad):
        if self.cuenta.saldo < cantidad:
            self.cuenta.saldo -= 5
            print(f"Operacion no realizada, saldo insuficiente cobrar una tarifa de $5 - Saldo restante:{self.cuenta.saldo} ")
            self.printlog(f"Operacion no realizada, saldo insuficiente cobrar una tarifa de $5 - Saldo restante:{self.cuenta.saldo}")
            return self
        self.cuenta.retiro(cantidad)
        print(f"{self.name} - Retiro de: ${cantidad}")
        self.printlog(f"{self.name} - Retiro de: ${cantidad}")
        return self

    def muestra_saldo(self):
        print(f"{self.name}",end=" - ")
        self.cuenta.informacion_cuenta()
        self.printlog(f"{self.name} - Saldo en cuenta: ${self.cuenta.saldo}")
        return 

    def tranferencia(self,otro_usuario,cantidad):
        print(f"Transferencia {self.name} a {otro_usuario.name} por -----> ${cantidad}")
        self.printlog(f"Transferencia {self.name} a {otro_usuario.name} por -----> ${cantidad}")
        
        self.cuenta.retiro(cantidad)
        otro_usuario.cuenta.deposito(cantidad)
        
        print(f"Saldo {self.name}:{self.cuenta.saldo} -", f"Saldo {otro_usuario.name}:{otro_usuario.cuenta.saldo}")
        self.printlog(f"Saldo {self.name}: ${self.cuenta.saldo} - Saldo {otro_usuario.name}: ${otro_usuario.cuenta.saldo}")
        return self

    def muestraintereses(self):
        if self.cuenta.saldo > 0:
            self.cuenta.intereses_ganados()
            print(f"{self.name} - Intereses ganados = {self.cuenta.saldo*self.cuenta.intereses}")
            self.printlog(f"{self.name} - Intereses ganados = {self.cuenta.saldo*self.cuenta.intereses}")
        return self

    def printlog(self,operacion):
        logging.warning(operacion)

class CuentaBancaria:
    def __init__(self, intereses=0.01, saldo=0):
        self.saldo=saldo
        self.intereses=intereses

    def deposito(self, cantidad):
        self.saldo += cantidad	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self

    def retiro(self, cantidad):
        # if self.saldo < cantidad:
        #     self.saldo -= 5
        #     print(f"Operacion no realizada, saldo insuficiente cobrar una tarifa de $5 - Saldo restante:{self.saldo} ")
        #     self.printlog(f"Operacion no realizada, saldo insuficiente cobrar una tarifa de $5 - Saldo restante:{self.saldo}")
        #     return self
        self.saldo -= cantidad
        return self
    
    def informacion_cuenta(self):
        print(f"Saldo en cuenta: ${self.saldo}")
        return self
    
    def intereses_ganados(self):
        self.saldo += self.saldo * self.intereses
        return self
    
    # def printlog(self,operacion):
    #     logging.warning(operacion)

# crea 3 instancias de User
#Cuando se crea la instancia no se pasa el self
jp = User("Juan Pablo", "jp12345@gmail.com")
mb = User("Maribel Astrid","maribel12345@gmail.com")
ib = User("Isabella Castillo", "icc12345@gmail.cl")

#funcion para imprimir en consola y guardar en log
def imprimelog(usuario_cuenta,mensaje):
    print(f"{usuario_cuenta.name} - {mensaje}")
    usuario_cuenta.printlog(f"{usuario_cuenta.name} - {mensaje}")

#Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
imprimelog(jp,"Inicio")
jp.muestra_saldo()

imprimelog(jp,"Deposito 1")
jp.hacer_deposito(500)

imprimelog(jp,"Deposito 2")
jp.hacer_deposito(100)

imprimelog(jp,"Deposito 3")
jp.hacer_deposito(300)
jp.muestra_saldo()

imprimelog(jp,"Retiro 1")
jp.hacer_retiro(2500)
jp.muestra_saldo()
print("Cambio de usuario")
jp.printlog("Cambio de usuario")

#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
imprimelog(mb,"Inicio")
mb.muestra_saldo()

imprimelog(mb,"Deposito 1")
mb.hacer_deposito(500)

imprimelog(mb,"Deposito 2")
mb.hacer_deposito(100)
mb.muestra_saldo()

imprimelog(mb,"Retiro 1")
mb.hacer_retiro(300)

imprimelog(mb,"Retiro 2")
mb.hacer_retiro(100)
mb.muestra_saldo()
print("Cambio de usuario")
jp.printlog("Cambio de usuario")

#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
imprimelog(ib,"Inicio")
ib.muestra_saldo()

imprimelog(ib,"Deposito 1")
ib.hacer_deposito(2500)

imprimelog(ib,"Retiro 1")
ib.hacer_retiro(310)

imprimelog(ib,"Retiro 2")
ib.hacer_retiro(410)

imprimelog(ib,"Retiro 3")
ib.hacer_retiro(580)
ib.muestra_saldo()
print("Cambio de usuario")
jp.printlog("Cambio de usuario")

#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario
# y luego imprima los saldos de ambos usuarios
# print(f"Transferencia {jp.name} a {ib.name} ----->")
# jp.printlog(f"Transferencia {jp.name} a {ib.name} ----->")
jp.tranferencia(ib,500)


jp.hacer_deposito(200).hacer_deposito(100).hacer_retiro(80).muestraintereses().muestra_saldo()
mb.hacer_deposito(200).hacer_deposito(100).hacer_retiro(80).hacer_retiro(80).hacer_retiro(20).hacer_retiro(80).muestraintereses().muestra_saldo()

logging.warning("Fin ejecucion ")