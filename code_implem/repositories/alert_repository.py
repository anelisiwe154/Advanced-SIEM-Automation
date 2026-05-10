
from typing import Optional, List
from .repository import Repository
from code_implem.src.alert import Alert


class AlertRepository(Repository[Alert, str]):
    def save(self, entity: Alert) -> None:
        raise NotImplementedError

    def find_by_id(self, id: str) -> Optional[Alert]:
        raise NotImplementedError

    def find_all(self) -> List[Alert]:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
