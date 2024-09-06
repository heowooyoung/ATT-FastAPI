from abc import ABC,abstractmethod

class QnaService(ABC):

    @abstractmethod
    def requestQnaResult(self):
        pass