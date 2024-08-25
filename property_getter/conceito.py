# getter - um método para obter um atributo
# cor -> get_cor()
# usado para proteger um atributo e não quebrar o código cliente

# @property - um getter no modo Pythônico
# modo pythônico - modo do Python de fazer coisas

# @property é uma propriedade do objeto.
  # -> ela é um método que se comporta como um atributo 🤯 🤯 🤯

# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# Código cliente - é o código que usa seu código



######## MODO CLÁSSICO GET ########
# class Caneta:
#     def __init__(self, nome, cor):
#         self.nome = nome
#         self.cor = cor

#     def get_nome(self):
#         return self.nome
    
#     def get_cor(self):
#         return self.cor
    

# c1 = Caneta("Bic", "Azul")
# print(c1.nome, c1.cor)

# print(c1.get_nome())
# print(c1.get_cor())
######## /MODO CLÁSSICO GET ########



class Caneta:
    def __init__(self, nome, cor):
        self.nome_caneta = nome
        self.cor_caneta = cor

    @property
    def name(self):
        return self.nome_caneta
    
    @property
    def cor(self):
        return self.cor_caneta
    
c1 = Caneta("Nankin", "preta")

print(c1.name) # agora o método aparece como atributo
print(c1.cor)