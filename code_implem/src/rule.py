

class Rule:
    def __init__(self, rule_id, rule_name, description, severity="Medium", conditions=None, actions=None):
        self.rule_id = rule_id
        self.rule_name = rule_name   
        self.description = description
        self.severity = severity
        self.conditions = conditions or []
        self.actions = actions or []

    def add_condition(self, condition):
        self.conditions.append(condition)

    def add_action(self, action):
        self.actions.append(action)

    def evaluate(self, event):
        return all(cond(event) for cond in self.conditions)

    def execute_actions(self, event):
        for action in self.actions:
            action(event)

