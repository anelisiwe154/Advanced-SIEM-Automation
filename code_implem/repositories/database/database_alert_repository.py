from code_implem.repositories.alert_repository import AlertRepository
from code_implem.src.alert import Alert

class DatabaseAlertRepository(AlertRepository):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        # Future: initialize DB connection here

    def save(self, entity: Alert) -> None:
        raise NotImplementedError("Database save not yet implemented")

    def find_by_id(self, incident_id: str) -> Alert | None:
        raise NotImplementedError("Database find_by_id not yet implemented")

    def find_all(self) -> list[Alert]:
        raise NotImplementedError("Database find_all not yet implemented")

    def delete(self, incident_id: str) -> None:
        raise NotImplementedError("Database delete not yet implemented")

