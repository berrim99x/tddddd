from src.infrastructure.repositories.memory_user_repository import MemoryUserRepository
from src.domain.usecases.create_user import CreateUserUseCase
from src.application.presenters.user_presenter import UserPresenter

class UserFactory:
    @staticmethod
    def create_usecase():
        repo = MemoryUserRepository()
        return CreateUserUseCase(repo)

    @staticmethod
    def create_presenter():
        return UserPresenter()
