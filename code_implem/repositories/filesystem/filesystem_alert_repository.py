from code_implem.repositories.alert_repository import AlertRepository
from code_implem.src.alert import Alert

class FileSystemAlertRepository(AlertRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save(self, entity: Alert) -> None:
        raise NotImplementedError("Filesystem save not yet implemented")

    def find_by_id(self, incident_id: str) -> Alert | None:
        raise NotImplementedError("Filesystem find_by_id not yet implemented")

    def find_all(self) -> list[Alert]:
        raise NotImplementedError("Filesystem find_all not yet implemented")

    def delete(self, incident_id: str) -> None:
        raise NotImplementedError("Filesystem delete not yet implemented")

