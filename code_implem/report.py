class Report:
    def __init__(self, report_id, type, generated_date):
        self.report_id = report_id
        self.type = type
        self.generated_date = generated_date

    def compile(self):
        return f"Report {self.report_id} compiled."

    def publish(self):
        return f"Report {self.report_id} published."