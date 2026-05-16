# /services/user_service.py
from code_implem.repositories.user_repository import UserRepository
from code_implem.src.user import User

class UserNotFoundException(Exception):
    pass

class UserService:
    def __init__(self, user_repo: UserRepository, max_active_users: int = 100):
        self.user_repo = user_repo
        self.max_active_users = max_active_users

    def register_user(self, user: User) -> User:
        users = self.user_repo.find_all()
        if len(users) >= self.max_active_users:
            raise ValueError("Maximum active users reached")
        return self.user_repo.save(user)

    def deactivate_user(self, user_id: str) -> User:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise UserNotFoundException(user_id)

        user.deactivate()
        return self.user_repo.save(user)
