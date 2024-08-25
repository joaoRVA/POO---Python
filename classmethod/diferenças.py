# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.password = None
        self.user = None

    #  method - tem acesso a instância da classe
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    # classmethod -> tem acesso a classe em si

    @classmethod
    def create_with_auth(cls, user, password):
        conect = cls()
        conect.user = user
        conect.password = password
        return conect
    

    # staticmethod -> não tem acesso a classe e nem a instância, igual uma função comum
    @staticmethod
    def connection_log(msg):
        print("LOG:", msg)

c1 = Connection()
c1.set_user("Joao")
c1.set_password("1234")
print(c1.user)
print(c1.password)

c2 = Connection.create_with_auth("Joao", "1234")
print(c2.user, c2.password)

Connection.connection_log("esse é meu log.")