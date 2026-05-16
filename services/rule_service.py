# /services/rule_service.py
from code_implem.repositories.rule_repository import RuleRepository
from code_implem.src.rule import Rule

class DuplicateRuleException(Exception):
    pass

class RuleService:
    def __init__(self, rule_repo: RuleRepository):
        self.rule_repo = rule_repo

    def add_rule(self, rule: Rule) -> Rule:
        existing = self.rule_repo.find_by_name(rule.name)
        if existing:
            raise DuplicateRuleException(f"Rule '{rule.name}' already exists")
        return self.rule_repo.save(rule)

    def get_rules(self):
        return self.rule_repo.find_all()

    def apply_rules(self, alert):
        rules = self.rule_repo.find_all()
        triggered = [r for r in rules if r.matches(alert)]
        return triggered
