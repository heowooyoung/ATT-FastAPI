from abc import ABC, abstractmethod

class QnaRepositry(ABC):

    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass