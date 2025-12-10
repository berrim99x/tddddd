from typing import List, Optional
from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository

class MemoryUserRepository(UserRepository):
    def __init__(self):
        self._store: List[User] = []
        self._seq = 1

    def save(self, user: User) -> User:
        saved = User(self._seq, user.name, user.email)
        self._store.append(saved)
        self._seq += 1
        return saved

    def find_by_email(self, email: str) -> Optional[User]:
        for user in self._store:
            if user.email.value == email:
                return user
        return None
