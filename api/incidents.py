from fastapi import APIRouter, HTTPException
from services.incident_service import IncidentService, IncidentNotFoundException, IncidentAlreadyEscalatedException
from code_implem.repositories.inmemory.inmemory_incident_repository import InMemoryIncidentRepository
from api.schemas import IncidentSchema

router = APIRouter(prefix="/api/incidents", tags=["Incidents"])
incident_service = IncidentService(InMemoryIncidentRepository())

@router.get("/", response_model=list[IncidentSchema])
def get_all_incidents():
    return incident_service.incident_repo.find_all()

@router.post("/{incident_id}/escalate", response_model=IncidentSchema)
def escalate_incident(incident_id: str):
    try:
        return incident_service.escalate_incident(incident_id)
    except IncidentNotFoundException:
        raise HTTPException(status_code=404, detail="Incident not found")
    except IncidentAlreadyEscalatedException:
        raise HTTPException(status_code=400, detail="Incident already escalated")

@router.post("/{incident_id}/acknowledge", response_model=IncidentSchema)
def acknowledge_incident(incident_id: str):
    try:
        return incident_service.acknowledge_incident(incident_id)
    except IncidentNotFoundException:
        raise HTTPException(status_code=404, detail="Incident not found")
