from src.application.dto.user_dto import CreateUserDTO, CreateUserResponseDTO
from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, dto: CreateUserDTO) -> CreateUserResponseDTO:
        existing = self.repo.find_by_email(dto.email)
        if existing:
            return CreateUserResponseDTO(False, "Email already exists", None)

        user = User(None, dto.name, dto.email)

        try:
            saved = self.repo.save(user)
            return CreateUserResponseDTO(True, "User created", saved.id)
        except Exception as e:
            return CreateUserResponseDTO(False, str(e), None)
