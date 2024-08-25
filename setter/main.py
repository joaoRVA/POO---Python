# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe - > protected private

# setter -> serve para atribuir um valor ao getter, evita erros e problemas

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta1 = Caneta("Azul")
print(caneta1.cor)

caneta1.cor = "Rosa" # agora posso atribuir um valor diretamente daqui
print(caneta1.cor)

caneta1.cor_tampa = "preta"
print(caneta1.cor_tampa)