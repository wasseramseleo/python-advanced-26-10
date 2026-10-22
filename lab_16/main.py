"""
Lab 16 — Basis: Direkter SQL-Zugriff über SQLAlchemy Core.

Verbindet sich mit der mitgelieferten `bank.db` und führt einfache
SQL-Abfragen mit `text(...)` aus. Die Helper-Funktionen `find_account`,
`list_transactions` und `total_balance` schreiben Sie selbst.
"""

from pathlib import Path

from sqlalchemy import create_engine, text

DB_PATH = Path(__file__).parent / "bank.db"
engine = create_engine(f"sqlite:///{DB_PATH}")


# 1. Verbindung aufbauen und einfache Abfrage
print("--- 1. Alle Konten ---")
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT account_number, owner, balance FROM accounts ORDER BY account_number")
    )
    for row in result.mappings():
        print(f"{row['account_number']} | {row['owner']:20s} | {row['balance']:10.2f} EUR")


# 2. Parametrisierte Abfrage: find_account
#    TODO: Implementieren Sie die Funktion `find_account(conn, account_number)`,
#    die genau einen Datensatz aus `accounts` per `account_number` holt.
#    - Verwenden Sie `text("... WHERE account_number = :number")` mit benannten
#      Parametern.
#    - Geben Sie die gefundene Zeile als Mapping (dict-artig) zurück, oder
#      `None`, wenn kein Datensatz existiert.

# print("\n--- 2. find_account('AT001') ---")
# with engine.connect() as conn:
#     account = find_account(conn, "AT001")
#     print(account)


# 3. JOIN-Abfrage: list_transactions
#    TODO: Implementieren Sie `list_transactions(conn, account_number)`,
#    die alle Transaktionen eines Kontos zurückgibt.
#    - Joinen Sie `transactions` mit `accounts` über `account_id = accounts.id`.
#    - Filtern Sie nach `accounts.account_number = :number`.
#    - Sortieren Sie nach `timestamp` aufsteigend.

# print("\n--- 3. Transaktionen für AT001 ---")
# with engine.connect() as conn:
#     for tx in list_transactions(conn, "AT001"):
#         print(f"  {tx['timestamp']}  {tx['kind']:8s}  {tx['amount']:8.2f} EUR")


# 4. Aggregat: total_balance
#    TODO: Implementieren Sie `total_balance(conn)`, das die Summe aller
#    `balance`-Werte aus `accounts` als float zurückgibt.

# print("\n--- 4. Gesamtsumme aller Konten ---")
# with engine.connect() as conn:
#     total = total_balance(conn)
#     print(f"Gesamtsumme: {total:.2f} EUR")
