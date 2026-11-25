flowchart TD
    A["Network Traffic"] --> B["Suricata IDS"]
    B --> C["EVE JSON Logs"]
    C --> D["Python Alert Processor"]
    D --> E[("SQLite Database")]
    E --> F["Flask Dashboard"]
    D --> G["Threat Analyzer"]
    G --> F
    F --> H["Security Monitoring"]
