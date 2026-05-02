import pytest
from creational_patterns.alert_factory import AlertFactory
from creational_patterns.processor import RuleProcessor, IncidentProcessor
from creational_patterns.siem_factory import CloudSIEMFactory, OnPremSIEMFactory
from creational_patterns.rule_builder import RuleBuilder
from creational_patterns.alert_prototype import AlertPrototype
from creational_patterns.database_connection import DatabaseConnection
from src.alert import Alert



def test_alert_factory():
    alert = AlertFactory.create_alert("Critical", incident_id="1", incident_title="Test", rule_name="Rule1",
                                      event_type="Login", first_occurred="2026-05-01", last_occurred="2026-05-01",
                                      category="Auth", sub_category="Login", tactics="BruteForce", tag="Test",
                                      reporting_ip="192.168.1.1", count=5)
    assert alert.severity == "High"


def test_rule_processor():
    processor = RuleProcessor()
    result = processor.process("Rule Data")
    assert "Rule processed" in result

def test_incident_processor():
    processor = IncidentProcessor()
    result = processor.process("Incident Data")
    assert "Incident processed" in result


def test_cloud_siem_factory():
    factory = CloudSIEMFactory()
    alert = factory.create_alert(incident_id="2", incident_title="Cloud Alert", rule_name="Rule2",
                                 event_type="Network", severity="Medium", first_occurred="2026-05-01",
                                 last_occurred="2026-05-01", category="Cloud", sub_category="Network",
                                 tactics="Persistence", tag="Cloud", reporting_ip="10.0.0.1", count=3)
    assert alert.category == "Cloud"

def test_onprem_siem_factory():
    factory = OnPremSIEMFactory()
    incident = factory.create_incident(incident_id="3", type="OnPrem", status="Open")
    assert incident.type == "OnPrem"


def test_rule_builder():
    rule = (RuleBuilder()
            .set_metadata("Suspicious Login", "Detects failed logins", "AuthLogs", "Signature", "LoginEvent", "Reset password")
            .set_condition("FailedLoginCondition", "status=failed", "count", "userID")
            .set_action("High", "Authentication", "BruteForce", "Persistence", "Alert", "LoginFailure")
            .build())
    assert rule.rule_name == "Suspicious Login"
    assert rule.severity == "High"


def test_alert_prototype_clone():
    prototype = AlertPrototype()
    base_alert = Alert("4", "Prototype Alert", "Rule3", "Event", "Low", "2026-05-01", "2026-05-01",
                       "Auth", "Login", "Recon", "Tag", "127.0.0.1", 1)
    prototype.register("base", base_alert)
    cloned_alert = prototype.clone("base", severity="Critical")
    assert cloned_alert.severity == "Critical"
    assert cloned_alert.incident_title == "Prototype Alert"


def test_database_connection_singleton():
    conn1 = DatabaseConnection("DB1")
    conn2 = DatabaseConnection("DB2")
    assert conn1 is conn2
    assert conn1.connection_string == "DB1" 
