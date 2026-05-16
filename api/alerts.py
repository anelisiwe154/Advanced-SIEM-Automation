from fastapi import APIRouter, HTTPException
from services.alert_service import AlertService, AlertNotFoundException
from code_implem.repositories.inmemory.inmemory_alert_repository import InMemoryAlertRepository
from api.schemas import AlertSchema

router = APIRouter(prefix="/api/alerts", tags=["Alerts"])
alert_service = AlertService(InMemoryAlertRepository())

@router.get("/", response_model=list[AlertSchema])
def get_all_alerts():
    return alert_service.alert_repo.find_all()

@router.post("/{alert_id}/acknowledge", response_model=AlertSchema)
def acknowledge_alert(alert_id: str):
    try:
        return alert_service.acknowledge_alert(alert_id)
    except AlertNotFoundException:
        raise HTTPException(status_code=404, detail="Alert not found")

@router.post("/{alert_id}/dismiss", response_model=AlertSchema)
def dismiss_alert(alert_id: str):
    try:
        return alert_service.dismiss_alert(alert_id)
    except AlertNotFoundException:
        raise HTTPException(status_code=404, detail="Alert not found")

