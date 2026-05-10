
from typing import Optional, List
from .repository import Repository
from code_implem.src.incident import Incident

class IncidentRepository(Repository[Incident, str]):
    def save(self, entity: Incident) -> None:
        raise NotImplementedError

    def find_by_id(self, id: str) -> Optional[Incident]:
        raise NotImplementedError

    def find_all(self) -> List[Incident]:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
