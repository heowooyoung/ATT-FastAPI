import os.path
import sys

from fastapi.middleware.cors import CORSMiddleware

import colorama

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

# llm project용 router 추가
from user_defined_initializer.init import UserDefinedInitializer
from istp_test.controller.istp_test_controller import istpTestRouter

from exponential_regression.controller.exponential_regression_controller import exponentialRegressionRouter

# 내부 로직을 import 하여 사용할 때 아래 path를 인식시켜줘야함
# 고로 내부 로직은 이 라인 하위에 import 해야 합니다.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.deep_learning.controller.deep_learning_controller import deepLearningRouter
from template.dice.controller.dice_controller import diceResultRouter
from template.include.socket_server.initializer.init_domain import DomainInitializer
from template.system_initializer.init import SystemInitializer
from template.task_manager.manager import TaskManager

DomainInitializer.initEachDomain()
SystemInitializer.initSystemDomain()
# 추가
UserDefinedInitializer.initUserDefinedDomain()

app = FastAPI()

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deepLearningRouter)
app.include_router(diceResultRouter)

app.include_router(exponentialRegressionRouter)

# 사용자 정의형 라우터들 등록
app.include_router(istpTestRouter)

if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
