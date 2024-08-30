import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from enfp_test.service.enfp_test_service_impl import EnfpTestServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

enfpTestRouter = APIRouter()

async def injectEnfpTestService() -> EnfpTestServiceImpl:
    return EnfpTestServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

# post라 적기
@enfpTestRouter.post('/enfp-test-result')
async def requestEnfpTestResult(enfpTestService: EnfpTestServiceImpl =
                                 Depends(injectEnfpTestService)):

    ColorPrinter.print_important_message("requestEnfpTestResult()")

    generatedEnfpTestResult = enfpTestService.requestEnfpTestResult()

    return JSONResponse(content=generatedEnfpTestResult, status_code=status.HTTP_200_OK)