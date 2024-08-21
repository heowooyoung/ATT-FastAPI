import json
import queue

from istp_test.repository.istp_test_repository import IstpTestRepository


class IstpTestRepositoryImpl(IstpTestRepository):

    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"IstpTestRepositoryImpl getResult()")

        try:
            # 왜 False를 get하지 ?
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"