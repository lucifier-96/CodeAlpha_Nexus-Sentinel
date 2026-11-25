🛡️ NEXUS SENTINEL

Network Intrusion Detection & Threat Intelligence Dashboard

NEXUS SENTINEL is a network security monitoring project designed to detect suspicious network activity, process security alerts, store detection records and present security insights through a web-based dashboard.

🚀 Key Features

- Network intrusion detection using Suricata IDS
- EVE JSON security event processing
- Python-based alert processing engine
- SQLite database for alert storage
- Flask-powered monitoring dashboard
- Threat intelligence analysis
- Security alert classification

🧰 Technology Stack

Technology| Purpose
Python| Backend processing
Suricata| Intrusion detection
Flask| Web dashboard
SQLite| Alert storage
JSON| Security event processing
Linux| Development environment

🏗️ Project Architecture

Network Traffic
      |
      v
  Suricata IDS
      |
      v
   EVE JSON
      |
      v
 Alert Processor
      |
      v
 SQLite Database
      |
      v
 Flask Dashboard
      |
      v
 Security Monitoring

Threat analysis is handled by the intelligence module.

📁 Project Structure

nexus-sentinel/
│
├── config/
├── dashboard/
│   └── app.py
├── database/
├── detection/
├── engine/
│   └── alert_processor.py
├── intelligence/
│   ├── __init__.py
│   └── threat_analyzer.py
├── logs/
├── README.md
└── .gitignore

⚙️ Installation

Clone the repository:

git clone https://github.com/lucifier-96/CodeAlpha_Nexus-Sentinel.git

Navigate into the project:

cd CodeAlpha_Nexus-Sentinel

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Configure Suricata and the required event log paths before running the application.

🎯 Project Objective

To develop a modular network intrusion detection and monitoring system that combines network security event detection, automated processing, database storage and threat analysis.

🔮 Future Enhancements

- Advanced threat intelligence integration
- Real-time alert notifications
- IP reputation analysis
- Interactive security analytics
- Advanced incident reporting

⚠️ Disclaimer

This project is intended for educational purposes and authorized defensive security monitoring only.

---

Developed as a cybersecurity learning project.
