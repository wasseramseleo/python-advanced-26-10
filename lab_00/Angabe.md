# Lab 0: Einrichtung der Python-Umgebung mit uv

## Ziel

Dieses Lab stellt sicher, dass Ihre lokale Entwicklungsumgebung (Windows) korrekt für den Kurs konfiguriert ist. Wir verwenden in diesem Kurs ausschließlich **uv** – einen extrem schnellen, modernen Python-Paketmanager – und zielen auf **Python 3.12** (nur noch Sicherheits-Updates; aktuell sind 3.14 und 3.15).

**Bitte führen Sie alle Schritte sorgfältig aus und bitten Sie den Trainer um Hilfe, falls ein Befehl fehlschlägt.**

-----

## 1\. Konsole öffnen

Öffnen Sie eine neue Konsole. Sie können entweder die **Eingabeaufforderung** (`cmd.exe`) oder **PowerShell** verwenden. Alle folgenden Befehle werden dort ausgeführt.

-----

## 2\. `uv` prüfen

`uv` ersetzt in diesem Kurs `pip`, `venv` und die Verwaltung der Python-Versionen vollständig. Prüfen Sie zunächst, ob `uv` bereits installiert ist.

1.  Führen Sie aus:

    ```bash
    uv --version
    ```

**Erwartetes Ergebnis:** Sie sollten eine Versionsnummer sehen (z.B. `uv 0.x.y`). Die genaue Version ist nicht entscheidend; eine ältere Installation bringen Sie mit `uv self update` auf den aktuellen Stand.

  * **Falls `uv` nicht gefunden wird:**
    Installieren Sie es über PowerShell (empfohlen vom `uv`-Team):

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

    Schließen Sie nach der Installation Ihre Konsole und öffnen Sie eine neue, bevor Sie `uv --version` erneut versuchen.

-----

## 3\. Python 3.12 bereitstellen

`uv` verwaltet die Python-Interpreter selbst – Sie benötigen keine separate, systemweite Python-Installation.

1.  Installieren Sie Python 3.12:

    ```bash
    uv python install 3.12
    ```

2.  Prüfen Sie, dass eine 3.12-Version verfügbar ist:

    ```bash
    uv python list
    ```

**Erwartetes Ergebnis:** In der Liste erscheint ein Eintrag für `cpython-3.12.x`.

-----

## 4\. Gemeinsame Kurs-Umgebung synchronisieren

Der gesamte Kurs ist **ein einziges uv-Projekt**: Alle Labs teilen sich eine gemeinsame Umgebung, die durch die `pyproject.toml` und die `uv.lock` im Kurs-Ordner definiert ist. Sie legen also **keine** eigenen Environments pro Lab an.

1.  Wechseln Sie in den Kurs-Ordner (das Verzeichnis mit der `pyproject.toml`). Wie Sie das Kurs-Repository klonen, beschreibt die `README.md` des Kurs-Repositorys (auch auf GitHub lesbar). Ersetzen Sie `<Pfad zum Kurs-Ordner>` durch den Pfad auf Ihrem Rechner:

    ```bash
    cd <Pfad zum Kurs-Ordner>
    ```

2.  Synchronisieren Sie die Umgebung:

    ```bash
    uv sync
    ```

    `uv` legt dabei automatisch einen `.venv`-Ordner an und installiert alle in der `uv.lock` festgelegten Pakete (die *Single Source of Truth* für alle Labs). Sie müssen das Environment **nicht** manuell aktivieren – `uv run` erledigt das im Hintergrund.

-----

## 5\. Verifikation

Zuletzt prüfen wir, dass die Umgebung läuft und die richtige Python-Version sowie die Pakete bereitstehen.

1.  Prüfen Sie die Python-Version der Umgebung:

    ```bash
    uv run python --version
    ```

    **Erwartetes Ergebnis:** `Python 3.12.x`

2.  Führen Sie einen kurzen Import-Test aus:

    ```bash
    uv run python -c "import sys, numpy; print(sys.version.split()[0], numpy.__version__)"
    ```

**Erwartetes Ergebnis:**

```
3.12.x 2.x.x
```

(Die genaue numpy-Version kann abweichen.)

-----

## Abschluss

Wenn alle Befehle erfolgreich ausgeführt wurden, ist Ihre Umgebung für den Kurs bereit. Wenn Sie bei einem Schritt auf Probleme gestoßen sind, melden Sie sich bitte jetzt beim Trainer.
