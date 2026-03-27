## 1. Use Case Diagram
```mermaid
usecase
  actor SecurityAnalyst
  actor IncidentResponder
  actor ITAdmin
  actor Developer
  actor EnterpriseUser
  actor ThreatIntelAPI

  SecurityAnalyst --> (View Dashboard)
  SecurityAnalyst --> (Acknowledge/Dismiss Alerts)
  SecurityAnalyst --> (Generate Alerts)
  IncidentResponder --> (Trigger Automated Response)
  ITAdmin --> (Ingest Logs)
  ITAdmin --> (Parse Logs)
  Developer --> (Maintain Detection Rules)
  EnterpriseUser --> (Receive Notifications)
  ThreatIntelAPI --> (Query Threat Intelligence API)
  ```