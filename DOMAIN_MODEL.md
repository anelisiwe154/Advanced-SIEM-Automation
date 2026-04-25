## Domain Model
| Entity | Attributes | Methods | Relationships |
| --- | --- | --- | --- |
| User | userID, password, organisation, locale | +login(), +logout(), +viewDashboard() | Has accounts, views Alerts |
| Alert | incidentID, incidentTitle, ruleName, eventType, severity, firstOccurred, lastOccurred, category, subCategory, tactics, tag, reportingIP, count | +generate(), +acknowledge(), +dismiss(), +escalate() | Generated from LogEvent, linked to Rule, escalates to Incident |
| Rule (Step 1) | ruleName, description, dataSource, detectionTechnology, eventType, remediationNotes | +createRule(), +editRule(), +deleteRule() | Defines detection logic applied to LogEvents |
| Rule (Step 2: Defined Condition) | conditionName, filters, aggregate, groupBy | +applyCondition(), +validateCondition() | Conditions refine Rule application |
| Rule (Step 3: Defined Action) | severity, category, techniques, tactics, action, tag | +executeAction(), +logAction() | Actions triggered when Rule matches an event |
| Incident | incidentId, type, status, resolutionDetails | +assign(), +investigate(), +resolve() | Escalated from Alert, triggers ResponseWorkflow |
| ResponseWorkflow | workflowId, actions, status | +trigger(), +execute(), +logAction() | Triggered by Incident |
| Report | reportId, type, generatedDate | +compile(), +publish() | Summarizes Alerts and Incidents |


## Business Rules
- A User must log in with userID, password, and organisation (customer/tenant context).
- An Alert is generated when a Rule condition matches a LogEvent.
- Alerts can be acknowledged or dismissed only by Analysts.
- A Rule is defined in three steps:
 - Metadata (name, description, data source, detection technology, event type, remediation notes).
 - Condition (filters, aggregation, grouping).
 - Action (severity, category, techniques, tactics, action, tag).
- An Incident is escalated from an Alert and may trigger one or more ResponseWorkflows.
- All automated actions must be logged and summarized in Reports for audit purposes.