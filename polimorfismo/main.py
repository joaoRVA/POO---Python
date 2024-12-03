from abc import ABC,abstractmethod


class notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...

class notificacaoSMS(notificacao):
    def enviar(self) -> bool:
        print("Enviando SMS: ", self.mensagem)
        return True

class notificacaoEmail(notificacao):
    def enviar(self) -> bool:
        print("Enviando E-mail: ", self.mensagem)
        return False
    
    
def enviarNotificacao(mensagem:notificacao):
    mensagem_enviada = mensagem.enviar()

    if mensagem_enviada:
        print("Mensagem foi enviada!")
    else:
        print("Mensagem NÃO foi enviada!")

enviarNotificacao(notificacaoSMS("oi, td bem?"))
enviarNotificacao(notificacaoEmail("olá, de boa?"))