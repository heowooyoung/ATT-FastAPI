from abc import ABC, abstractmethod


class EnfpTestRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass