from code_implem.repositories.user_repository import UserRepository
from code_implem.src.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage: dict[str, User] = {}

    def save(self, entity: User) -> None:
        self._storage[entity.user_id] = entity

    def find_by_id(self, user_id: str) -> User | None:
        return self._storage.get(user_id)

    def find_all(self) -> list[User]:
        return list(self._storage.values())

    def delete(self, user_id: str) -> None:
        self._storage.pop(user_id, None)

