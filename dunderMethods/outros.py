class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self.x!r}, {self.y!r})'
    
    def __add__(self, other):
        ponto_x = self.x + other.x
        ponto_y = self.y + other.y
        return Ponto(ponto_x, ponto_y)
   
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
    
        return result_self > result_other
    
if __name__ == '__main__':
    p1 = Ponto(2, 4) # 6
    p2 = Ponto(5, 8) # 13
    p3 = p1 + p2
    print(p3)
    print("p1 é maior do que p2?", p1 > p2)
    print("p2 é maior do que p1?", p2 > p1)