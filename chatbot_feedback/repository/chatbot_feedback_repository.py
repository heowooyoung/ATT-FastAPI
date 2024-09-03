from abc import ABC, abstractmethod

class ChatbotFeedbackRepository(ABC):

    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass