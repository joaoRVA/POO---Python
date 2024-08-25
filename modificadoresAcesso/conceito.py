# Encapsulamento (modificadores de acesso: public, protected, private)

# Python NÃO TEM modificadores de acesso

# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses(heranças)
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Teste:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'
    
    def publico(self):
        self._protegido()
        self.__privado()
        return 'método público'
    
    def _protegido(self):
        print("método protegido")
        return 'método protegido'
    
    def __privado(self):
        print("método privado")
        return 'método privado'
    

t1 = Teste()
print(t1.publico())
# print(t1.__privado()) não da pra acessar fora da classe
print(t1._Teste__privado()) # teria que acessar dessa forma aqui, mas foi feito para nao ser utilizado fora do escopo da classe