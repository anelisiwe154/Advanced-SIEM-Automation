# api/incidents.py
from fastapi import APIRouter, HTTPException
from code_implem.repositories.inmemory.inmemory_incident_repository import InMemoryIncidentRepository
from services.incident_service import IncidentService

router = APIRouter(prefix="/api/incidents", tags=["Incidents"])

incident_repo = InMemoryIncidentRepository()
incident_service = IncidentService(incident_repo)

@router.get("/")
def get_all_incidents():
    return [
        {
            "id": i.id,
            "description": i.description,
            "is_escalated": i.is_escalated,
            "is_acknowledged": i.is_acknowledged,
        }
        for i in incident_service.get_incidents()
    ]

@router.post("/{incident_id}/escalate")
def escalate_incident(incident_id: str):
    try:
        incident = incident_service.escalate_incident(incident_id)
        return {
            "id": incident.id,
            "description": incident.description,
            "is_escalated": incident.is_escalated,
            "is_acknowledged": incident.is_acknowledged,
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{incident_id}/acknowledge")
def acknowledge_incident(incident_id: str):
    try:
        incident = incident_service.acknowledge_incident(incident_id)
        return {
            "id": incident.id,
            "description": incident.description,
            "is_escalated": incident.is_escalated,
            "is_acknowledged": incident.is_acknowledged,
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


    

