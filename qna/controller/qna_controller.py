import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from qna.service.qna_service_impl import QnaServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

qnaRouter = APIRouter()

async def injectQnaService() -> QnaServiceImpl:
    return QnaServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

# post라 적기
@qnaRouter.post('/date-qna-result')
async def requestDateQnaResult(qnaService: QnaServiceImpl =
                                 Depends(injectQnaService)):

    ColorPrinter.print_important_message("requestQnaResult()")

    generatedQnaResult = qnaService.requestQnaResult()

    return JSONResponse(content=generatedQnaResult, status_code=status.HTTP_200_OK)