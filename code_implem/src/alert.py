class Alert:
    def __init__(self, incident_id, incident_title, rule_name, event_type, severity,
                 first_occurred, last_occurred, category, sub_category, tactics,
                 tag, reporting_ip, count):
        self.incident_id = incident_id
        self.incident_title = incident_title
        self.rule_name = rule_name
        self.event_type = event_type
        self.severity = severity
        self.first_occurred = first_occurred
        self.last_occurred = last_occurred
        self.category = category
        self.sub_category = sub_category
        self.tactics = tactics
        self.tag = tag
        self.reporting_ip = reporting_ip
        self.count = count

    def generate(self):
        return f"Alert {self.incident_title} generated."

    def acknowledge(self):
        return f"Alert {self.incident_id} acknowledged."

    def dismiss(self):
        return f"Alert {self.incident_id} dismissed."

    def escalate(self):
        return f"Alert {self.incident_id} escalated to Incident."
    
    __all__ = ["Alert"]
