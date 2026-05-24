class Rule:
    def __init__(self, id: str, name: str, condition=None):
        self.id = id
        self.name = name
        self.rule_id = id
        self.condition = condition

    def matches(self, alert):
        if self.condition:
            return self.condition(alert)
        return False


