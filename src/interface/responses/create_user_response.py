from pydantic import BaseModel

class CreateUserResponse(BaseModel):
    success: bool
    message: str
    user_id: int | None
