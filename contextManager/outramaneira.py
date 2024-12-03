# Context Manager com função - Criando e Usando gerenciadores de contexto

from contextlib import contextmanager

@contextmanager
def my_open(caminho, modo):
    try:
        print("ABRINDO ARQUIVO")
        arquivo = open(caminho, modo, encoding="utf8")
        yield arquivo
    except Exception as e:
        print("Ocorreu um erro: ", e)
    finally:
        print("FECHANDO ARQUIVO")
        arquivo.close()
    
with my_open("contextManager/arq2.txt", 'w') as arquivo:
    arquivo.write("linha 1\n")
    arquivo.write("linha 2\n", 3)
    arquivo.write("linha 3\n")

