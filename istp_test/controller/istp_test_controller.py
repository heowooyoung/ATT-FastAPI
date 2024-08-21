import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from istp_test.service.istp_test_service_impl import IstpTestServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

istpTestRouter = APIRouter()

async def injectIstpTestService() -> IstpTestServiceImpl:
    return IstpTestServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@istpTestRouter.get('/istp-test-result')
async def requestIstpTestResult(istpTestService: IstpTestServiceImpl =
                                 Depends(injectIstpTestService)):

    ColorPrinter.print_important_message("requestIstpTestResult()")

    generatedIstpTestResult = istpTestService.requestIstpTestResult()

    return JSONResponse(content=generatedIstpTestResult, status_code=status.HTTP_200_OK)