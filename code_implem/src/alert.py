# code_implem/src/alert.py
class Alert:
    def __init__(self, id: str, description: str):
        self.id = id
        self.description = description
        self.incident_id = id
        self.incident_title = description
        self.is_acknowledged = False
        self.is_dismissed = False

    def generate(self):
        return f"Alert {self.description} generated."

    def acknowledge(self):
        self.is_acknowledged = True
        return f"Alert {self.id} acknowledged."

    def dismiss(self):
        self.is_dismissed = True
        return f"Alert {self.id} dismissed."

    def escalate(self):
        return f"Alert {self.id} escalated to Incident."


class AlertNotFoundException(Exception):
    pass


