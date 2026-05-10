from code_implem.repositories.alert_repository import AlertRepository
from code_implem.src.alert import Alert

class InMemoryAlertRepository(AlertRepository):
    def __init__(self):
        self._storage: dict[str, Alert] = {}

    def save(self, entity: Alert) -> None:
        self._storage[entity.incident_id] = entity

    def find_by_id(self, incident_id: str) -> Alert | None:
        return self._storage.get(incident_id)

    def find_all(self) -> list[Alert]:
        return list(self._storage.values())

    def delete(self, incident_id: str) -> None:
        self._storage.pop(incident_id, None)

