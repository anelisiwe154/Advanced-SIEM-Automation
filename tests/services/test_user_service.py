# /tests/services/test_user_service.py
import pytest
from services.user_service import UserService, UserNotFoundException
from code_implem.repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from code_implem.src.user import User

def test_register_user_success():
    repo = InMemoryUserRepository()
    service = UserService(repo, max_active_users=2)
    user = User(id="U1", name="Alice")
    saved = service.register_user(user)
    assert saved.name == "Alice"

def test_register_user_limit_exceeded():
    repo = InMemoryUserRepository()
    service = UserService(repo, max_active_users=1)
    repo.save(User(id="U1", name="Alice"))
    with pytest.raises(ValueError):
        service.register_user(User(id="U2", name="Bob"))

def test_deactivate_user_success():
    repo = InMemoryUserRepository()
    user = User(id="U1", name="Alice")
    repo.save(user)
    service = UserService(repo)

    deactivated = service.deactivate_user("U1")
    assert not deactivated.is_active

def test_deactivate_user_not_found():
    repo = InMemoryUserRepository()
    service = UserService(repo)
    with pytest.raises(UserNotFoundException):
        service.deactivate_user("U99")
