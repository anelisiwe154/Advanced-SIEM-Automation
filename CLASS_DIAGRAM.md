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
  %% Step 1: Metadata
  -ruleName: String
  -description: String
  -dataSource: String
  -detectionTechnology: String
  -eventType: String
  -remediationNotes: String
  %% Step 2: Condition
  -conditionName: String
  -filters: String
  -aggregate: String
  -groupBy: String
  %% Step 3: Action
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

``` 

### Design Decisions
- User simplified to only core authentication and organisational attributes.  
- Alert expanded with detailed incident metadata (severity, tactics, reporting IP, etc.).  
- Rule modeled in three logical steps (General, condition, action) but kept in one class for readability.  
- Incident escalates from Alerts and triggers ResponseWorkflows.  
- Reports summarize Incidents for audit and compliance.  

---
