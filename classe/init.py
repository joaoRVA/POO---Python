class pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = pessoa("João", "Rodrigues") # criar uma instância

# p1.nome = 'Joao'
# p1.sobrenome = 'Rodrigues'

print(p1.nome, p1.sobrenome)

p2 = pessoa("Julia", "Alvez")

# p2.nome = 'julia'
# p2.sobrenome = 'Alvez'

print(p2.nome, p2.sobrenome)