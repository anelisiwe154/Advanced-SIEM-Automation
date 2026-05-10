from code_implem.repositories.incident_repository import IncidentRepository
from code_implem.src.incident import Incident

class InMemoryIncidentRepository(IncidentRepository):
    def __init__(self):
        self._storage: dict[str, Incident] = {}

    def save(self, entity: Incident) -> None:
        self._storage[entity.incident_id] = entity

    def find_by_id(self, incident_id: str) -> Incident | None:
        return self._storage.get(incident_id)

    def find_all(self) -> list[Incident]:
        return list(self._storage.values())

    def delete(self, incident_id: str) -> None:
        self._storage.pop(incident_id, None)

