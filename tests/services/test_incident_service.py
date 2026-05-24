# /tests/services/test_incident_service.py
import pytest
from services.incident_service import IncidentService, IncidentNotFoundException, IncidentAlreadyEscalatedException
from code_implem.repositories.inmemory.inmemory_incident_repository import InMemoryIncidentRepository
from code_implem.src.incident import Incident

def test_escalate_success():
    repo = InMemoryIncidentRepository()
    incident = Incident(id="I1", description="Suspicious login")
    repo.save(incident)
    service = IncidentService(repo)

    escalated = service.escalate_incident("I1")
    assert escalated.is_escalated

def test_escalate_not_found():
    repo = InMemoryIncidentRepository()
    service = IncidentService(repo)
    with pytest.raises(IncidentNotFoundException):
        service.escalate_incident("I99")

def test_escalate_already_escalated():
    repo = InMemoryIncidentRepository()
    incident = Incident(id="I1", description="Suspicious login")
    incident.escalate()
    repo.save(incident)
    service = IncidentService(repo)

    with pytest.raises(IncidentAlreadyEscalatedException):
        service.escalate_incident("I1")
