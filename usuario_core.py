#Asignatura: usuario

# make_withdrawal (self, amount) : haz que este método disminuya el saldo del usuario en la cantidad especificada
# display_user_balance (self) : haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
# p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
# BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user

class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # agrega el método deposit 
    def hacer_deposito(self, amount):	# toma un argumento que es el monto del depósito
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        self.printlog(self.name)
        self.printlog(str(self.account_balance))
        return self.account_balance
        
    def hacer_retiro(self,amount):
        self.account_balance -= amount
        self.printlog(self.name)
        self.printlog(str(self.account_balance))

        return self.account_balance
    def muestra_saldo(self):
        s=(f"Usuario: {self.name}, Saldo: {self.account_balance}")
        self.printlog(s)
        return s
    
    def tranferencia(self,otro_usuario,cantidad):
        self.account_balance -= cantidad
        otro_usuario.account_balance += cantidad
        self.printlog(self.name)
        self.printlog(str(self.account_balance))
        self.printlog(otro_usuario.name)
        self.printlog(str(otro_usuario.account_balance))
        return (self.account_balance, otro_usuario.account_balance)
    
    def printlog(self,operacion):
        with open("log.txt","a") as log:
            log.write(operacion + "\n") 

# crea 3 instancias de User
#Cuando se crea la instancia no se pasa el self
jp = User("Juan Pablo", "jp12345@gmail.com")
mb = User("Maribel Astrid","maribel12345@gmail.com")
ib = User("Isabella Castillo", "icc12345@gmail.cl")

#Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
print("inicio")
jp.printlog("Inicio")
print(jp.muestra_saldo())
# jp.printlog(jp.muestra_saldo())

print("deposito1 ")
jp.printlog("deposito1")
jp.hacer_deposito(500)

print("deposito2 ")
jp.printlog("deposito2 ")
jp.hacer_deposito(100)
print("deposito3 ")
jp.printlog("deposito3 ")
jp.hacer_deposito(300)
print(jp.muestra_saldo())

print("retiro1")
jp.printlog("retiro1")
jp.hacer_retiro(300)
print(jp.muestra_saldo())
print("")
jp.printlog("")



#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
print("inicio")
mb.printlog("Inicio")
print(mb.muestra_saldo())
print("deposito1 ")
mb.printlog("deposito1")
mb.hacer_deposito(500)
print("deposito2 ")
mb.printlog("deposito2 ")

mb.hacer_deposito(100)
print(mb.muestra_saldo())
print("retiro1")
mb.printlog("retiro1")

mb.hacer_retiro(300)
print("retiro2")
mb.printlog("retiro2")
mb.hacer_retiro(100)
print(mb.muestra_saldo())
print("")
mb.printlog("")

#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
print("inicio")
ib.printlog("inicio")
print(ib.muestra_saldo())
print("deposito1 ")
ib.printlog("deposito1 ")
ib.hacer_deposito(2500)

print("retiro1")
ib.printlog("retiro1")
ib.hacer_retiro(310)
print("retiro2")
ib.printlog("retiro2")
ib.hacer_retiro(410)
print("retiro3")
ib.printlog("retiro3")
ib.hacer_retiro(580)
print(ib.muestra_saldo())
print("")
ib.printlog("")

#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario 
# y luego imprima los saldos de ambos usuarios
print(f"Transferencia {jp.name} a {ib.name} ----->")
jp.printlog(f"Transferencia {jp.name} a {ib.name} ----->")
jp.tranferencia(ib,500)
print(f"Saldo {jp.name}:{jp.account_balance} -",f"Saldo {ib.name}:{ib.account_balance}")
jp.printlog(str(f"Saldo {jp.name}:{jp.account_balance} -",f"Saldo {ib.name}:{ib.account_balance}"))

