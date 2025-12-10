from dataclasses import dataclass

@dataclass
class CreateUserViewModel:
    success: bool
    message: str
    user_id: int
