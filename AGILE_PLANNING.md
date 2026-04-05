# Agile Planning 

## 1. User Stories

| Story ID | User Story | Acceptance Criteria | Priority |
|----------|------------|---------------------|----------|
| US-001 | As a security analyst, I want to ingest logs from multiple sources so that I can monitor diverse systems. | Logs from at least 2 sources are ingested and stored successfully. | High |
| US-002 | As a system admin, I want to parse logs into a standard format so that anomalies can be detected consistently. | Raw logs are normalized into a common schema. | High |
| US-003 | As a security analyst, I want detection rules applied to logs so that suspicious activity is flagged. | Rules trigger alerts when anomalies are detected. | High |
| US-004 | As a security analyst, I want to query threat intelligence APIs so that alerts are enriched with context. | API queries return enrichment data for suspicious hashes/IPs. | Medium |
| US-005 | As a security analyst, I want alerts generated and stored so that incidents can be tracked. | Alerts are visible in the dashboard with timestamps. | High |
| US-006 | As a security analyst, I want to view alerts in a dashboard so that I can quickly assess incidents. | Dashboard displays alerts with severity levels. | High |
| US-007 | As a security analyst, I want to acknowledge or dismiss alerts so that I can manage incident workflow. | Alerts can be marked as acknowledged or dismissed. | Medium |
| US-008 | As a system admin, I want automated responses triggered for critical alerts so that threats are contained quickly. | Critical alerts trigger automated workflows (e.g., block IP). | Medium |
| US-009 | As a system admin, I want system queries to return results in ≤2 seconds so that performance is acceptable. | Query response time ≤2 seconds under normal load. | High |
| US-010 | As a system admin, I want user data encrypted with AES-256 so that compliance is met. | All stored data is encrypted; unauthorized access is blocked. | High |

---

## 2. Product Backlog

| Story ID | User Story | Priority (MoSCoW) | Effort Estimate (Story Points) | Dependencies |
|----------|------------|-------------------|--------------------------------|--------------|
| US-001 | Ingest logs from multiple sources | Must-have | 5 | None |
| US-002 | Parse logs into standard format | Must-have | 3 | US-001 |
| US-003 | Apply detection rules | Must-have | 5 | US-002 |
| US-004 | Query threat intelligence APIs | Should-have | 3 | US-003 |
| US-005 | Generate and store alerts | Must-have | 4 | US-003 |
| US-006 | View alerts in dashboard | Must-have | 5 | US-005 |
| US-007 | Acknowledge/dismiss alerts | Should-have | 3 | US-006 |
| US-008 | Trigger automated responses | Could-have | 5 | US-005 |
| US-009 | Ensure query response ≤2s | Must-have | 2 | US-001 |
| US-010 | Encrypt user data | Must-have | 3 | None |

**Justification:**  
- Must-have stories deliver the MVP (ingestion, parsing, detection, alerts, dashboard, security).  
- Should-have stories improve usability.  
- Could-have stories add automation but can wait until later sprints.  

---

## 3. Sprint Plan

**Sprint 1 Goal:** Deliver the foundation of the SIEM backend by implementing log ingestion and log parsing into a standard format.

**Selected Stories:** US-001, US-002

| Task ID | Task Description | Assigned To | Estimated days | Status |
|---------|-----------------|-------------|-----------------|--------|
| T-001 | Develop log ingestion API | Anelisiwe | 8 | To Do |
| T-002 | Configure database for log storage | Anelisiwe | 6 | To Do |
| T-003 | Implement log parsing module | Anelisiwe | 6 | To Do |
| T-004 | Test ingestion → parsing pipeline end-to-end | Anelisiwe | 6 | To Do |

---

## Reflection

As the only stakeholder, I had to pretend to have competing goals, which was similar to the compromise and negotiation that actual Scrum teams have to deal with. While I fought for usability elements like dashboards and processes, I also wanted to give security aspects like encryption and efficiency first priority. I have to consider carefully what actually constitutes a minimal viable product in order to reconcile these viewpoints.

Setting priorities was my first significant obstacle. I was able to distinguish between necessary and optional features by using the MoSCoW approach. At first, I intended to incorporate automated replies in Sprint 1, but I came to understand that ingesting and parsing are the real cornerstones of a SIEM. This demonstrated how simple it is to overcommit and how crucial it is to prioritize producing essential value.

Another challenge was estimation. It was necessary to balance effort, risk, and complexity while assigning story points. For instance, log ingestion appeared simple, but I projected five points since combining numerous sources adds hidden complexity. Although crucial, parsing is more contained, therefore I gave it three points. Estimating was subjective when I worked alone, but it helped me understand how teams must compromise and adjust their estimations together.


Another important lesson was to divide stories into tasks. Before I divided them down into specific tasks like Develop ingestion API or Implement parsing module, user stories felt abstract. Dependencies and sequencing were made clear, which is important for sprint planning. Additionally, it made the task measurable and tangible.

Lastly, I thought about how Agile is iterative. Sprint 1 is a foundation, not the finished product. Workflows, automation, enrichment, and detection will be added in the following sprints. In line with the Agile manifesto's emphasis on adapting to change rather than adhering to a strict plan, this incremental approach lowers risk and delivers return early.

To sum up, this part of the project taught me how to convert use cases and requirements into useful Agile artifacts. Even though I was the only stakeholder, the difficulties with prioritization, estimation, and alignment reflected real-world Agile dynamics. I had a greater understanding of the discipline needed to balance competing by modeling internal resistance. needs. Most importantly, I saw how Agile planning transforms abstract requirements into a roadmap for delivering a working system, one sprint at a time.

---