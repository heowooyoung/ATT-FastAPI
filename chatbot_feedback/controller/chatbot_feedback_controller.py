import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

chatbotFeedbackRouter = APIRouter()

async def injectChatbotFeedbackService() -> ChatbotFeedbackServiceImpl:
    return ChatbotFeedbackServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@chatbotFeedbackRouter.post('/give-chatbot-feedback')
async def requestChatbotFeedback(chatbotFeedbackService: ChatbotFeedbackServiceImpl =
                                 Depends(injectChatbotFeedbackService)):

    ColorPrinter.print_important_message("requestChatbotFeedback()")

    getChatbotFeedback = chatbotFeedbackService.requestChatbotFeedback()

    return JSONResponse(content=getChatbotFeedback, status_code=status.HTTP_200_OK)