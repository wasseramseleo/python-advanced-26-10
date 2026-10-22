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
#    TODO: Eröffnen Sie eine `Session(engine)`, bauen Sie ein
#    `select(Account).order_by(Account.account_number)`-Statement und
#    geben Sie alle Accounts aus (jedes Objekt hat .account_number,
#    .owner, .balance).

# print("--- 1. Alle Konten (ORM) ---")
# with Session(engine) as session:
#     stmt = select(Account).order_by(Account.account_number)
#     for account in session.execute(stmt).scalars():
#         print(account)


# 2. Ein Konto per Nummer holen
#    TODO: Bauen Sie `select(Account).where(Account.account_number == "AT001")`
#    und holen Sie genau einen Treffer mit `.scalar_one_or_none()`.

# print("\n--- 2. find_account('AT001') (ORM) ---")
# with Session(engine) as session:
#     stmt = select(Account).where(Account.account_number == "AT001")
#     account = session.execute(stmt).scalar_one_or_none()
#     print(account)


# 3. Transaktionen über die `relationship` lesen
#    TODO: Greifen Sie auf `account.transactions` zu — die Beziehung wird
#    automatisch nachgeladen. Kein JOIN-SQL nötig.

# print("\n--- 3. Transaktionen für AT001 (ORM) ---")
# with Session(engine) as session:
#     account = session.execute(
#         select(Account).where(Account.account_number == "AT001")
#     ).scalar_one()
#     for tx in account.transactions:
#         print(f"  {tx.timestamp}  {tx.kind:8s}  {tx.amount:8.2f} EUR")


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
# with Session(engine) as session:
#     new_account = Account(
#         account_number="AT999",
#         owner="Neuer Kunde",
#         balance=100.0,
#         transactions=[
#             Transaction(kind="DEPOSIT", amount=100.0, timestamp="2026-05-01T12:00:00")
#         ],
#     )
#     session.add(new_account)
#     session.commit()
#     print(f"Eingefügt: {new_account}")
