# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class pessoa:
    ...

p1 = pessoa() # criar uma instância

p1.nome = 'Joao'
p1.sobrenome = 'Rodrigues'

print(p1.nome, p1.sobrenome)

p2 = pessoa()

p2.nome = 'julia'
p2.sobrenome = 'Alvez'

print(p2.nome, p2.sobrenome)