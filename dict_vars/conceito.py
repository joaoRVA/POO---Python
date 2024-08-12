# __dict__ = é aonde os dados de uma classe estão salvos, é um dicionário {}
# vars = retorna o __dict__

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa("João", 21)

dados = {'nome': 'Lucas', 'idade': 34} # da pra fazer isso tbm
p2 = Pessoa(**dados) # desempacotar aqui

print(p1.__dict__)
print(vars(p1)) # vars() lê o __dict__

# também da pra escrever

p2.__dict__['altura'] = 1.70

print(vars(p2))