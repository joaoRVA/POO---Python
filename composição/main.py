# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) 

    def listar_enderecos(self):
        print(self.nome)
        for e in self.enderecos:
            print(e.rua, e.numero)
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

pessoa1 = Pessoa("Joao")

pessoa1.inserir_endereco("Av. Brasil", 123)
pessoa1.inserir_endereco("jardim bangu", 3)

# end1 = Endereco("asd", 1)
# end2 = Endereco("aada", 2)

# pessoa1.inserir_endereco(end1.rua, end1.numero)
pessoa1.listar_enderecos()

        