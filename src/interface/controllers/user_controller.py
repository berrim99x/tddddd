from fastapi import APIRouter, Depends
from src.application.dto.user_dto import CreateUserDTO
from src.infrastructure.factories.user_factory import UserFactory
from src.interface.requests.create_user_request import CreateUserRequest
from src.interface.responses.create_user_response import CreateUserResponse

router = APIRouter()

def get_usecase():
    return UserFactory.create_usecase()

def get_presenter():
    return UserFactory.create_presenter()

@router.post("/users", response_model=CreateUserResponse)
def create_user(
    request: CreateUserRequest,
    usecase = Depends(get_usecase),
    presenter = Depends(get_presenter)
):
    dto = CreateUserDTO(name=request.name, email=request.email)
    response = usecase.execute(dto)
    vm = presenter.present(response)
    return CreateUserResponse(**vm.__dict__)
