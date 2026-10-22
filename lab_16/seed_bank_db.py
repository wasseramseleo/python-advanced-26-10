"""
Erzeugt die mitgelieferte Demo-Datenbank `bank.db` für Lab 16.

Wird einmalig ausgeführt, um die SQLite-Datei mit Beispiel-Konten und
-Transaktionen zu befüllen. Die Studenten brauchen dieses Skript NICHT
selbst auszuführen — `bank.db` liegt bereits im Lab-Ordner. Es dient
nur der Reproduzierbarkeit und der Dokumentation des Schemas.

Aufruf (im Lab-Ordner lab_16):
    uv run python seed_bank_db.py
"""

import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

DB_PATH = Path(__file__).parent / "bank.db"

SCHEMA = """
CREATE TABLE accounts (
    id              INTEGER PRIMARY KEY,
    account_number  TEXT    NOT NULL UNIQUE,
    owner           TEXT    NOT NULL,
    balance         REAL    NOT NULL
);

CREATE TABLE transactions (
    id          INTEGER PRIMARY KEY,
    account_id  INTEGER NOT NULL,
    kind        TEXT    NOT NULL CHECK (kind IN ('DEPOSIT', 'WITHDRAW')),
    amount      REAL    NOT NULL,
    timestamp   TEXT    NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);
"""

ACCOUNTS = [
    # (account_number, owner, balance)
    ("AT001", "Max Mustermann", 1250.50),
    ("AT002", "Erika Musterfrau", 8400.00),
    ("AT003", "Hans Huber", 320.75),
    ("AT004", "Ina Invest", 15600.00),
    ("AT005", "Berta Bank", 50.00),
    ("AT006", "Karl Konto", 2780.30),
    ("DE100", "Lena Leitner", 9999.99),
    ("DE101", "Otto Ortner", 12.50),
    ("CH200", "Petra Peters", 4500.00),
    ("CH201", "Quinn Quirin", 720.00),
]

# (account_number, kind, amount, days_ago)
TRANSACTIONS = [
    ("AT001", "DEPOSIT", 500.00, 30),
    ("AT001", "WITHDRAW", 150.00, 21),
    ("AT001", "DEPOSIT", 1000.00, 14),
    ("AT001", "WITHDRAW", 99.50, 7),
    ("AT002", "DEPOSIT", 8000.00, 60),
    ("AT002", "DEPOSIT", 400.00, 28),
    ("AT002", "WITHDRAW", 1000.00, 14),
    ("AT002", "DEPOSIT", 1000.00, 2),
    ("AT003", "DEPOSIT", 500.00, 45),
    ("AT003", "WITHDRAW", 179.25, 10),
    ("AT004", "DEPOSIT", 15000.00, 90),
    ("AT004", "DEPOSIT", 600.00, 12),
    ("AT005", "DEPOSIT", 100.00, 5),
    ("AT005", "WITHDRAW", 50.00, 1),
    ("AT006", "DEPOSIT", 3000.00, 20),
    ("AT006", "WITHDRAW", 219.70, 4),
    ("DE100", "DEPOSIT", 5000.00, 50),
    ("DE100", "DEPOSIT", 5000.00, 15),
    ("DE100", "WITHDRAW", 0.01, 3),
    ("DE101", "DEPOSIT", 12.50, 1),
    ("CH200", "DEPOSIT", 4000.00, 40),
    ("CH200", "DEPOSIT", 500.00, 17),
    ("CH201", "DEPOSIT", 800.00, 25),
    ("CH201", "WITHDRAW", 80.00, 9),
]


def main() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
        print(f"Alte Datenbank entfernt: {DB_PATH.name}")

    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(SCHEMA)

        conn.executemany(
            "INSERT INTO accounts (account_number, owner, balance) VALUES (?, ?, ?)",
            ACCOUNTS,
        )

        # account_number -> id (für die FK-Auflösung)
        id_by_number = {
            row[0]: row[1]
            for row in conn.execute("SELECT account_number, id FROM accounts")
        }

        now = datetime(2026, 5, 1, 12, 0, 0)
        for account_number, kind, amount, days_ago in TRANSACTIONS:
            ts = (now - timedelta(days=days_ago)).isoformat(timespec="seconds")
            conn.execute(
                "INSERT INTO transactions (account_id, kind, amount, timestamp) "
                "VALUES (?, ?, ?, ?)",
                (id_by_number[account_number], kind, amount, ts),
            )

        conn.commit()
        print(f"Datenbank erstellt: {DB_PATH}")
        print(f"  {len(ACCOUNTS)} Konten, {len(TRANSACTIONS)} Transaktionen")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
