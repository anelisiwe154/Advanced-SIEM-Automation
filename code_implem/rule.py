class Rule:
    def __init__(self, rule_name=None, description=None, data_source=None,
                 detection_technology=None, event_type=None, remediation_notes=None,
                 condition_name=None, filters=None, aggregate=None, group_by=None,
                 severity=None, category=None, techniques=None, tactics=None,
                 action=None, tag=None):
        # Step 1: Metadata
        self.rule_name = rule_name
        self.description = description
        self.data_source = data_source
        self.detection_technology = detection_technology
        self.event_type = event_type
        self.remediation_notes = remediation_notes

        # Step 2: Condition
        self.condition_name = condition_name
        self.filters = filters
        self.aggregate = aggregate
        self.group_by = group_by

        # Step 3: Action
        self.severity = severity
        self.category = category
        self.techniques = techniques
        self.tactics = tactics
        self.action = action
        self.tag = tag

    def create_rule(self):
        return f"Rule {self.rule_name} created."

    def apply_condition(self):
        return f"Condition {self.condition_name} applied."

    def execute_action(self):
        return f"Action {self.action} executed."