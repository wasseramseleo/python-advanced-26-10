# Python Advanced – Kursmaterial

Kurs „Python Advanced“ vom 20. bis 22.10.2026. Hier finden Sie die Angaben, Starter-Dateien, Daten, Demos und Folien des Kurses. Jeden Kurstag kommen die neuen Labs dazu, am Folgetag die Lösungen.

Der **Kurs-Ordner** ist das Verzeichnis mit der `pyproject.toml`, nach dem Klonen also `python-advanced-26-10`.

## Einrichtung

1.  Klonen Sie das Repository und wechseln Sie in den Kurs-Ordner:

    ```bash
    git clone https://github.com/wasseramseleo/python-advanced-26-10
    cd python-advanced-26-10
    ```

2.  Richten Sie die Umgebung ein, wie es `lab_00/Angabe.md` beschreibt. Der zentrale Befehl im Kurs-Ordner lautet:

    ```bash
    uv sync
    ```

Alle Labs teilen sich diese eine Umgebung, und alle Pakete für die Labs sind bereits enthalten. Führen Sie deshalb **weder `uv add` noch `pip install`** aus und ändern Sie `pyproject.toml` und `uv.lock` nicht.

## Skripte starten

Starten Sie Skripte immer **aus dem Lab-Ordner**, so wie es auch der grüne Pfeil in PyCharm tut. Vom Kurs-Ordner aus also zum Beispiel:

```bash
cd lab_01
uv run python main.py
```

- Mitgelieferte Daten (z.B. `transactions.csv`, `bank.db`) findet der Code von selbst, egal von wo aus Sie starten.
- Dateien, die Sie oder Ihr Code anlegen (z.B. `test_tx.log` oder Logdateien), liegen im Lab-Ordner.
- **mypy** (Lab 10) ist nicht Teil der Kurs-Umgebung. `uv run --with mypy` stellt es nur für den jeweiligen Aufruf bereit, zum Beispiel im Lab-Ordner `lab_10`:

  ```bash
  uv run --with mypy mypy account.py --strict
  ```

- **Tests** (Lab 15) starten Sie im Lab-Ordner `lab_15` (nicht ohne Pfad im Kurs-Ordner) mit:

  ```bash
  uv run pytest
  ```

## Aktualisieren

Holen Sie zu Beginn jedes Kurstags (und am 23.10. für die Lösungen von Tag 3) neue Labs, Lösungen und Folien im Kurs-Ordner mit:

```bash
git pull
```

Committen Sie nichts. Ihre eigenen Dateien stören den `git pull` nicht, weil Lösungen nie unter demselben Pfad erscheinen. Falls Sie doch etwas committet haben, aktualisieren Sie stattdessen mit:

```bash
git pull --no-rebase --no-edit
```

`--no-rebase` führt Ihre Commits mit den neuen Kursdateien zusammen. `--no-edit` übernimmt dabei die vorgeschlagene Merge-Nachricht, ohne einen Editor zu öffnen. Ein einfaches `git pull` bricht in diesem Fall je nach Git-Einstellung mit „Need to specify how to reconcile divergent branches“ ab.

Angaben, Demos und Folien können während des Kurses noch korrigiert werden. Bearbeiten Sie diese Dateien deshalb nicht direkt, sondern arbeiten Sie in einer Kopie. Starter-Dateien wie `lab_13/main.py` bearbeiten Sie dagegen direkt. Bricht `git pull` dennoch mit „Your local changes to the following files would be overwritten by merge“ ab, verwerfen Sie Ihre Änderung an den genannten Dateien mit `git restore <datei>` und wiederholen Sie `git pull`.

## Lösungen

- **Am Kurstag** liegt die Musterlösung als Zip auf dem Fileshare. Sie müssen das Zip nicht ins Repository entpacken. Falls Sie es doch im Kurs-Ordner entpacken, ignoriert Git den Ordner `musterloesung_tagN/`.
- **Ab dem Folgetag** stehen die Lösungen im Repository: die Erklärung unter `lab_XX/Lösung.md`, die Lösungsdateien unter `lab_XX/Lösung/`. Die Lösungen von Tag 3 erscheinen am 23.10.

## Folien

Die Folien kommen jeweils am Kurstag dazu und liegen unter `folien/tag_N.pdf` (`folien/tag_1.pdf` bis `folien/tag_3.pdf`).
