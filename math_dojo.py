import unittest

class MathDojo:
    def __init__(self):
    	self.result = 0

    def add(self, num, *nums):
    	# tu código aquí
        print("Suma los argumentos")
        self.result += num
        for n in nums:
            self.result += n
        return self
    def resta(self, num, *nums):
    	# tu código aquí
        print("Resta los argumentos")
        self.result -= num
        for n in nums:
            self.result -= n
        return self

md = MathDojo()

class IsEvenTests(unittest.TestCase):
    # cada método en esta clase es una prueba que se ejecutará 
    def testSuma(self):
        print("Prueba Suma")
        self.assertEqual(md.add(2).add(2,5,1).resta(3,2).result, 5)
        # otra forma de escribir arriba es 
        
    def testResta(self):
        print("Prueba Resta")
        self.assertEqual(md.add(10).resta(1,2,2).resta(2,3).result, 0)
        # otra forma de escribir lo de arriba es
        
    #  cualquier tarea que desee ejecutar antes de ejecutar cualquier método anterior, colóquelas en el método setUp 
    def setUp(self):
        # agrega las tareas setUp 
        md.result = 0
        print(f"Ejecutando prueba con valor inicial = {md.result}")
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método
    def tearDown(self):
        # agrega las tareas tearDown 
        print("No se que se hace aqui")

if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas


# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).resta(3,2).result
print(x) # debe imprimir 5
y = md.resta(1,2,3).result
	
print(y) # -1
# corre cada uno de los metodos algunos mas veces y valida el resultado!