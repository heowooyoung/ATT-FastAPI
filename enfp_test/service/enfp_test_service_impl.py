import os
import sys

from enfp_test.repository.enfp_test_repository_impl import EnfpTestRepositoryImpl
from enfp_test.service.enfp_test_service import EnfpTestService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class EnfpTestServiceImpl(EnfpTestService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__enfpTestRepository = EnfpTestRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository


    def requestEnfpTestResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__enfpTestRepository.getResult(userDefinedReceiverFastAPIChannel)