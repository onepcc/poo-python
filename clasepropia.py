
#combustible
#rendimieno

class Vehiculo:		
    def __init__(self, tipo,ruedas, color):
        self.tipo = tipo
        self.ruedas = ruedas
        self.color = color
        self.km = 0
    
    # agrega el método avanza
    def avance(self, cantidad = int):	# toma un argumento que es el monto del depósito
        self.km += cantidad * self.ruedas	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        print(f"{self.tipo} avanza {self.km} km")
        return self

    def retroceso(self, cantidad = int):
        self.km -= cantidad * self.ruedas
        print(f"{self.tipo} retrocede {self.km}")
        return self

    def competencia(self,otro_vehiculo,cantidad):
        self.km = cantidad*self.ruedas 
        otro_vehiculo.km = cantidad * otro_vehiculo.ruedas
        print(f"Compite {self.tipo} vs {otro_vehiculo.tipo} en {cantidad} km")
        if self.km> otro_vehiculo.km:
            print(f"Gana {self.tipo} {self.color}")
            return self
        elif self.km == otro_vehiculo.km:
            print("EMPATE")
        else:
            print(f"Gana {otro_vehiculo.tipo}")
            return otro_vehiculo


auto = Vehiculo("Automovil", 4, "rojo")
moto = Vehiculo("Motocicleta", 2, "azul")
bus = Vehiculo("Autobus", 8, "naranja")

auto.avance(10)


auto.competencia(bus,200)
moto.competencia(auto,100).competencia(bus,200)