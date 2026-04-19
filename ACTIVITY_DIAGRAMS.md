# User Login
```mermaid
flowchart TD
    Start --> EnterCredentials
    EnterCredentials --> ValidateCredentials
    ValidateCredentials -->|Valid| GrantAccess
    ValidateCredentials -->|Invalid| ShowError
    GrantAccess --> LoadDashboard
    LoadDashboard --> End
    ShowError --> End
```
    
Explanation:

Workflow: Analyst enters username, password, and customer ID. System validates credentials. If valid, access is granted and the dashboard loads; if invalid, an error is shown.

Stakeholder Concern: Ensures only authorized analysts can access sensitive alerts and logs.

Traceability: FR-7 (provide a dashboard for analysts to view alerts).



# Log Ingestion
```mermaid
flowchart TD
    Start --> CollectLogs
    CollectLogs --> NormalizeFormat
    NormalizeFormat --> StoreLogs
    StoreLogs --> End

    ```
Explanation:

Workflow: Logs collected, normalized, stored.

Stakeholder Concern: Scalability for enterprise servers.

Traceability: FR-1 (ingest logs), FR-2 (parse logs), FR-6 (store logs).

# Alert Generation
```mermaid
flowchart TD
    Start --> ApplyRules
    ApplyRules -->|Anomaly| GenerateAlert
    ApplyRules -->|No anomaly| End
    GenerateAlert --> StoreAlert
    StoreAlert --> End

```
Explanation:

Workflow: Detection rules applied, anomalies trigger alerts.

Stakeholder Concern: Timely detection of threats.

Traceability: FR-3 (apply rules), FR-5 (generate alerts), FR-6 (store alerts).

# VirusTotal Enrichment
```mermaid
flowchart TD
    Start --> SubmitQuery
    SubmitQuery --> ReceiveData
    ReceiveData --> UpdateAlert
    UpdateAlert --> End

```
Explanation:

Workflow: Suspicious event enriched with VirusTotal data.

Stakeholder Concern: Analysts need context for decisions.

Traceability: FR-4 (query VirusTotal API).

# Dashboard Viewing
```mermaid
flowchart TD
    Start --> LoadAlerts
    LoadAlerts --> DisplayAlerts
    DisplayAlerts --> RefreshAlerts
    RefreshAlerts --> DisplayAlerts
    DisplayAlerts --> End

```
Explanation:

Workflow: Alerts loaded, displayed, refreshed.

Stakeholder Concern: Real‑time visibility.

Traceability: FR-7 (dashboard for analysts).

# Alert Acknowledgement/Dismissal
```mermaid
flowchart TD
    Start --> ViewAlert
    ViewAlert --> Decision{Acknowledge or Dismiss?}
    Decision -->|Acknowledge| MarkAcknowledged
    Decision -->|Dismiss| MarkDismissed
    MarkAcknowledged --> End
    MarkDismissed --> End

```
Explanation:

Workflow: Analyst decides to acknowledge or dismiss.

Stakeholder Concern: Control over alert triage.

Traceability: FR-8 (acknowledge/dismiss alerts).

#  Automated Response Workflow
```mermaid
flowchart TD
    Start --> TriggerResponse
    TriggerResponse --> ExecuteActions
    ExecuteActions --> LogActions
    LogActions --> End

```
Explanation:

Workflow: Response triggered, actions executed, logged.

Stakeholder Concern: Fast mitigation with audit trail.

Traceability: FR-9 (trigger workflows), FR-10 (log actions).

# Report Generation
```mermaid
flowchart TD
    Start --> CompileData
    CompileData --> GenerateReport
    GenerateReport --> ReviewReport
    ReviewReport --> PublishReport
    PublishReport --> End

```
**Explanation:**

Workflow: Data compiled, report generated, reviewed, published.

Stakeholder Concern: Transparency for stakeholders.

Traceability: FR-10 (log/report automated actions).