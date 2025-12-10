from src.application.dto.user_dto import CreateUserDTO
from src.domain.repositories.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, dto: CreateUserDTO):
        return self.repo.save(dto)
