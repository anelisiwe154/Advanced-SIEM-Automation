# /services/alert_service.py
from code_implem.src.alert import Alert
from code_implem.repositories.alert_repository import AlertRepository

class AlertNotFoundException(Exception):
    """Raised when an alert cannot be found in the repository."""
    pass

class AlertService:
    def __init__(self, alert_repo: AlertRepository):
        self.alert_repo = alert_repo

    def acknowledge_alert(self, alert_id: str) -> Alert:
        alert = self.alert_repo.find_by_id(alert_id)
        if not alert:
            raise AlertNotFoundException(alert_id)
        alert.acknowledge()
        self.alert_repo.save(alert)
        return alert

    def dismiss_alert(self, alert_id: str) -> Alert:
        alert = self.alert_repo.find_by_id(alert_id)
        if not alert:
            raise AlertNotFoundException(alert_id)
        alert.dismiss()
        self.alert_repo.save(alert)
        return alert
    
    def get_alerts(self) -> list[Alert]:
        return self.alert_repo.find_all()


