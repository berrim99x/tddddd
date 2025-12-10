from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateUserDTO:
    name: str
    email: str

@dataclass
class CreateUserResponseDTO:
    success: bool
    message: str
    user_id: Optional[int] = None
