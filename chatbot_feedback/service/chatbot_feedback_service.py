from abc import ABC, abstractmethod

class ChatbotFeedbackService(ABC):

    @abstractmethod
    def requestChatbotFeedback(self):
        pass

    @abstractmethod
    def requestFinetuneWithFeedback(self):
        pass