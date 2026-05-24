class Incident:
    def __init__(self, id: str, description: str):
        self.id = id
        self.description = description
        self.incident_id = id
        self.incident_title = description
        self.is_escalated = False
        self.is_acknowledged = False

    def escalate(self):
        self.is_escalated = True
        return f"Incident {self.id} escalated."

    def acknowledge(self):
        self.is_acknowledged = True
        return f"Incident {self.id} acknowledged."

