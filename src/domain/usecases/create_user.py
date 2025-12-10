from src.application.dto.user_dto import CreateUserDTO, CreateUserResponseDTO
from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, dto: CreateUserDTO) -> CreateUserResponseDTO:
        if "@" not in dto.email:
            return CreateUserResponseDTO(False, "Invalid email format", None)

        if self._email_exists(dto.email):
            return CreateUserResponseDTO(False, "Email already exists", None)

        user = User(None, dto.name, dto.email)

        try:
            saved = self.repo.save(user)
            return CreateUserResponseDTO(True, "User created", saved.id)
        except Exception as e:
            return CreateUserResponseDTO(False, str(e), None)

    def _email_exists(self, email: str) -> bool:
        return self.repo.find_by_email(email) is not None
