# Atributos em classes

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 2050 # prioridade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa("João", 21)
p2 = Pessoa("Lucas", 34)

print(p1.ano_nascimento())
print(p2.ano_nascimento())