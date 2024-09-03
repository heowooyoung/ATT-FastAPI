from abc import ABC, abstractmethod

class ChatbotFeedbackService(ABC):

    @abstractmethod
    def requestChatbotFeedback(self):
        pass