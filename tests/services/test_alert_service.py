# /tests/services/test_alert_service.py
import pytest
from services.alert_service import AlertService, AlertNotFoundException
from code_implem.repositories.inmemory.inmemory_alert_repository import InMemoryAlertRepository
from code_implem.src.alert import Alert

def test_acknowledge_alert_success():
    repo = InMemoryAlertRepository()
    alert = Alert(id="A1", description="Suspicious activity")
    repo.save(alert)
    service = AlertService(repo)

    acknowledged = service.acknowledge_alert("A1")
    assert acknowledged.is_acknowledged

def test_acknowledge_alert_not_found():
    repo = InMemoryAlertRepository()
    service = AlertService(repo)
    with pytest.raises(AlertNotFoundException):
        service.acknowledge_alert("A99")

def test_dismiss_alert_success():
    repo = InMemoryAlertRepository()
    alert = Alert(id="A1", description="Suspicious activity")
    repo.save(alert)
    service = AlertService(repo)

    dismissed = service.dismiss_alert("A1")
    assert dismissed.is_dismissed
