# SIEM System Requirements 

## Functional Requirements
1. The system shall ingest logs from enterprise servers and endpoints.
2. The system shall parse logs into a standardized format.
3. The system shall apply detection rules to identify anomalies.
4. The system shall query VirusTotal API for threat enrichment.
5. The system shall generate alerts for suspicious events.
6. The system shall store logs and alerts in a database.
7. The system shall provide a dashboard for analysts to view alerts.
8. The system shall allow analysts to acknowledge or dismiss alerts.
9. The system shall trigger automated response workflows.
10. The system shall log all automated actions for audit purposes.

### Acceptance Criteria
- Detection rules must flag anomalies within 5 seconds of log ingestion.
- Dashboard must display alerts in real time with enrichment data.


## Non-Functional Requirements

### Usability
- The dashboard shall comply with WCAG 2.1 accessibility standards.
- The interface shall provide clear visual indicators for alert severity.
- The dashboard shall be simple enough to run in a browser on a laptop without requiring specialized hardware.
- The system shall provide straightforward navigation with minimal steps to access alerts and logs.

### Deployability
- The system shall be deployable on a personal laptop running Windows for prototype environment.
- Deployment scripts shall complete setup in under 1 hour on a standard laptop.
- The system shall run using lightweight components  suitable for limited hardware resources.
- For production design goals, the architecture could be extended to support deployment on Linux servers and cloud environments, but in the home lab prototype it will be demonstrated locally.

### Maintainability
- Documentation shall include an API guide for future integrations.
- The codebase shall be organized with clear comments and consistent naming conventions.
- Configuration files shall be separated from source code to simplify updates without code changes.
- The system shall use version control  so changes can be tracked and rolled back if needed.

### Scalability
- The system shall be able to ingest multiple simulated log sources concurrently.
- The database shall be able to store and query thousands of logs without performance degradation.
- The system shall demonstrate the ability to expand to additional log sources by adding more sample files or containers.
- For production design goals, the architecture could scale to hundreds of sources and millions of logs/day, but in the home lab prototype this will be simulated with smaller datasets.

### Security
- All user data stored locally shall be encrypted using AES‑256.
- API calls in the prototype shall require authentication tokens to simulate secure communication, even if only tested with sample files.
- The system shall restrict access to the dashboard with basic authentication (e.g., username/password) to demonstrate secure access control.

### Performance
- Search results shall load within 2 seconds when querying a dataset of thousands of logs on a laptop.
- Automated response workflows shall execute within 10 seconds of detection in the prototype environment.
- The system shall demonstrate responsiveness by handling multiple sample log sources without noticeable lag.