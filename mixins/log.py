# Abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class log:
    def _log(self, msg):
        raise NotImplementedError("Por favor, implemente o método log.")
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    

    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    

class logFileMixin(log):
    def _log(self, msg):
        mensagem = f"{msg} ({self.__class__.__name__})"
        print(f"Salvando mensagem no arquivo: '{mensagem}'")
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(mensagem)
            arquivo.write("\n")


class logPrintMixin(log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")
       



if __name__ == '__main__':

    l_print = logPrintMixin()
    l_print.log_error("deu erro")
    l_print.log_success("deu certo")
    
    l_file = logFileMixin()
    l_file.log_error("deu erro")
    l_file.log_success("deu certo")
