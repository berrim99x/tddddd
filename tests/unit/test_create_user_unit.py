from unittest.mock import Mock
from src.domain.usecases.create_user import CreateUserUseCase
from src.application.dto.user_dto import CreateUserDTO
import pytest

def test_create_user_should_fail_when_repo_throws():
    repo = Mock()
    repo.find_by_email.return_value = None
    repo.save.side_effect = Exception("DB error")
    usecase = CreateUserUseCase(repo)

    dto = CreateUserDTO(name="Test", email="test@example.com")

    with pytest.raises(Exception):
        usecase.execute(dto)
