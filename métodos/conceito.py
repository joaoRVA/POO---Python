# métodos em instâncias de classes

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f"{self.nome} está acelerando...")

celta = Carro("celta")

print(celta.nome)

fusca = Carro("Fusca")
print(fusca.nome)

celta.acelerar()
fusca.acelerar()