import sqlite3
from pathlib import Path
from flask import Flask, render_template_string

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
DB_FILE = BASE_DIR / "database" / "alerts.db"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>NEXUS SENTINEL</title>
    <meta http-equiv="refresh" content="5">
    <style>
    .severity-1 {
    color: #ef4444;
    font-weight: bold;
}

.severity-2 {
    color: #f97316;
    font-weight: bold;
}

.severity-3 {
    color: #eab308;
    font-weight: bold;
}

.severity-4 {
    color: #22c55e;
    font-weight: bold;
}
        body {
            background: #101827;
            color: white;
            font-family: Arial;
            padding: 30px;
        }
        h1 { color: #38bdf8; }
        .card {
            background: #1e293b;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            border-bottom: 1px solid #475569;
            text-align: left;
        }
        th { color: #38bdf8; }
    </style>
</head>
<body>
    <h1>NEXUS SENTINEL</h1>
    <p>Network Intrusion Detection Dashboard</p>

    <div class="card">
        <h2>Total Alerts: {{ total }}</h2>
    </div>
<div class="card">
    <h2>Alert Severity Breakdown</h2>

    {% for severity, count in severity_counts %}
        <p>
            Severity {{ severity }}:
            <strong>{{ count }}</strong> alerts
        </p>
    {% endfor %}
</div>

    <div class="card">
        <h2>Recent Alerts</h2>
    <div class="card">
    <h2>Threat Intelligence — Top Source IPs</h2>

    <table>
        <tr>
            <th>Source IP</th>
            <th>Total Alerts</th>
            <th>Highest Severity</th>
        </tr>

        {% for ip, count, severity in threat_summary %}
        <tr>
            <td>{{ ip }}</td>
            <td>{{ count }}</td>
            <td class="severity-{{ severity }}">
                {{ severity }}
            </td>
        </tr>
        {% endfor %}
    </table>
</div>
        <table>
            <tr>
                <th>Time</th>
                <th>Source IP</th>
                <th>Destination IP</th>
                <th>Protocol</th>
                <th>Signature</th>
                <th>Severity</th>
            </tr>

            {% for alert in alerts %}
            <tr>
                <td>{{ alert[1] }}</td>
                <td>{{ alert[2] }}</td>
                <td>{{ alert[4] }}</td>
                <td>{{ alert[6] }}</td>
                <td>{{ alert[7] }}</td>
                <td class="severity-{{ alert[9] }}">
    {{ alert[9] }}
</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""


@app.route("/")
def dashboard():
    connection = sqlite3.connect(DB_FILE)

    total = connection.execute(
        "SELECT COUNT(*) FROM alerts"
    ).fetchone()[0]
    severity_counts = connection.execute(
    "SELECT severity, COUNT(*) FROM alerts GROUP BY severity"
    ).fetchall()

    threat_summary = connection.execute("""
        SELECT source_ip, COUNT(*) AS total,
               MAX(severity) AS highest_severity
        FROM alerts
        GROUP BY source_ip
        ORDER BY total DESC
        LIMIT 10
    """).fetchall()

    alerts = connection.execute(
        "SELECT * FROM alerts ORDER BY id DESC LIMIT 50"
    ).fetchall()

    connection.close()

    return render_template_string(
       HTML,
       total=total,
       alerts=alerts,
       severity_counts=severity_counts,
       threat_summary=threat_summary
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
