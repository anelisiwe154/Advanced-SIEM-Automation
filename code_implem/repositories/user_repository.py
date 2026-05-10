
from typing import Optional, List
from .repository import Repository
from code_implem.src.user import User

class UserRepository(Repository[User, str]):
    def save(self, entity: User) -> None:
        raise NotImplementedError

    def find_by_id(self, id: str) -> Optional[User]:
        raise NotImplementedError

    def find_all(self) -> List[User]:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
