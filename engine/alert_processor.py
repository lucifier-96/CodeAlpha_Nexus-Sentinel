import json
import sqlite3
import time
from pathlib import Path

EVE_FILE = Path("/var/log/suricata/eve.json")
DB_FILE = Path(__file__).resolve().parent.parent / "database" / "alerts.db"


def save_alert(event):
    alert = event.get("alert", {})

    with sqlite3.connect(DB_FILE) as connection:
        connection.execute("""
            INSERT OR IGNORE INTO alerts
            (timestamp, source_ip, source_port,
             destination_ip, destination_port,
             protocol, signature, category, severity)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            event.get("timestamp"),
            event.get("src_ip"),
            event.get("src_port"),
            event.get("dest_ip"),
            event.get("dest_port"),
            event.get("proto"),
            alert.get("signature"),
            alert.get("category"),
            alert.get("severity")
        ))

        if connection.execute("SELECT changes()").fetchone()[0]:
            print("New alert:", alert.get("signature"))


def monitor():
    print("NEXUS SENTINEL alert monitor started.")
    print("Waiting for new Suricata alerts...")

    with EVE_FILE.open("r", encoding="utf-8") as log_file:
        # Start from the end to monitor only new events.
        log_file.seek(0, 2)

        while True:
            line = log_file.readline()

            if not line:
                time.sleep(0.5)
                continue

            try:
                event = json.loads(line)

                if event.get("event_type") == "alert":
                    save_alert(event)

            except json.JSONDecodeError:
                continue


if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        print("\nNEXUS SENTINEL monitor stopped.")
    except PermissionError:
        print("Permission denied: cannot read Suricata's log file.")
