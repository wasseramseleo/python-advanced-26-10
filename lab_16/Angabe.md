# Lab 16: Datenbanken mit SQLAlchemy

## Lernziele

In diesem Lab heben Sie unsere Banking-App von rein in-memory gehaltenen Daten auf eine echte Persistenzschicht (SQLite) und sprechen die Datenbank mit der `SQLAlchemy`-Bibliothek an.

  * Eine SQLite-Datenbank über `create_engine` und `engine.connect()` ansprechen.
  * SQL-Anweisungen mit `text(...)` formulieren und mit **benannten Parametern** (`:name`) gegen SQL-Injection absichern.
  * Ergebnis-Rows als `Mapping` (dict-artig) lesen und Spaltennamen verwenden.
  * Mehrere Tabellen mit `JOIN` verknüpfen und Aggregate (`SUM`) abfragen.
  * (Bonus) ORM-Modelle im modernen SQLAlchemy-2.0-Stil definieren (`DeclarativeBase`, `Mapped[...]`, `mapped_column`, `relationship`).
  * (Bonus) Mit einer `Session` und `select(...).where(...)` Datensätze als echte Python-Objekte abfragen und neue Datensätze persistieren.

## Szenario

In den bisherigen Labs lebten unsere Konten ausschließlich im RAM — beim Beenden des Programms war alles weg. In der echten Welt liegt der Kontostand natürlich in einer Datenbank. Die IT-Abteilung der Bank stellt Ihnen eine bereits gefüllte SQLite-Datei `bank.db` zur Verfügung (10 Konten, 24 Transaktionen einer Filiale).

Ihre Aufgabe: Lesen Sie die Daten zuerst mit klassischem SQL über die `SQLAlchemy`-Engine. In der Bonus-Herausforderung übersetzen Sie das `Account`-Modell in eine ORM-Klasse und arbeiten mit Objekten statt mit Rows.

**Vorbereitung:** Die Bibliothek SQLAlchemy ist bereits Teil der Kurs-Umgebung (`uv sync` aus Lab 0).

**Skripte starten:** Führen Sie die Skripte dieses Labs im Lab-Ordner aus:

```bash
cd lab_16
uv run python main.py
uv run python main_bonus.py   # Bonus-Herausforderung
```

**Hinweis zur DB-Datei:** Die mitgelieferte `bank.db` liegt im Lab-Ordner. Sollten Sie sie versehentlich beschädigen, können Sie jederzeit eine frische Kopie erzeugen, indem Sie im Lab-Ordner `uv run python seed_bank_db.py` ausführen.

## Schema der Demo-Datenbank

```
accounts                          transactions
----------------                  -----------------------
id              INTEGER PK        id              INTEGER PK
account_number  TEXT  UNIQUE      account_id      INTEGER  FK → accounts.id
owner           TEXT              kind            TEXT  ('DEPOSIT' | 'WITHDRAW')
balance         REAL              amount          REAL
                                  timestamp       TEXT  (ISO 8601)
```

### Angabe

**Ziel:** Implementieren Sie in `main.py` drei Helper-Funktionen für den lesenden Zugriff auf `bank.db`.

**Datei: `main.py`**

1.  **Engine erstellen** *(bereits vorgegeben)*:

      * `engine = create_engine("sqlite:///<pfad zu bank.db>")` ist im Starter schon enthalten. Eine `Engine` ist der zentrale Einstiegspunkt — sie verwaltet einen Pool an Verbindungen.

2.  **`find_account(conn, account_number) -> Mapping | None`**:

      * Holt genau einen Datensatz aus `accounts` per `account_number` (z.B. `"AT001"`).
      * Verwenden Sie eine **parametrisierte Query** mit `:number` als Platzhalter:
        ```python
        stmt = text("SELECT id, account_number, owner, balance FROM accounts WHERE account_number = :number")
        row = conn.execute(stmt, {"number": account_number}).mappings().first()
        ```
      * Gibt die Row als Mapping zurück (zugreifbar via `row["owner"]`) — oder `None`, wenn nichts gefunden wurde.
      * **Wichtig:** Bauen Sie das SQL niemals via f-string mit dem `account_number`-Wert zusammen — das öffnet die Tür für SQL-Injection!

3.  **`list_transactions(conn, account_number) -> list[Mapping]`**:

      * Gibt alle Transaktionen eines Kontos (sortiert nach `timestamp` aufsteigend) zurück.
      * Hier brauchen Sie einen `JOIN`, weil die `transactions`-Tabelle nur die numerische `account_id` kennt, Sie aber per `account_number` suchen wollen:
        ```sql
        SELECT t.timestamp, t.kind, t.amount
        FROM transactions AS t
        JOIN accounts AS a ON t.account_id = a.id
        WHERE a.account_number = :number
        ORDER BY t.timestamp ASC
        ```
      * Geben Sie eine Liste von Mappings zurück.

4.  **`total_balance(conn) -> float`**:

      * Berechnet die Gesamtsumme aller Konten-Salden:
        ```sql
        SELECT SUM(balance) FROM accounts
        ```
      * Verwenden Sie `.scalar_one()` auf dem Result, um den einzelnen Skalarwert zu erhalten.

5.  **Testen** Sie alle drei Funktionen, indem Sie die im Starter vorbereiteten `print`-Blöcke aktivieren.

-----

### Bonus-Herausforderung

**Ziel:** Übersetzen Sie die `Account`- und `Transaction`-Tabellen in ORM-Modelle und führen Sie dieselben Abfragen mit objektorientiertem Code aus. Fügen Sie zusätzlich einen neuen Account in die Datenbank ein.

**Datei: `models.py`**

1.  **ORM-Modelle** im modernen SQLAlchemy-2.0-Stil definieren:

      * Eine gemeinsame Basis-Klasse:
        ```python
        class Base(DeclarativeBase):
            pass
        ```
      * Klasse `Account` (Tabelle `accounts`) mit Feldern `id`, `account_number`, `owner`, `balance`. Verwenden Sie `Mapped[...]` als Typannotation und `mapped_column(primary_key=True)` bzw. `mapped_column(unique=True)` für die Constraints.
      * Klasse `Transaction` (Tabelle `transactions`) mit `id`, `account_id` (`ForeignKey("accounts.id")`), `kind`, `amount`, `timestamp`.
      * Eine `relationship` von `Account` zu `Transaction` (Liste) und in Gegenrichtung (Skalar) — beide mit `back_populates`.

**Datei: `main_bonus.py`**

2.  **Queries mit `select()`**:

      * Eröffnen Sie eine `Session(engine)` als Kontextmanager.
      * Alle Konten lesen: `stmt = select(Account).order_by(Account.account_number)` → `session.execute(stmt).scalars()`.
      * Einen Account holen: `select(Account).where(Account.account_number == "AT001")` → `.scalar_one_or_none()`.
      * Transaktionen eines Kontos: Statt JOIN einfach `account.transactions` lesen — die Beziehung wird automatisch nachgeladen.

3.  **Insert via Session**:

      * Legen Sie einen neuen `Account` an (z.B. `account_number="AT999"`, `owner="Neuer Kunde"`, `balance=100.0`) und hängen Sie direkt eine erste `Transaction` daran — über das `transactions=[...]`-Argument auf dem `Account`.
      * Mit `session.add(new_account)` zur Session hinzufügen und `session.commit()` persistieren.
      * Vergleichen Sie: **kein einziges SQL-Statement** in Ihrem Code — SQLAlchemy generiert die `INSERT`s aus den Objekten.
      * Lesen Sie den neuen Account anschließend mit `select(...)` erneut, um zu zeigen, dass er wirklich in der DB landet (nicht nur im RAM).

> **Hinweis:** Der Bonus verändert `bank.db` dauerhaft. Führen Sie `main_bonus.py` ein zweites Mal aus, bricht der Insert mit einem `IntegrityError` (`UNIQUE constraint failed: accounts.account_number`) ab, weil `AT999` bereits existiert. Zurücksetzen können Sie die Datenbank jederzeit mit `uv run python seed_bank_db.py` im Lab-Ordner.
>
> **Tipp (Idempotenz):** Machen Sie das Skript wiederholbar, indem Sie ganz am Anfang mit `select(...)` und `.scalar_one_or_none()` prüfen, ob `AT999` schon existiert, und den Datensatz dann mit `session.delete(...)` und `session.commit()` entfernen. Damit die zugehörigen Transaktionen mitgelöscht werden, braucht die `relationship` in `Account` das Argument `cascade="all, delete-orphan"`.
