from pydantic import BaseModel

class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    user_id: int | None = None
