import pytest
from code_implem.src.alert import Alert
from code_implem.src.incident import Incident
from code_implem.src.user import User
from code_implem.src.rule import Rule

from code_implem.repositories.inmemory.inmemory_alert_repository import InMemoryAlertRepository
from code_implem.repositories.inmemory.inmemory_incident_repository import InMemoryIncidentRepository
from code_implem.repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from code_implem.repositories.inmemory.inmemory_rule_repository import InMemoryRuleRepository


def test_inmemory_alert_repository_crud():
    repo = InMemoryAlertRepository()
    alert = Alert("1","Test Alert","Rule1","Event","High","2026-05-09","2026-05-09","Category","SubCategory","Tactic","Tag","127.0.0.1",1)
    repo.save(alert)
    assert repo.find_by_id("1") == alert
    assert alert in repo.find_all()
    repo.delete("1")
    assert repo.find_by_id("1") is None


def test_inmemory_incident_repository_crud():
    repo = InMemoryIncidentRepository()
    incident = Incident("1","Test Incident","Open")
    repo.save(incident)
    assert repo.find_by_id("1") == incident
    assert incident in repo.find_all()
    repo.delete("1")
    assert repo.find_by_id("1") is None


def test_inmemory_user_repository_crud():
    repo = InMemoryUserRepository()
    user = User("1", "password", "org", "local")
    repo.save(user)
    assert repo.find_by_id("1") == user
    assert user in repo.find_all()
    repo.delete("1")
    assert repo.find_by_id("1") is None



def test_inmemory_rule_repository_crud():
    repo = InMemoryRuleRepository()
    rule = Rule("1","Test Rule","Rule description")
    repo.save(rule)
    assert repo.find_by_id("1") == rule
    assert rule in repo.find_all()
    repo.delete("1")
    assert repo.find_by_id("1") is None
