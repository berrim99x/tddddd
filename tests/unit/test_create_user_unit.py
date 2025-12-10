from unittest.mock import Mock
from src.domain.usecases.create_user import CreateUserUseCase
from src.application.dto.user_dto import CreateUserDTO
from src.application.presenters.user_presenter import UserPresenter
from src.application.dto.user_dto import CreateUserResponseDTO
import pytest



def test_create_user_should_fail_when_repo_throws():
    repo = Mock()
    repo.find_by_email.return_value = None
    repo.save.side_effect = Exception("DB error")
    usecase = CreateUserUseCase(repo)

    dto = CreateUserDTO(name="Test", email="test@example.com")
    res = usecase.execute(dto)

    assert res.success is False
    assert "db error" in res.message.lower()

def test_create_user_fails_when_email_already_exists():
    repo = Mock()
    repo.find_by_email.return_value = {"id": 1, "name": "Old", "email": "test@example.com"}
    usecase = CreateUserUseCase(repo)

    dto = CreateUserDTO(name="New User", email="test@example.com")
    res = usecase.execute(dto)

    assert res.success is False
    assert "exists" in res.message.lower()

def test_create_user_fails_with_invalid_email_format():
    repo = Mock()
    repo.find_by_email.return_value = None
    usecase = CreateUserUseCase(repo)

    dto = CreateUserDTO(name="Test User", email="invalid-email")

    res = usecase.execute(dto)

    assert res.success is False
    assert "invalid" in res.message.lower()

def test_create_user_fails_when_name_is_empty():
    repo = Mock()
    repo.find_by_email.return_value = None
    usecase = CreateUserUseCase(repo)

    dto = CreateUserDTO(name="", email="valid@example.com")

    res = usecase.execute(dto)

    assert res.success is False
    assert "name" in res.message.lower()


def test_presenter_converts_response_to_viewmodel():
    presenter = UserPresenter()

    response = CreateUserResponseDTO(
        success=True,
        message="User created",
        user_id=10
    )

    vm = presenter.present(response)

    assert vm["success"] is True
    assert vm["message"] == "User created"
    assert vm["user_id"] == 10