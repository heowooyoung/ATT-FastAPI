from fastapi import APIRouter, Depends

from exponential_regression.service.exponential_regression_service_impl import ExponentialRegressionServiceImpl

exponentialRegressionRouter = APIRouter()

# Dependency Injection On Asynchronous Framework

# 여기서 이걸 선언하고 24번째 줄에서 함수 정의할때 의존성 Dpends 해줌으로써 service 객체를 부를 수 있음
async def injectExponentialRegressionService() -> ExponentialRegressionServiceImpl:
    return ExponentialRegressionServiceImpl()

exponentialRegressionService = ExponentialRegressionServiceImpl()

@exponentialRegressionRouter.get("/exponential-regression")
async def exponentialRegression(exponentialRegressionService:ExponentialRegressionServiceImpl =
                                Depends(injectExponentialRegressionService)):
    print(f"exponentialRegression()")
    return exponentialRegressionService.createSampleForExponentialRegression()