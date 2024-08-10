# Manter estados em uma classe

class Camera:

    def __init__(self, camera, filmando=False):
        self.camera = camera
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.camera} já está filmando!')
            return

        self.filmando = True
        print(f'{self.camera} começou a filmar')

    def parar_filmagem(self):
        if not self.filmando:
            print(f'{self.camera} NÃO está filmando...')
            return
        self.filmando = False
        print(f'{self.camera} parou de filmar')

    def fotografar(self):
        if self.filmando:
            print(f'{self.camera} está filmando, impossível fotografar.')
            return
        print(f'{self.camera} TIROU UMA FOTO')


c1 = Camera("Canon")
c2 = Camera("Sony")

c1.filmar()
c1.filmar()
c1.parar_filmagem()
c1.parar_filmagem()
c1.fotografar()
c1.fotografar()
c1.filmar()
c1.fotografar()

print()
c2.parar_filmagem()
c2.filmar()
c2.fotografar()
c2.parar_filmagem()
c2.fotografar()
