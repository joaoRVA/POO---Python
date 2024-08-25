# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem UM ou MUITOS objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.

from Carrinho import Carrinho
from Produto import Produto

carrinho1 = Carrinho()
p1 = Produto("Maçã", 8.99)
p2 = Produto("Carne", 12.99)

carrinho1.inserir_produtos(p1, p2)

carrinho1.lista_produtos()

print("TOTAL: ", carrinho1.total())