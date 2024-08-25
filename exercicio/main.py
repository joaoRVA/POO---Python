# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabrica = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabrica(self):
        return self._fabrica
    
    @fabrica.setter
    def fabrica(self, fabrica):
        self._fabrica = fabrica

    

        
class Motor:
    def __init__(self, nome):
        self.nome = nome
    
    def exibir(self):
        return self.nome
    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome

    def exibir(self):
        return self.nome


carro1 = Carro("Civic")
motor1 = Motor("Turbo8000")
fabric1 = Fabricante("Honda")   

carro1.motor = motor1
carro1.fabrica = fabric1

print(carro1.fabrica.exibir(), carro1.nome, carro1.motor.exibir())

print()
carro2 = Carro("Celta")
motor2 = Motor("3.0")
fabric2 = Fabricante("Chevrolet")

carro2.motor = motor2
carro2.fabrica = fabric2

print(carro2.nome, carro2.fabrica.nome, carro2.motor.nome)