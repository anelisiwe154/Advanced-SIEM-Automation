
from code_implem.src.rule import Rule

class RuleBuilder:
    def __init__(self):
        self.rule_id = None
        self.rule_name = None
        self.description = None
        self.severity = None
        self.category = None
        self.tactics = None
        self.actions = []
        self.conditions = []

    def set_metadata(self, rule_name, description, source, type, event, response):
        self.rule_name = rule_name
        self.description = description
        return self

    def set_condition(self, condition_name, expression, count, userID):
        self.conditions.append((condition_name, expression, count, userID))
        return self

    def set_action(self, severity, category, tactic, persistence, action_type, tag):
        self.severity = severity
        self.category = category
        self.tactics = tactic
        self.actions.append((action_type, tag))
        return self

    def build(self):
        return Rule(
            rule_id="R1",
            rule_name=self.rule_name,
            description=self.description,
            severity=self.severity,
            conditions=self.conditions,
            actions=self.actions
        )

