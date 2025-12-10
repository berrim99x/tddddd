from dataclasses import dataclass
from typing import Optional
from src.domain.value_objects.email import Email

@dataclass(frozen=True)
class User:
    id: Optional[int]
    name: str
    email: Email
