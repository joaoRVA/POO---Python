# o metodo __repr__ serve para dizer aos outros devs como aquele objeto deve ser criado
# o metodo __str__ é mais informal, e serve para retornar uma string com os valores


class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __repr__(self) -> str:
        # class_name = self.__class__.__name__ mesma coisa
        class_name = type(self).__name__
        return f'{class_name}({self.x!r}, {self.y!r}, {self.z!r})'

p1 = Ponto(2, 4)
p2 = Ponto(44, 12)

print(f'{p1!r}') # dessa forma o repr é executado primeiro
print(p2) # o str é executado primeiro