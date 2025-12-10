from dataclasses import dataclass
from typing import Optional
from src.domain.value_objects.email import Email
from src.domain.value_objects.name import Name

@dataclass(frozen=True)
class User:
    id: Optional[int]
    name: Name
    email: Email
