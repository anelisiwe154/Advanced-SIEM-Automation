class ResponseWorkflow:
    def __init__(self, workflow_id, actions, status="Pending"):
        self.workflow_id = workflow_id
        self.actions = actions
        self.status = status

    def trigger(self):
        self.status = "Triggered"
        return f"Workflow {self.workflow_id} triggered."

    def execute(self):
        self.status = "Executed"
        return f"Workflow {self.workflow_id} executed: {self.actions}"

    def log_action(self):
        return f"Workflow {self.workflow_id} logged."