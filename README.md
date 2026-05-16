# Advanced SIEM with Automated Incident Response

## Introduction
This project focuses on building an advanced Security Information and Event Management (SIEM) system enhanced with automated incident response capabilities. Traditional SIEM systems detect threats but often rely on manual analyst intervention, which slows down response times. By integrating automation and external threat intelligence (such as VirusTotal), this project aims to enable real‑time detection, enrichment, and automated response actions like device isolation.

Once completed, the system will:
- Ingest and analyze enterprise logs.
- Detect anomalies using rules and enrichment from external APIs.
- Provide a dashboard for analysts to monitor alerts.
- Automatically trigger response workflows to contain threats.

---

## Project Title and Description
**Advanced SIEM with Automated Incident Response**  
A simulation of a modern SIEM system that combines log ingestion, anomaly detection, external API enrichment, and automated response workflows. Designed to demonstrate how automation can reduce response times and improve cybersecurity resilience.

## Documentation
- [System Specification](SPECIFICATION.md)
- [Architecture & C4 Diagrams](ARCHITECTURE.md)
- [stakeholders.md](stakeholders.md) – Stakeholder analysis table.
- [requirements.md](requirements.md) – System Requirements Document (functional and non-functional requirements).
- [reflection.md](reflection.md) – Reflection on balancing stakeholder needs.
- [Use Case Diagram](usecase.drawio.png)

## Agile Planning 
- [Agile Planning Document](AGILE_PLANNING.md)  
- [GitHub Project Board](https://github.com/users/anelisiwe154/projects/4)  
- [Sprint 1 Milestone](https://github.com/anelisiwe154/Advanced-SIEM-Automation/milestone/1)  
- [Issues (User Stories)](https://github.com/anelisiwe154/Advanced-SIEM-Automation/issues)

## Assignment 7
- [Comparison of Kanban, Team Planning, Iterative Development, with justification for chosen template and reflection](TEMPLATE_ANALYSIS.md)
- [Template screenshots](screenshoots)
- [kaban expanation](KANBAN_EXPLANATION.md)

## Assignment 8: Object State Modeling and Activity Workflow Modeling
- [Activity Diagrams](ACTIVITY_DIAGRAMS.md)
- [State Diagrams](STATE_DIAGRAMS.md)
- [Assignment 8 Reflection](REFLECTION.md)

## Assignment 9: Domain Modeling and Class Diagram Development
- [Domain Model](DOMAIN_MODEL.md)  
Contains the key entities (User, Alert, Rule, Incident, ResponseWorkflow, Report), their attributes, methods, relationships, and business rules.
- [Class Diagram](CLASS_DIAGRAM.md)  
Mermaid.js UML diagram showing classes, attributes, methods, and relationships with multiplicity.
- [Assignment 9: Reflection](REFLECTION.md)  


# Assignment 10 : From Class Diagrams to Code with All Creational Patterns

- [Assignment 10 : Reflection](REFLECTION.md)
- [covrage,pytest screenshots](screenshoots)


## Overview
This project implements six creational design patterns in Python as part of an Advanced SIEM (Security Information and Event Management) system. The goal is to demonstrate design pattern usage, reproducibility through testing, and professional repository organization.

## Implemented Creational Patterns
- Factory: AlertFactory, SIEMFactory – creates alerts and incidents consistently.
- Builder: RuleBuilder – constructs complex Rule objects step by step.
- Prototype: AlertPrototype – clones existing alerts for reuse.
- Singleton: DatabaseConnection – ensures only one database connection instance.
- Additional Supporting Classes: Alert, Incident, Rule, User, ResponseWorkflow.

## Design Choices & Rationales
- Factory: Used to abstract alert/incident creation, ensuring consistent attributes across Cloud and OnPrem SIEM.
- Builder: Chosen for flexibility in constructing rules with metadata, conditions, and actions.
- Prototype: Enables cloning of alerts for rapid duplication in incident response scenarios.
- Singleton: Prevents multiple database connections, ensuring thread safety and resource efficiency.
- Traceability: Each pattern builds on prior assignments (state diagrams, domain models, class diagrams).

## Testing & Coverage
- Unit tests located in `/tests`.
- Run tests:
  ```bash
  pytest -v



## Language Choice & Design Decisions

This project was implemented in Python because:
- It provides clear syntax and readability, making UML-to-code translation straight forward.
- Strong support for object-oriented programming (classes, inheritance, composition).
- Excellent ecosystem for testing ('pytest') and coverage reporting.

### UML to Code Mapping
- Each class from the Mermaid.js UML diagram was translated into a Python class in '/src'.
- Attributes were implemented as instance variables (with '_' prefix for private fields where appropriate).
- Methods from the UML diagram were implemented directly (e.g., 'evaluate()', 'execute_actions()' in 'Rule').
- Relationships:
- Factory classes create 'Alert' and 'Incident' objects (composition).
-Builder constructs 'Rule' objects step by step.
- Singleton ensures only one 'DatabaseConnection' instance.
- Prototype clones 'Alert' objects for reuse.

This ensures traceability between UML diagrams (Assignment 9) and the Python implementation (Assignment 10).

## Creational Pattern Rationales

-Simple Factory (AlertFactory)  
  Used to centralize alert creation. This ensures consistent initialization of alerts without exposing object construction details.

- Factory Method (Processor classes)
  Applied to delegate instantiation logic to subclasses (RuleProcessor, IncidentProcessor). This supports extensibility when new processors are added.

-Abstract Factory (SIEMFactory)  
  Implemented to create families of related objects for different environments (Cloud vs OnPrem). This enforces environment‑specific consistency.

-Builder (RuleBuilder) 
  Chosen to construct complex Rule objects step by step. Rules often have optional metadata, conditions, and actions, making Builder ideal.

-Prototype (AlertPrototype) 
  Enables cloning of preconfigured alerts to avoid costly reinitialization. Useful in incident response where alerts need to be duplicated quickly.

-Singleton (DatabaseConnection) 
  Ensures only one database connection exists globally, preventing resource conflicts and maintaining thread safety.

## Assignment 11 : Implementing a Persistence Repository Layer

- Repository Interfaces:
  - repository.py
  - alert_repository.py, incident_repository.py, rule_repository.py, user_repository.py
- In-Memory Implementation:
  - inmemory_alert_repository.py, inmemory_incident_repository.py, inmemory_rule_repository.py, inmemory_user_repository.py
- Abstraction Mechanism:
  - repository_factory.py
- Future-Proofing:
  - Stubs: database_alert_repository.py, filesystem_alert_repository.py
  - Updated : [Class Diagram](CLASS_DIAGRAM.md) 
- Tests:
  - test_repository.py, test_repository_factory.py, test_inmemory_repositories.py, test_user.py

  - [Assignment 11 : Reflection](REFLECTION.md)

  ## Assignment 11 : Service Layer and REST API Implementation
  - [Sprint board update.png](screenshoots)
  - [Swagger UI Screenshots](docs)
  - [CHANGELOG.md]CHANGELOG.md)
  




