from abc import ABC, abstractmethod


class IstpTestRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass