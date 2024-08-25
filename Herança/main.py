class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def mostra_nome_classe(self):
        print("CLASSE PESSOA")
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
     def mostra_nome_classe(self):
        print("CLASSE CLIENTE") # tem prioridade
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Funcionario(Pessoa):
    ...


c1 = Cliente("João Vítor", "Rodrigues")

print(c1.nome, c1.sobrenome)
c1.mostra_nome_classe()

print()
f1 = Funcionario("Julia", "Gomez")

f1.mostra_nome_classe()
print(f1.nome, f1.sobrenome)

# help(Cliente)

# Method Resolution Order (MRO)
    # é a ordem que o python vai dar prioridade na execução