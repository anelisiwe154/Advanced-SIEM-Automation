# /tests/services/test_rule_service.py
import pytest
from services.rule_service import RuleService, DuplicateRuleException
from code_implem.repositories.inmemory.inmemory_rule_repository import InMemoryRuleRepository
from code_implem.src.rule import Rule

def test_add_rule_success():
    repo = InMemoryRuleRepository()
    service = RuleService(repo)
    rule = Rule(id="R1", name="Detect Failed Logins")
    saved = service.add_rule(rule)
    assert saved.name == "Detect Failed Logins"

def test_add_rule_duplicate():
    repo = InMemoryRuleRepository()
    service = RuleService(repo)
    rule = Rule(id="R1", name="Detect Failed Logins")
    repo.save(rule)
    with pytest.raises(DuplicateRuleException):
        service.add_rule(rule)

def test_apply_rules_triggered():
    repo = InMemoryRuleRepository()
    service = RuleService(repo)
    rule = Rule(id="R1", name="Detect Failed Logins", condition=lambda alert: "failed" in alert.description)
    repo.save(rule)

    alert = type("Alert", (), {"description": "failed login attempt"})()
    triggered = service.apply_rules(alert)
    assert len(triggered) == 1
