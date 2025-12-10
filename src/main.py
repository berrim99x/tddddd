from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.interface.controllers.user_controller import router as user_router
from src.interface.responses.error_response import ErrorResponse

app = FastAPI()


# ========== Custom 422 Error Handler (BLUE 7) ==========
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    error = exc.errors()[0]
    missing_field = error["loc"][-1]
    message = f"Missing required field: {missing_field}"

    error_response = ErrorResponse(message=message)
    return JSONResponse(
        status_code=422,
        content=error_response.dict()
    )


# ========== Routes ==========
app.include_router(user_router)
