import logging
logging.basicConfig(filename='usr_bk_log.txt', filemode='a', format='%(message)s            ----           %(asctime)s',datefmt='%d-%m-%Y %H:%M:%S')

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
        self.cuentas = {"ahorros":self.cuenta }
    # agrega el método deposit
   
    def abrir_cuenta(self, nombre, intereses, saldo):
        self.nombre= CuentaBancaria(intereses, saldo)
        self.cuentas[nombre] = self.nombre 
        return self
    
    def hacer_deposito(self, cuenta,cantidad):	# toma un argumento que es el monto del depósito
        self.cuentas[cuenta].deposito(cantidad)	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        print(f"{self.name} - Deposito de: ${cantidad} - en cuenta {cuenta}")
        self.printlog(f"{self.name} - en cuenta {cuenta} -Deposito de: ${cantidad}")
        return self

    def hacer_retiro(self,cuenta,cantidad):
        if self.cuentas[cuenta].saldo < cantidad:
            self.cuentas[cuenta].saldo -= 5
            print(f"Operacion no realizada, saldo insuficiente cobrar una tarifa de $5 - Saldo restante en cuenta {cuenta}: {self.cuentas[cuenta].saldo} ")
            self.printlog(f"Operacion no realizada, saldo insuficiente cobrar una tarifa de $5 - Saldo restante en cuenta {cuenta}: {self.cuentas[cuenta].saldo}")
            return self
        self.cuentas[cuenta].retiro(cantidad)
        
        print(f"{self.name} - Retiro de: ${cantidad} - en cuenta {cuenta}")
        self.printlog(f"{self.name} - Retiro de: ${cantidad} - en cuenta {cuenta}")
        return self

    def tranferencia(self,cuenta,otro_usuario, otro_usuario_cuenta,cantidad):
        if self.cuentas[cuenta].saldo < cantidad:
            self.cuentas[cuenta].saldo -= 5
            print(f"Operacion no realizada, saldo insuficiente cobro tarifa de $5 - Saldo restante en cuenta {cuenta}: {self.cuentas[cuenta].saldo} ")
            self.printlog(f"Operacion no realizada, saldo insuficiente cobro tarifa de $5 - Saldo restante en cuenta {cuenta}: {self.cuentas[cuenta].saldo}")
            return self

        print(f"Transferencia de {self.name} cuenta {cuenta} a {otro_usuario.name} cuenta {otro_usuario_cuenta} por -----> ${cantidad}")
        self.printlog(f"Transferencia de {self.name} cuenta {cuenta} a {otro_usuario.name} cuenta {otro_usuario_cuenta} por -----> ${cantidad}")
        
        self.cuentas[cuenta].retiro(cantidad)
        otro_usuario.cuentas[otro_usuario_cuenta].deposito(cantidad)
        
        print(f"Saldo {self.name} cuenta {cuenta}:{self.cuentas[cuenta].saldo} -", f"Saldo {otro_usuario.name} cuenta {otro_usuario_cuenta}:{otro_usuario.cuentas[otro_usuario_cuenta].saldo}")
        self.printlog(f"Saldo {self.name} cuenta {cuenta}: ${self.cuentas[cuenta].saldo} - Saldo {otro_usuario.name} cuenta {otro_usuario_cuenta}: ${otro_usuario.cuentas[otro_usuario_cuenta].saldo}")
        return self

    def muestra_saldo(self):
        for cuenta, valor in self.cuentas.items():
            # print(f"{self.name}",end=" - ")
            # self.cuentas[cuenta].informacion_cuenta()
            print(f"""*****************************************************************
{self.name} - Saldo en cuenta {cuenta}: ${self.cuentas[cuenta].saldo}
*****************************************************************""")
            self.printlog(f"""*****************************************************************
{self.name} - Saldo en cuenta {cuenta}: ${self.cuentas[cuenta].saldo}
*****************************************************************""")
        return self

    def muestraintereses(self):
        for cuenta in self.cuentas:
            if self.cuentas[cuenta].saldo > 0:
                self.cuentas[cuenta].intereses_ganados()
                print(f"""*****************************************************************
                {self.name} - Intereses ganados en cuenta {cuenta} = $ {self.cuentas[cuenta].saldo*self.cuentas[cuenta].intereses}
                *****************************************************************""")
                self.printlog(f"""*****************************************************************
                {self.name} - Intereses ganados en cuenta {cuenta} = $ {self.cuentas[cuenta].saldo*self.cuentas[cuenta].intereses}
                *****************************************************************""")
            else:
                print(f"{self.name} - cuenta {cuenta} No gano intereses")
                self.printlog(f"{self.name} - cuenta {cuenta} No gano intereses")
        return self

    def printlog(self,operacion):
        logging.warning(operacion)

class CuentaBancaria:
    def __init__(self, intereses=0.01, saldo=0):
        self.saldo=saldo
        self.intereses=intereses

    def __str__(self):
        """ Informacion de cuenta """
        return f"Intereses: {self.intereses} Saldo: {self.saldo}" 

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
jp.abrir_cuenta("nomina",0.02,20)
jp.abrir_cuenta("vista",0.01,500)

for x, y in jp.cuentas.items():
  print(x, y,sep=": ")
# print(list(jp.cuentas))



mb = User("Maribel Astrid","maribel12345@gmail.com")
mb.abrir_cuenta("nomina",0.02,20)
mb.abrir_cuenta("vista",0.01,500)

ib = User("Isabella Castillo", "icc12345@gmail.cl")
ib.abrir_cuenta("vista",0.01,500)

#funcion para imprimir en consola y guardar en log
def imprimelog(usuario_cuenta,mensaje):
    "Imprime y loggea fuera de las clases"
    print(f"{usuario_cuenta.name} - {mensaje}")
    usuario_cuenta.printlog(f"{usuario_cuenta.name} - {mensaje}")

#Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
imprimelog(jp,"Inicio")
jp.muestra_saldo()

imprimelog(jp,"Deposito 1")
jp.hacer_deposito("nomina",500)
jp.hacer_deposito("vista",200)

imprimelog(jp,"Deposito 2")
jp.hacer_deposito("ahorros",100)

imprimelog(jp,"Deposito 3")
jp.hacer_deposito("vista",300)
jp.muestra_saldo()

imprimelog(jp,"Retiro 1")
jp.hacer_retiro("vista",250)
jp.hacer_retiro("nomina",650)
jp.hacer_retiro("ahorros",250)
jp.muestra_saldo()
print("Cambio de usuario")
jp.printlog("Cambio de usuario")

#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
imprimelog(mb,"Inicio")
mb.muestra_saldo()

imprimelog(mb,"Deposito 1")
mb.hacer_deposito("ahorros",500)
mb.hacer_deposito("nomina",50)
mb.hacer_deposito("vista",80)

imprimelog(mb,"Deposito 2")
mb.hacer_deposito("ahorros",100)
mb.hacer_deposito("nomina",100)
mb.hacer_deposito("vista",100)
mb.muestra_saldo()

imprimelog(mb,"Retiro 1")
mb.hacer_retiro("ahorros",300)
mb.hacer_retiro("nomina",300)
mb.hacer_retiro("vista",30)

imprimelog(mb,"Retiro 2")
mb.hacer_retiro("ahorros",100)
mb.hacer_retiro("nomina",1000)
mb.hacer_retiro("vista",200)
mb.muestra_saldo()
print("Cambio de usuario")
jp.printlog("Cambio de usuario")

#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
imprimelog(ib,"Inicio")
ib.muestra_saldo()

imprimelog(ib,"Deposito 1")
ib.hacer_deposito("ahorros",2500)
ib.hacer_deposito("vista",250)

imprimelog(ib,"Retiro 1")
ib.hacer_retiro("ahorros",310)

imprimelog(ib,"Retiro 2")
ib.hacer_retiro("vista",40)

imprimelog(ib,"Retiro 3")
ib.hacer_retiro("ahorros",580)
ib.muestra_saldo()
print("Cambio de usuario")
jp.printlog("Cambio de usuario")

#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario
# y luego imprima los saldos de ambos usuarios
# print(f"Transferencia {jp.name} a {ib.name} ----->")
# jp.printlog(f"Transferencia {jp.name} a {ib.name} ----->")
jp.tranferencia("ahorros",ib,"ahorros",500)


jp.hacer_deposito("nomina",200).hacer_deposito("nomina",100).hacer_retiro("nomina",80).muestraintereses().muestra_saldo()
mb.hacer_deposito("nomina",2000).tranferencia("nomina",ib,"ahorros",650).hacer_retiro("ahorros",80).hacer_retiro("nomina",800).hacer_retiro("vista",200).hacer_retiro("nomina",80).muestraintereses().muestra_saldo()

logging.warning("Fin ejecucion ")