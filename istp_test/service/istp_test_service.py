from abc import ABC, abstractmethod

class IstpTestService(ABC):

    @abstractmethod
    def requestIstpTestResult(self):
        pass