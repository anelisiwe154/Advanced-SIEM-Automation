# Use Case Specifications

## Use Case 1: Ingest Logs
- **Actor:** IT Admin  
- **Precondition:** Log source configured.  
- **Postcondition:** Logs stored in raw format.  
- **Basic Flow:**  
  1. Admin configures source.  
  2. System ingests logs.  
  3. Logs stored.  
- **Alternative Flows:**  
  - Source unavailable -> error logged.  

---

## Use Case 2: Parse Logs
- **Actor:** IT Admin  
- **Precondition:** Logs ingested.  
- **Postcondition:** Logs standardized.  
- **Basic Flow:**  
  1. System parses logs.  
  2. Normalizes format.  
- **Alternative Flows:**  
  - Invalid format -> flagged.  

---

## Use Case 3: Apply Detection Rules
- **Actor:** Developer  
- **Precondition:** Parsed logs available.  
- **Postcondition:** Anomalies flagged.  
- **Basic Flow:**  
  1. Rules applied.  
  2. Anomalies detected.  
- **Alternative Flows:**  
  - No anomalies -> no alerts.  

---

## Use Case 4: Query Threat Intelligence API
- **Actor:** System (via API)  
- **Precondition:** Suspicious event detected.  
- **Postcondition:** Enrichment data attached.  
- **Basic Flow:**  
  1. System sends query.  
  2. Receives enrichment.  
  3. Attaches to alert.  
- **Alternative Flows:**  
  - API unavailable -> cached data used.  

---

## Use Case 5: Generate Alerts
- **Actor:** Security Analyst  
- **Precondition:** Detection rules triggered.  
- **Postcondition:** Alert created.  
- **Basic Flow:**  
  1. System generates alert.  
  2. Analyst notified.  
- **Alternative Flows:**  
  - Duplicate alert -> merged.  

---

## Use Case 6: View Dashboard
- **Actor:** Security Analyst  
- **Precondition:** Alerts exist.  
- **Postcondition:** Analyst sees enriched alerts.  
- **Basic Flow:**  
  1. Analyst logs in.  
  2. Dashboard displays alerts.  
- **Alternative Flows:**  
  - No alerts -> empty dashboard.  

---

## Use Case 7: Acknowledge/Dismiss Alerts
- **Actor:** Security Analyst  
- **Precondition:** Alert visible.  
- **Postcondition:** Alert marked acknowledged/dismissed.  
- **Basic Flow:**  
  1. Analyst selects alert.  
  2. System updates status.  
- **Alternative Flows:**  
  - Analyst cancels action -> no change.  

---

## Use Case 8: Trigger Automated Response
- **Actor:** Incident Responder  
- **Precondition:** Alert confirmed.  
- **Postcondition:** Response executed + logged.  
- **Basic Flow:**  
  1. Responder approves response.  
  2. System executes workflow.  
  3. Logs action + notifies user.  
- **Alternative Flows:**  
  - Response fails -> error logged. 