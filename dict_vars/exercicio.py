import json

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
CAMINHO = "dict_vars\\dados.json"


p1 = Pessoa("Joao", 20)

# p1.__dict__['altura'] = 1.75

p2 = Pessoa("Lucas", 90)
arquivo = [vars(p1), vars(p2)]

with open(CAMINHO, "w", encoding="utf8") as dados:
    json.dump(arquivo, dados, indent=2, ensure_ascii=False)