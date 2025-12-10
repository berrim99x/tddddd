from fastapi import APIRouter, HTTPException
from src.application.dto.user_dto import CreateUserDTO
from src.application.presenters.user_presenter import UserPresenter
from src.domain.usecases.create_user import CreateUserUseCase
from src.infrastructure.repositories.memory_user_repository import MemoryUserRepository

router = APIRouter()
repo = MemoryUserRepository()
usecase = CreateUserUseCase(repo)
presenter = UserPresenter()

@router.post('/users')
async def create_user(payload: CreateUserDTO):
    res = usecase.execute(payload)
    if not res.success:
        raise HTTPException(status_code=400, detail=res.message)
    return presenter.present(res)
