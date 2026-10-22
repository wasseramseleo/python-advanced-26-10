"""
Lab 16 — Bonus: ORM-Zugriff über SQLAlchemy 2.0 (Session + select()).

Nutzt die in `models.py` definierten ORM-Modelle `Account` und
`Transaction`. Statt rohem SQL kommen `select(...).where(...)` und
`session.execute(...)` zum Einsatz; das Ergebnis sind echte
Python-Objekte mit Attributen.
"""

from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

# Nach Erledigung der TODOs in models.py einkommentieren:
# from models import Account, Transaction

DB_PATH = Path(__file__).parent / "bank.db"
engine = create_engine(f"sqlite:///{DB_PATH}")


# 1. Alle Konten via ORM lesen
#    TODO: Eröffnen Sie eine `Session(engine)`, lesen Sie mit `select(...)`
#    alle Accounts sortiert nach `account_number` und geben Sie sie aus
#    (jedes Objekt hat .account_number, .owner, .balance).

# print("--- 1. Alle Konten (ORM) ---")


# 2. Ein Konto per Nummer holen
#    TODO: Holen Sie mit `select(...)` und `.where(...)` den Account
#    "AT001" — genau einen Treffer oder `None`.

# print("\n--- 2. find_account('AT001') (ORM) ---")


# 3. Transaktionen über die `relationship` lesen
#    TODO: Greifen Sie auf `account.transactions` zu — die Beziehung wird
#    automatisch nachgeladen. Kein JOIN-SQL nötig.

# print("\n--- 3. Transaktionen für AT001 (ORM) ---")


# 4. Neuen Account + Transaktion einfügen
#    TODO: Erstellen Sie einen neuen `Account` (z.B. account_number="AT999",
#    owner="Neuer Kunde", balance=100.0). Hängen Sie eine erste
#    `Transaction` daran (kind="DEPOSIT", amount=100.0, timestamp="2026-05-01T12:00:00").
#    Speichern Sie mit `session.add(...)` + `session.commit()`.
#    Lesen Sie danach den Account erneut, um die Persistenz zu verifizieren.
#    Achtung: Ein zweiter Lauf scheitert mit einem IntegrityError, weil
#    AT999 dann schon existiert. Zurücksetzen: `uv run python seed_bank_db.py`
#    (Idempotenz-Tipp siehe Angabe).

# print("\n--- 4. Neuen Account einfügen ---")
