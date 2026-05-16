# /tests/api/test_incidents_api.py
import pytest
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_get_all_incidents_empty():
    response = client.get("/api/incidents/")
    assert response.status_code == 200
    assert response.json() == []

def test_escalate_not_found():
    response = client.post("/api/incidents/I99/escalate")
    assert response.status_code == 404


