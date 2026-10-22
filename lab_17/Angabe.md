# Lab 17 (optional): Ein Feature mit einem KI-Coding-Agenten spezifizieren und bauen

## Lernziele

In diesem Lab wenden Sie den Ablauf aus der Demo von Tag 2 selbst an: Sie schärfen eine lose Idee im Gespräch mit dem Agenten, lassen ihn das Feature bauen und nehmen das Ergebnis mit Tests ab.

  * Einen unscharfen Problem-Space mit `/grill-me` in Entscheidungen verwandeln.
  * Entscheidungen bewusst treffen (auch gegen die Empfehlung des Agenten) und den Scope beschneiden.
  * `/implement` nur Entschiedenes bauen lassen und das Ergebnis mit `pytest` abnehmen.
  * Den Diff vollständig lesen, bevor Sie ihn akzeptieren.

## Szenario

Unsere Bank möchte Kunden erlauben, ihr Konto bis zu einem vereinbarten Rahmen zu überziehen („Dispo“). Mehr wissen wir noch nicht. Genau dieser unscharfe Auftrag ist der Ausgangspunkt für das Grilling.

## Voraussetzungen

  * Claude Code mit installiertem Plugin (siehe `ki-demo.md` im Kurs-Ordner):

    ```
    /plugin install mattpocock-skills@claude-plugins-official
    ```

  * Starten Sie Claude Code im Ordner `lab_17/`. Dort liegen `account.py` und `exceptions.py` auf dem Stand von Lab 4 (Exceptions statt `return False`, Log-Datei pro Konto).
  * Tests laufen aus dem Lab-Ordner mit:

    ```bash
    cd lab_17
    uv run pytest -q
    ```

### Angabe

**Schritt 1: Grilling (ca. 15 min).**

Starten Sie eine frische Session (Plan-Modus aus) und geben Sie ein:

> /grill-me Kunden sollen ihr Konto bis zu einem vereinbarten Rahmen überziehen dürfen. Basis ist `account.py` in diesem Ordner.

Beantworten Sie jede Frage. Der Agent empfiehlt, Sie entscheiden. Mindestens diese Punkte müssen am Ende geklärt sein:

  * Wo wird der Rahmen festgelegt (Konstruktor, eigene Methode, beides)?
  * Was passiert, wenn eine Abhebung den Rahmen überschreitet (welche Exception, und wie verhält sie sich zu `InsufficientFundsError`)?
  * Darf der Rahmen negativ sein? Darf er nachträglich gesenkt werden, wenn das Konto schon im Minus ist?
  * Was ist bewusst **nicht** Teil dieses Features (z.B. Zinsen, Mahnungen)?
  * Welche Testfälle nehmen das Feature ab?

Schneiden Sie mindestens einen Vorschlag des Agenten bewusst aus dem Scope.

**Schritt 2: Bauen (ca. 15 min).**

Bleiben Sie in derselben Session und geben Sie ein:

> /implement Der Plan steht nur in diesem Gespräch, es gibt keine Spec-Datei. Tests kommen als `test_overdraft.py` in diesen Ordner.

Beobachten Sie die Freigabe-Anfragen und die Testläufe. Greifen Sie nicht in den Code ein, solange der Agent arbeitet.

**Schritt 3: Abnahme (ca. 10 min).**

  * Führen Sie `uv run pytest -q` im Ordner `lab_17/` aus. Alle Tests müssen grün sein.
  * Lesen Sie den Diff von `account.py` und `exceptions.py` vollständig.
  * Gehen Sie die Review-Checkliste durch.

### Review-Checkliste

  * Steht im Code etwas, das Sie im Grilling nicht entschieden haben?
  * Fehlt etwas, das Sie entschieden haben?
  * Gibt es für jede Entscheidung mindestens einen Test?
  * Sind Fehlerfälle als Exceptions aus `exceptions.py` modelliert, nicht als `return False`?
  * Wurde `pyproject.toml` oder `uv.lock` angefasst? (Darf nicht sein.)

### Bonus-Herausforderung

  * Lassen Sie den Agenten `uv run --with mypy mypy account.py exceptions.py` grün bekommen.
  * Starten Sie eine zweite, frische Session und lassen Sie sich den Diff mit `/code-review` prüfen. Vergleichen Sie die Befunde mit Ihrer eigenen Checkliste.
