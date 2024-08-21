import os
import sys

from istp_test.repository.istp_test_repository_impl import IstpTestRepositoryImpl
from istp_test.service.istp_test_service import IstpTestService

from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class IstpTestServiceImpl(IstpTestService):

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__istpTestRepository = IstpTestRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository


    def requestIstpTestResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__istpTestRepository.getResult(userDefinedReceiverFastAPIChannel)