
from src.alert import Alert

class AlertFactory:
    @staticmethod
    def create_alert(alert_type, **kwargs):
        if alert_type == "Critical":
            return Alert(severity="High", **kwargs)
        elif alert_type == "Warning":
            return Alert(severity="Medium", **kwargs)
        elif alert_type == "Info":
            return Alert(severity="Low", **kwargs)
        else:
            raise ValueError("Unknown alert type")

