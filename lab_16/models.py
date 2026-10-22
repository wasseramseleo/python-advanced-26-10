"""
Lab 16 — Bonus: ORM-Modelle für die `accounts`- und `transactions`-Tabellen.

TODO (Bonus-Aufgabe):
  1. Eine gemeinsame `Base(DeclarativeBase)`-Klasse definieren.
  2. Eine Klasse `Account` (Tabelle `accounts`) mit den Spalten
     id, account_number, owner, balance. Verwenden Sie `Mapped[...]`
     und `mapped_column(...)`. Setzen Sie `primary_key=True` und
     `unique=True` wo passend.
  3. Eine Klasse `Transaction` (Tabelle `transactions`) mit den Spalten
     id, account_id (ForeignKey auf accounts.id), kind, amount, timestamp.
  4. Eine `relationship` von `Account` zu `Transaction` (Liste) und in
     Gegenrichtung (Skalar), beide mit `back_populates`.
  5. Optional: `__repr__`-Methoden für lesbare Ausgaben.

Die vollständige Referenzimplementierung finden Sie in der Musterlösung
(am Kurstag auf dem Fileshare).
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Gemeinsame Basis-Klasse für alle ORM-Modelle."""


# class Account(Base):
#     ...

# class Transaction(Base):
#     ...
