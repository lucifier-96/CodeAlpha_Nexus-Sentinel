import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_FILE = BASE_DIR / "database" / "alerts.db"


def analyze_alerts():
    connection = sqlite3.connect(DB_FILE)

    print("\n=== NEXUS SENTINEL THREAT INTELLIGENCE ===")

    alerts = connection.execute("""
        SELECT source_ip, signature, severity, COUNT(*)
        FROM alerts
        GROUP BY source_ip, signature, severity
        ORDER BY COUNT(*) DESC
        LIMIT 10
    """).fetchall()

    if not alerts:
        print("No alerts available.")
    else:
        for ip, signature, severity, count in alerts:
            if severity == 1:
                level = "CRITICAL"
            elif severity == 2:
                level = "HIGH"
            elif severity == 3:
                level = "MEDIUM"
            else:
                level = "LOW"

            print(f"Threat Level: {level}")
            print(f"\nSource IP: {ip}")
            print(f"Signature: {signature}")
            print(f"Severity: {severity}")
            print(f"Occurrences: {count}")

    connection.close()


if __name__ == "__main__":
    analyze_alerts()
