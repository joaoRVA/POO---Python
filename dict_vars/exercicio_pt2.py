from exercicio import CAMINHO, Pessoa
import json


with open(CAMINHO, "r") as arquivo:
    dados = json.load(arquivo)
    p2 = Pessoa(**dados[1])
    p1 = Pessoa(**dados[0])
    print(p2.nome, p2.idade)
    print(p1.nome, p1.idade)