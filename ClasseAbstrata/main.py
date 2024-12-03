from abc import ABC, abstractmethod

# Uma classe abstrata não pode ser instanciada diretamente
# Deve ser herdada por outra classe

# class log(metaclass=ABCMeta): MESMA COISA

class log(ABC): # mas desse modo é melhor

    @abstractmethod # esse método DEVE ser implementado em todas as classes filhas
    def _log(self, msg): ...
        
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    

    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class logPrintMixin(log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")

l = logPrintMixin()
l.log_error("agora sim")