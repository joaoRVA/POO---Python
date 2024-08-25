
class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produtos(self, *produtos):
        for p in produtos:
            self._produtos.append(p)
    
    def lista_produtos(self):
        for p in self._produtos:
            print(p.nome, p.preco)
        print()

    def total(self):
        return sum([p.preco for p in self._produtos])
    

