# /services/alert_service.py
from code_implem.repositories.alert_repository import AlertRepository
from code_implem.src.alert import Alert

class AlertNotFoundException(Exception):
    pass

class AlertService:
    def __init__(self, alert_repo: AlertRepository):
        self.alert_repo = alert_repo

    def acknowledge_alert(self, alert_id: str) -> Alert:
        alert = self.alert_repo.find_by_id(alert_id)
        if not alert:
            raise AlertNotFoundException(alert_id)

        alert.acknowledge()
        return self.alert_repo.save(alert)

    def dismiss_alert(self, alert_id: str) -> Alert:
        alert = self.alert_repo.find_by_id(alert_id)
        if not alert:
            raise AlertNotFoundException(alert_id)

        alert.dismiss()
        return self.alert_repo.save(alert)
