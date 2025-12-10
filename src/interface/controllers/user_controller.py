from fastapi import APIRouter
from src.application.dto.user_dto import CreateUserDTO
from src.application.presenters.user_presenter import UserPresenter
from src.domain.usecases.create_user import CreateUserUseCase
from src.infrastructure.repositories.memory_user_repository import MemoryUserRepository

router = APIRouter()

repo = MemoryUserRepository()
usecase = CreateUserUseCase(repo)
presenter = UserPresenter()

@router.post("/users")
def create_user(payload: CreateUserDTO):
    response = usecase.execute(payload)
    vm = presenter.present(response)
    return vm
