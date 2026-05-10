import pytest

from code_implem.repositories.alert_repository import AlertRepository
from code_implem.repositories.incident_repository import IncidentRepository
from code_implem.repositories.user_repository import UserRepository
from code_implem.repositories.rule_repository import RuleRepository

from code_implem.src.alert import Alert
from code_implem.src.incident import Incident
from code_implem.src.user import User
from code_implem.src.rule import Rule


def test_alert_repository_interface():
    repo = AlertRepository()
    dummy_alert = Alert(
        "1",                
        "Test Alert",       
        "Rule1",            
        "Event",            
        "High",             
        "2026-05-09",       
        "2026-05-09",       
        "Category",         
        "SubCategory",      
        "Tactic",           
        "Tag",              
        "127.0.0.1",        
        1                   
    )
    with pytest.raises(NotImplementedError):
        repo.save(dummy_alert)


def test_incident_repository_interface():
    repo = IncidentRepository()
    dummy_incident = Incident(
        "1",                
        "Test Incident",    
        "Open"              
    )
    with pytest.raises(NotImplementedError):
        repo.save(dummy_incident)


def test_user_repository_interface():
    repo = UserRepository()
    dummy_user = User(
        "1",                
        "password",       
        "org",              
        "local"             
    )
    with pytest.raises(NotImplementedError):
        repo.save(dummy_user)


def test_rule_repository_interface():
    repo = RuleRepository()
    dummy_rule = Rule(
        "1",                
        "Test Rule",        
        "Rule description"  
    )
    with pytest.raises(NotImplementedError):
        repo.save(dummy_rule)


