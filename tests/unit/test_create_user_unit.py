from unittest.mock import Mock
from src.domain.usecases.create_user import CreateUserUseCase
from src.application.dto.user_dto import CreateUserDTO
import pytest

from unittest.mock import Mock
from src.domain.usecases.create_user import CreateUserUseCase
from src.application.dto.user_dto import CreateUserDTO

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
