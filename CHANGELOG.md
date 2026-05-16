---

## 2. CHANGELOG.md
# CHANGELOG

- Implemented all six creational patterns:
  - Factory (AlertFactory, SIEMFactory)
  - Builder (RuleBuilder)
  - Prototype (AlertPrototype)
  - Singleton (DatabaseConnection)
- Added unit tests for each pattern (8 tests total).
- Integrated pytest with coverage reporting.

### Fixed
- Corrected import errors in alert_factory.py and siem_factory.py.
- Resolved duplicate keyword argument issues in CloudSIEMFactory and OnPremSIEMFactory.
- Updated Rule class to expose rule_name attribute (matching test expectations).
- Fixed RuleBuilder initialization to avoid missing arguments.

### Changed
- Refactored siem_factory.py to safely override kwargs instead of duplicating.
- Improved repository structure with src/, creational_patterns/, and tests/ directories.

### Known Issues
- Low coverage in response_workflow.py and user.py (0%).
- Partial coverage in incident.py and alert_factory.py.
- Future improvement: add more edge case tests and CI/CD integration.



### Features
- **Incidents API** (GET, Escalate, Acknowledge)  
  - Implemented in `api/incidents.py`  
  - Closes #11  

- **Alerts API** (GET, Acknowledge, Dismiss)  
  - Implemented in `api/alerts.py`  
  - Closes #14, #16  

- **Rules API** (GET, Add Rule)  
  - Implemented in `api/rules.py`  
  - Closes #12  

- **Users API** (GET, Register, Deactivate)  
  - Implemented in `api/users.py`  
  - Closes #37, #38  

### Documentation
- Added **OpenAPI/Swagger UI** (`/docs`) and **ReDoc** (`/redoc`)  
- Exported OpenAPI JSON → `docs/openapi.json`  
- Screenshot evidence → `docs/swagger_ui.png`  

### Fixes & Improvements
- Fixed validation errors on Rule creation (422 response for missing fields)  
- Improved error handling for User deactivation (404 when user not found)  

---

Closes #11, #12, #14, #16, #37, #38