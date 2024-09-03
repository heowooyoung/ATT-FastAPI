import os
import sys

from chatbot_feedback.repository.chatbot_feedback_repository_impl import ChatbotFeedbackRepositoryImpl
from chatbot_feedback.service.chatbot_feedback_service import ChatbotFeedbackService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter


class ChatbotFeedbackServiceImpl(ChatbotFeedbackService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__chatbotFeedbackRepository = ChatbotFeedbackRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def requestChatbotFeedback(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__chatbotFeedbackRepository.getResult(userDefinedReceiverFastAPIChannel)