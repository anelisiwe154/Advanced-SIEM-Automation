# Class Diagram – SIEM Domain Model
```mermaid
classDiagram
class User {
  -userID: String
  -password: String
  -organisation: String
  -locale: String
  +login()
  +logout()
  +viewDashboard()
}

class Alert {
  -incidentID: String
  -incidentTitle: String
  -ruleName: String
  -eventType: String
  -severity: String
  -firstOccurred: Date
  -lastOccurred: Date
  -category: String
  -subCategory: String
  -tactics: String
  -tag: String
  -reportingIP: String
  -count: int
  +generate()
  +acknowledge()
  +dismiss()
  +escalate()
}

class Rule {
  -ruleName: String
  -description: String
  -dataSource: String
  -detectionTechnology: String
  -eventType: String
  -remediationNotes: String
  -conditionName: String
  -filters: String
  -aggregate: String
  -groupBy: String
  -severity: String
  -category: String
  -techniques: String
  -tactics: String
  -action: String
  -tag: String
  +createRule()
  +applyCondition()
  +executeAction()
}

class Incident {
  -incidentId: String
  -type: String
  -status: String
  -resolutionDetails: String
  +assign()
  +investigate()
  +resolve()
}

class ResponseWorkflow {
  -workflowId: String
  -actions: String
  -status: String
  +trigger()
  +execute()
  +logAction()
}

class Report {
  -reportId: String
  -type: String
  -generatedDate: Date
  +compile()
  +publish()
}

User "1" --> "0..*" Alert : views
Alert "1" --> "0..1" Incident : escalates
Incident "1" --> "0..*" ResponseWorkflow : triggers
Rule "1" --> "0..*" Alert : defines
Incident "0..*" --> "0..*" Report : summarizedIn

%% =========================
%% Repository Interfaces
%% =========================
class Repository {
  +save(entity)
  +find_by_id(id)
  +find_all()
  +delete(id)
}

class AlertRepository
class IncidentRepository
class UserRepository
class RuleRepository

Repository <|-- AlertRepository
Repository <|-- IncidentRepository
Repository <|-- UserRepository
Repository <|-- RuleRepository

%% =========================
%% In-Memory Implementations
%% =========================
class InMemoryAlertRepository
class InMemoryIncidentRepository
class InMemoryUserRepository
class InMemoryRuleRepository

AlertRepository <|-- InMemoryAlertRepository
IncidentRepository <|-- InMemoryIncidentRepository
UserRepository <|-- InMemoryUserRepository
RuleRepository <|-- InMemoryRuleRepository

%% =========================
%% Future Stubs
%% =========================
class DatabaseAlertRepository
class FileSystemAlertRepository

AlertRepository <|-- DatabaseAlertRepository
AlertRepository <|-- FileSystemAlertRepository


``` 

### Design Decisions
- User remains simplified to core authentication and organisational attributes, ensuring clarity and avoiding      unnecessary complexity.
- Alert is expanded with detailed incident metadata (severity, tactics, reporting IP, etc.) to support richer detection and escalation workflows.
- Rule is modeled in three logical steps (metadata, condition, action) but kept in one class for readability and easier maintenance.
- Incident escalates from Alerts and triggers ResponseWorkflows, reflecting the operational flow of SIEM systems.
- Reports summarize Incidents for audit and compliance, ensuring traceability.
- Repository Interfaces abstract CRUD operations for each entity, enforcing consistent contracts and decoupling domain logic from storage.
- In-Memory Implementations provide working HashMap‑based storage for testing and current functionality.
- Future Stubs (Database, FileSystem) are included to demonstrate extensibility and future-proofing, raising NotImplementedError until implemented.
- This layered design balances simplicity, maintainability, and scalability, ensuring the SIEM domain model can evolve with new storage backends while remaining testable and robust. 

---
