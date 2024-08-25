# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):

class A:
    atributo_A = "A"

    def __init__(self, nome):
        self.nome = nome

    def metodo(self):
        print("Estou no A")
    
class B(A):
    atributo_B = "B"

    def __init__(self, nome, sobrenome):
        super().__init__(nome) # se eu quiser fazer outro init preciso usar o super
        self.sobrenome = sobrenome

    def metodo(self):
        print("Estou no B")

class C(B):
    atributo_C = "C"

    def __init__(self, idade, *args, **kwargs):
        print("ops, burlei o sistema")
        super().__init__(*args, **kwargs) # dessa forma ja pega tudo duma vez
        self.idade = idade


    def metodo(self):
        print("Estou no C")
        super().metodo() # super pega a classe a cima de acordo com o MRO - super = classe B
        super(B, self).metodo() # super = classe A

c1 = C(21, "João", "Rodrigues")

print(c1.nome, c1.sobrenome, c1.idade)

# c1.metodo()
# print(c1.atributo_A)
# print(c1.atributo_B)
# print(c1.atributo_C)