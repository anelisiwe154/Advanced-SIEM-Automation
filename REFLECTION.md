# Reflection

Balancing stakeholder needs proved challenging because:
- Security analysts require fewer false positives, while IT administrators prioritise overall system stability.
- Incident response teams demand automation to reduce response times, but enterprise users fear disruption to their daily work.
- Developers emphasize on maintainability and clear documentation, while performance goals pushed for speed and efficiency.

The main challenge is reconciling **automation vs. user experience**. The aim is to address this by ensuring automated responses include user notifications and audit logs, so actions are transparent and minimally disruptive. Another potential challenge is  balancing **API reliability vs. scalability**; This will be mitigated  by caching enrichment results to reduce external calls and improve consistency.

# Translating Requirements into Use Cases and Test Cases

One of the biggest challenges was ensuring completeness. It was easy to write a basic flow for each use case, but harder to anticipate alternative flows. For example, in the “Ingest Logs” use case, I had to consider what happens if the source is unavailable. Similarly, in “Trigger Automated Response,” I had to think about the possibility of a failed response. These alternative paths are critical because they reflect real world scenarios where systems don’t always behave ideally. Capturing them made the specifications more realistic and useful for testing.

Another challenge was distinguishing between functional and non‑functional requirements when designing test cases. Functional test cases map directly to the use cases, does the system ingest logs, parse them, apply detection rules, and so on? Non‑functional test cases, however, required me to think about qualities like performance and security. For instance, I had to design a test case to measure query response time and another to verify that API calls without authentication are rejected. This exercise highlighted the importance of testing not just what the system does, but how well it does it.

From a practical perspective, this assignment deepened my understanding of SIEM automation. Security systems are complex, and it is not enough to say “the system should detect anomalies.” You need to specify how anomalies are detected, what happens when they are found, how alerts are generated, and how analysts interact with those alerts. Writing use cases and test cases forced me to think about these details, which are essential for building a reliable SIEM solution.

# Assignment 8 : Reflection

Challenges in Choosing Granularity : Choosing how detailed to construct the status and activity diagrams was one of the most difficult tasks. Diagrams became complex and difficult to understand when there was too much detail, such as depicting every micro-step in log parsing. Missing crucial transitions, including differentiating between alert acknowledgment and dismissal, could result from providing too little information. By concentrating on significant states and behaviors that directly correspond to functional requirements, the balance was attained.

Aligning Diagrams with Agile User Stories: Making sure that every diagram matched the Agile user stories from Assignment 6 presented another difficulty. State and activity diagrams are system-focused, whereas user stories are produced from the analyst's point of view. Careful mapping was necessary to close this gap. For instance, the story "As an analyst, I want to acknowledge or dismiss alerts" was depicted in both the Alert state diagram and the Alert Acknowledge/Dismiss action diagram. This demonstrated that system behavior meets the needs of analysts.

State Diagrams vs. Activity Diagrams:State Diagrams, capture how individual objects (e.g., Alert, Incident, Log Event) change over time in response to events. They emphasize lifecycle and transitions, making them useful for understanding persistence and system rules. Activity Diagrams: Illustrate workflows and actions across multiple roles or components.

Lessons Learned
Granularity needs to strike a balance between completeness and readability secondly , diagrams are directly linked to system objectives when they are traceable to functional requirements. Analyst workflows and decision points are better modeled using activity diagrams, whereas system rules and lifecycles are best modeled using state diagrams. A comprehensive understanding of system behavior is produced by combining the two modeling approaches, which supports stakeholder needs and Agile development.

# Assignment 9: Reflection

Designing the domain model and class diagram for the SIEM system was a complex but rewarding exercise that required balancing abstraction, clarity, and alignment with prior assignments. One of the most significant challenges was determining the appropriate level of granularity for entities, particularly the Rule class. Rules in a SIEM system are inherently multi-layered, involving General, Defined conditions, and Defined actions. Initially, I considered splitting these into separate classes to reflect their distinct responsibilities, but this approach risked fragmenting the diagram and making relationships harder to trace. Consolidating them into a single class with structured attributes provided a more coherent representation, even though it sacrificed some granularity. This decision highlighted the trade-off between precision and readability, a recurring theme in object oriented design.

Another challenge was modeling the Alert entity, which required extensive attributes such as severity, tactics, reporting IP, and timestamps. Capturing all of these while maintaining a diagram that remained legible demanded careful structuring. Alerts also needed to be linked to both Rules (as their origin) and Incidents (as their escalation path). This dual relationship emphasized the importance of traceability, ensuring that alerts could be understood both as outputs of detection logic and as inputs to incident management. Similarly, defining whether ResponseWorkflow should be modeled as composition or aggregation required critical analysis. Composition would suggest that workflows are tightly bound to incidents, while aggregation reflects reusability across multiple incidents. I chose aggregation to better represent real SIEM practices, where workflows are often standardized and applied across different cases.

Method definitions also posed difficulties. For example, escalation could logically belong to either the Alert or Incident class. Placing it in Alert reflected the analyst’s workflow, where escalation is a direct response to alert severity, while Incident focused on investigation and resolution. This division of responsibilities reinforced the principle of cohesion, ensuring each class had a clear and focused role.

The class diagram aligns closely with earlier assignments. In Assignment 4 (Requirements), functional requirements such as FR-5 (generate alerts) and FR-9 (automated workflows) are directly represented in methods like Alert.generate() and ResponseWorkflow.trigger(). In Assignment 5 (Use Cases), scenarios such as “Analyst acknowledges alert” and “System triggers automated response” are captured in Alert.acknowledge() and ResponseWorkflow.execute(). In Assignment 8 (State and Activity Diagrams), the lifecycle of alerts (New -> Investigating -> Escalated -> Resolved -> Closed) is consistent with the attributes and transitions modeled in the class diagram. This continuity demonstrates how each assignment builds upon the previous, reinforcing the iterative nature of Agile development.

Several trade‑offs were necessary to keep the design practical. Inheritance was simplified by modeling user roles as attributes rather than creating subclasses for Analyst, Admin, or Manager. This reduced complexity while maintaining flexibility. Similarly, workflows were modeled as reusable aggregations rather than tightly coupled compositions. These trade‑offs illustrate the importance of pragmatism in design,  sometimes simplicity and clarity outweigh theoretical completeness.

The key lessons learned include the importance of balancing granularity with readability, ensuring traceability to requirements and use cases, and recognizing the complementary perspectives offered by different modeling techniques. State diagrams emphasize object lifecycles, activity diagrams highlight workflows, and class diagrams capture structural relationships. Together, they provide a holistic view of system behavior.



# Assignment 10 : Reflection

## Critical Analysis
Implementing the six creational patterns in the SIEM project highlighted the importance of design consistency and reproducibility. Each pattern was chosen to solve a specific problem:
- Factory simplified object creation by abstracting alert and incident instantiation.
- Builder provided flexibility in constructing complex `Rule` objects with metadata, conditions, and actions.
- Prototype enabled cloning of alerts, supporting rapid duplication in incident response workflows.
- Singleton ensured a single database connection, preventing resource conflicts.
- SIEMFactory demonstrated how Cloud and OnPrem environments can be encapsulated with consistent creation logic.

The biggest challenge was aligning class attributes with test expectations. For example, the Rule class originally used name, but tests required rule_name. This mismatch emphasized the need for traceability between UML diagrams, code, and test cases.

## Challenges Faced
- Import errors and module structure: Early failures occurred due to missing imports (ABC, Rule). These were resolved by carefully organizing src/ and creational_patterns/ directories.
- Duplicate keyword arguments: Factories initially passed duplicate parameters (category, type), causing runtime errors. Overriding `kwargs` safely fixed this.
- Coverage gaps: While core patterns achieved high coverage, supporting classes (response_workflow.py, user.py) remain under‑tested.

## Lessons Learned
- Consistency matters: Attribute naming must match across UML, implementation, and tests.
- Testing drives design: Pytest failures revealed subtle design flaws, guiding refactoring.
- Traceability improves quality: Linking commits to issues and maintaining a CHANGELOG ensured reproducibility and accountability.
- Coverage is a diagnostic tool: It highlighted areas of the system not yet validated, guiding future improvements.

## Alignment with Prior Work
This assignment builds directly on Assignments 8 and 9:
- From state diagrams and activity diagrams (Assignment 8), the transition logic informed how alerts and incidents should be modeled.
- From domain models and class diagrams (Assignment 9), the structural relationships guided the implementation of factories and builders.
- Assignment 10 extends these foundations by implementing creational patterns in code, validating them with tests, and documenting progress via GitHub.

Assignment 10 reinforced the value of design patterns in building scalable SIEM systems. The combination of structured implementation, automated testing, and GitHub project management provided a professional workflow that mirrors industry practice. Future work will focus on expanding test coverage and integrating CI/CD pipelines to further strengthen reproducibility.

# Assignment 11 : Reflection

In designing the repository layer for the SIEM project, I deliberately chose the Factory Pattern over Dependency Injection because it provides a lightweight and centralized mechanism for instantiating repositories without requiring a complex DI framework. This decision ensures that services remain decoupled from storage specifics, while still allowing flexibility to add new backends such as database or filesystem repositories in the future. The use of interfaces enforces consistent contracts across all entities, and the in‑memory implementations enabled fast unit testing and validation of CRUD operations. By introducing stub classes for database and filesystem repositories, the system demonstrates clear extensibility and future‑proofing, showing how new storage options can be integrated with minimal changes. Overall, this architecture balances simplicity, maintainability, and scalability, ensuring that the SIEM domain model remains robust and adaptable to evolving requirements.