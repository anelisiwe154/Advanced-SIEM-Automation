# /services/user_service.py
from code_implem.repositories.user_repository import UserRepository
from code_implem.src.user import User

class UserNotFoundException(Exception):
    pass

class UserAlreadyDeactivatedException(Exception):
    pass

class UserService:
    def __init__(self, user_repo: UserRepository, max_active_users: int = None):
        self.user_repo = user_repo
        self.max_active_users = max_active_users

    def register_user(self, user: User) -> User:
        if self.max_active_users is not None:
            active_count = sum(1 for u in self.user_repo.find_all() if u.is_active)
            if active_count >= self.max_active_users:
                raise ValueError(f"Cannot register more than {self.max_active_users} active users")
        self.user_repo.save(user)
        return user

    def deactivate_user(self, user_id: str) -> User:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise UserNotFoundException(user_id)
        if not user.is_active:
            raise UserAlreadyDeactivatedException(user_id)
        user.deactivate()
        self.user_repo.save(user)
        return user

   
    def get_users(self) -> list[User]:
        return self.user_repo.find_all()

