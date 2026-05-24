from code_implem.repositories.user_repository import UserRepository
from code_implem.src.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage: dict[str, User] = {}

    def save(self, entity: User) -> None:
        self._storage[entity.id] = entity

    def find_by_id(self, id: str) -> User | None:
        return self._storage.get(id)

    def find_all(self) -> list[User]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        self._storage.pop(id, None)

    def find_by_name(self, name: str) -> User | None:
        for user in self._storage.values():
            if user.name == name:
                return user
        return None


