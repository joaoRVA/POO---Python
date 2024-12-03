# Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.
# Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo.'
    
escritor = Escritor("João")
caneta = FerramentaDeEscrever("caneta bic")
maquina = FerramentaDeEscrever("máquina")
escritor.ferramenta = maquina # setando o valor de outro objeto nesse atributo

print(caneta.escrever())
print(maquina.escrever())
print(escritor.nome, escritor.ferramenta.escrever())