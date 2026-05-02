class Incident:
    def __init__(self, incident_id, type, status, resolution_details=None):
        self.incident_id = incident_id
        self.type = type
        self.status = status
        self.resolution_details = resolution_details

    def assign(self, analyst):
        return f"Incident {self.incident_id} assigned to {analyst}."

    def investigate(self):
        return f"Incident {self.incident_id} under investigation."

    def resolve(self, details):
        self.resolution_details = details
        self.status = "Resolved"
        return f"Incident {self.incident_id} resolved: {details}"