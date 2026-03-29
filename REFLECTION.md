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