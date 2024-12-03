from log import logFileMixin, logPrintMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False
        
    def ligar(self):
        if not self._ligado:
            self._ligado = True

 
    
    def desligar(self):
        if self._ligado:
            self.ligado = False



class Smartphone(Eletronico, logFileMixin):
    def ligar(self):
       super().ligar()

       if self._ligado:
           msg = f"{self._nome} está ligado."
           self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f"{self._nome} está desligado."
            self.log_success(msg)