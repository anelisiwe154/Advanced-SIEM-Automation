# Log Event
stateDiagram-v2
    [*] --> Ingested
    Ingested --> Parsed: Parser applies rules
    Parsed --> Stored: Save to database
    Stored --> Archived: Retention period expired
    Archived --> [*]
Explanation:

Key States: Ingested, Parsed, Stored, Archived.

Transitions: Logs are ingested, parsed into a standardized format, stored, and eventually archived.

Traceability: FR‑1 (ingest logs), FR‑2 (parse logs), FR‑6 (store logs).

# Detection Rule

stateDiagram-v2
    [*] --> Draft
    Draft --> Active: Approved by admin
    Active --> Disabled: Rule turned off
    Disabled --> Active: Re-enabled
    Active --> Retired: Outdated rule
    Retired --> [*]
Explanation:

Key States: Draft, Active, Disabled, Retired.

Transitions: Rules are drafted, activated, disabled, or retired.

Traceability: FR‑3 (apply detection rules).

# Alert

stateDiagram-v2
    [*] --> New
    New --> Investigating: Analyst reviews
    Investigating --> Acknowledged: Analyst acknowledges
    Investigating --> Dismissed: Analyst dismisses
    Investigating --> Escalated: Severity high
    Escalated --> Resolved: Incident resolved
    Resolved --> Closed: Manager approves closure
    Closed --> [*]
Explanation:

Key States: New, Investigating, Acknowledged, Dismissed, Escalated, Resolved, Closed.

Transitions: Alerts are generated, reviewed, acknowledged/dismissed, escalated if severe, resolved, and closed.

Traceability: FR‑5 (generate alerts), FR‑7 (dashboard for analysts), FR‑8 (acknowledge/dismiss alerts).

# Incident

stateDiagram-v2
    [*] --> Open
    Open --> Assigned: Analyst takes ownership
    Assigned --> InProgress: Investigation ongoing
    InProgress --> Resolved: Root cause fixed
    Resolved --> Closed: Manager validates resolution
    Closed --> [*]
Explanation:

Key States: Open, Assigned, InProgress, Resolved, Closed.

Transitions: Incidents move through assignment, investigation, resolution, and closure.

Traceability: FR‑9 (trigger automated response workflows).

# VirusTotal Query

stateDiagram-v2
    [*] --> Pending
    Pending --> Submitted: API request sent
    Submitted --> Enriched: Threat data received
    Enriched --> Stored: Save enrichment results
    Stored --> [*]
Explanation:

Key States: Pending, Submitted, Enriched, Stored.

Transitions: Queries are submitted, enriched with threat intelligence, and stored.

Traceability: FR‑4 (query VirusTotal API).

# Dashboard View

stateDiagram-v2
    [*] --> Loading
    Loading --> Displaying: Alerts retrieved
    Displaying --> Updated: Analyst refreshes
    Updated --> Displaying
    Displaying --> [*]
Explanation:

Key States: Loading, Displaying, Updated.

Transitions: Dashboard loads alerts, displays them, and updates when refreshed.

Traceability: FR‑7 (provide dashboard for analysts).

# Automated Response Workflow

stateDiagram-v2
    [*] --> Triggered
    Triggered --> Executing: Response actions running
    Executing --> Completed: Actions finished
    Completed --> Logged: Audit entry created
    Logged --> [*]
Explanation:

Key States: Triggered, Executing, Completed, Logged.

Transitions: Automated workflows are triggered, executed, completed, and logged for audit.

Traceability: FR‑9 (trigger workflows), FR‑10 (log automated actions).