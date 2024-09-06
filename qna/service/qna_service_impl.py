import os
import sys

from qna.service.qna_service import QnaService
from qna.repository.qna_repository_impl import QnaRepositoryImpl

from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter
class QnaServiceImpl(QnaService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__qnaRepository = QnaRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository


    def requestIstpTestResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__qnaRepository.getResult(userDefinedReceiverFastAPIChannel)
