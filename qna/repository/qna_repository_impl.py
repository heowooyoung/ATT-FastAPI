import json
import queue

from qna.repository.qna_repository import QnaRepositry

class QnaRepositoryImpl(QnaRepositry):

    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"QnaRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"