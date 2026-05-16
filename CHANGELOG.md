
date: "2026-05-01"

added:
  - Implemented all six creational patterns:
    - Factory (AlertFactory, SIEMFactory)
    - Builder (RuleBuilder)
    - Prototype (AlertPrototype)
    - Singleton (DatabaseConnection)
  - Added unit tests for each pattern (8 tests total)
  - Integrated pytest with coverage reporting

fixed:
  - Corrected import errors in alert_factory.py and siem_factory.py
  - Resolved duplicate keyword argument issues in CloudSIEMFactory and OnPremSIEMFactory
  - Updated Rule class to expose rule_name attribute
  - Fixed RuleBuilder initialization to avoid missing arguments

changed:
  - Refactored siem_factory.py to safely override kwargs
  - Improved repository structure with src/, creational_patterns/, and tests/ directories

known_issues:
  - Low coverage in response_workflow.py and user.py (0%)
  - Partial coverage in incident.py and alert_factory.py
  - Future improvement: add more edge case tests and CI/CD integration

features:
  - Incidents API (GET, Escalate, Acknowledge) → closes #11
  - Alerts API (GET, Acknowledge, Dismiss) → closes #14, #16
  - Rules API (GET, Add Rule) → closes #12
  - Users API (GET, Register, Deactivate) → closes #37, #38

documentation:
  - Added OpenAPI/Swagger UI (/docs)
  - Exported OpenAPI JSON → docs/openapi.json
  - Screenshot evidence → docs/swagger1_ui.png
  - Screenshot evidence → docs/swagger2_ui.png
  - Sprint board update.png → docs/screenshoots

fixes_improvements:
  - Fixed validation errors on Rule creation (422 response for missing fields)
  - Improved error handling for User deactivation (404 when user not found)
v
