# /services/incident_service.py
from code_implem.repositories.incident_repository import IncidentRepository
from code_implem.src.incident import Incident

class IncidentNotFoundException(Exception):
    pass

class IncidentAlreadyEscalatedException(Exception):
    pass

class IncidentService:
    def __init__(self, incident_repo: IncidentRepository):
        self.incident_repo = incident_repo

    def escalate_incident(self, incident_id: str) -> Incident:
        incident = self.incident_repo.find_by_id(incident_id)
        if not incident:
            raise IncidentNotFoundException(incident_id)

        if incident.is_escalated:
            raise IncidentAlreadyEscalatedException(incident_id)

        incident.escalate()
        return self.incident_repo.save(incident)

    def acknowledge_incident(self, incident_id: str) -> Incident:
        incident = self.incident_repo.find_by_id(incident_id)
        if not incident:
            raise IncidentNotFoundException(incident_id)

        incident.acknowledge()
        return self.incident_repo.save(incident)
