# factories - fábricas de criar objetos
# @classmethod - permite criar objeto sem instanciar um

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_conta_50_anos(cls, nome):
        return cls(nome, 50)
    
p1 = Pessoa.criar_conta_50_anos('Carimbo')

print(p1.nome, p1.idade)