from abc import ABC, abstractmethod

class EnfpTestService(ABC):

    @abstractmethod
    def requestEnfpTestResult(self):
        pass