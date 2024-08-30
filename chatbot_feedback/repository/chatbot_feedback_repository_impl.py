import json
import queue

from chatbot_feedback.repository.chatbot_feedback_repository import ChatbotFeedbackRepository


class ChatbotFeedbackRepositoryImpl(ChatbotFeedbackRepository):

    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"ChatbotFeedbackRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"