# class Time():

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

# flamengo = Time("Flamengo")
# vasco = Time("Vasco")

# print(flamengo)
# print(vasco)

def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

def add_repr(cls):
     cls.__repr__ = my_repr
     return cls

@add_repr
class Time():

    def __init__(self, name):
        self.name = name

@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

flamengo = Time("Flamengo")
vasco = Time("Vasco")

print(flamengo)
print(vasco)

marte = Planeta("marte")
print(marte)