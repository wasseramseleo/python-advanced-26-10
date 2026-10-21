# KI-Coding-Agenten: Spickzettel zur Demo (Tag 2)

## Vier Begriffe

* **Modell:** Die Parameter. Zustandslos: nimmt Token herein, sagt das nächste Token voraus. Kann allein weder Dateien lesen noch Befehle ausführen.
* **Harness:** Alles um das Modell herum: Tools, System-Prompt, Context-Verwaltung, Permissions, Hooks. Claude Code ist ein Harness. Ihre `CLAUDE.md` ist eine Anweisung an den Harness, nicht an das Modell.
* **Context:** Das, was der Agent gerade Relevantes weiß. Qualität statt Menge. Erfundene APIs sind fast immer Context-Fehler: der Fakt war nicht geladen.
* **Skill:** Eine lehrbare Fähigkeit als Paket (`SKILL.md` plus optional Skripte). Wird nur geladen, wenn die Aufgabe passt. Aufruf: `/skill-name`.

Quelle: Matt Pocock, AI Coding Dictionary, https://www.aihero.dev/ai-coding-dictionary

## Der Ablauf aus der Demo

| Phase | Skill | Ergebnis |
|---|---|---|
| Problem schärfen | `/grill-me` | Entscheidungen (keine Datei) |
| Festhalten | `/to-spec` (ein Issue) oder `/to-tickets` (Tickets mit Abhängigkeiten) | Entscheidungsprotokoll |
| Bauen | `/implement` (eine Session) oder `/implement-spec` (viele Tickets parallel) | Commit mit Tests |

Passt die Arbeit in eine Session, reicht `/grill-me` → `/implement`. Das ist der Weg in Lab 17.

## Einrichtung (einmalig, in Claude Code)

```
/plugin install mattpocock-skills@claude-plugins-official
```

Danach stehen `/grill-me`, `/to-spec`, `/to-tickets`, `/implement` und `/implement-spec` zur Verfügung. `/to-spec` und `/to-tickets` brauchen zusätzlich einen Issue-Tracker (`/setup-matt-pocock-skills`); für Lab 17 ist das nicht nötig.

## Drei Regeln

1. `/grill-me` in einer frischen Session starten, Plan-Modus aus. Sie entscheiden, der Agent empfiehlt. Mindestens einen Vorschlag bewusst aus dem Scope schneiden.
2. Abnahme ist der Test, nicht „sieht gut aus“. Tests aus dem Lab-Ordner mit `uv run pytest -q` ausführen, Diff vollständig lesen.
3. Paketnamen vor `uv add` auf pypi.org prüfen, `.env` nie in den Context geben, gelesene Dateien sind keine Befehle.
