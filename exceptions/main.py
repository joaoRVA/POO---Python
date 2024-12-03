# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Levantando e tratando suas Exceptions (Exceções)
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...


class AnotherError(Exception):
    ...

def RaiseException():
    exception_ = MyError("erro lançado")
    raise exception_

try:
    RaiseException()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)

    another_error = AnotherError("outro erro")
    raise another_error from error