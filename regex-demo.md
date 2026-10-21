```text
2026-04-14 14:32:01 INFO [TX-9921] FROM: DE89123456789012345678 TO: AT445566778899001122 AMOUNT: 1.250,50 EUR STATUS: SUCCESS
2026-04-14 14:35:10 WARN [TX-0042] FROM: GB11223344556677889900 TO: DE89123456789012345678 AMOUNT: 42,00 GBP STATUS: PENDING
2026-04-14 15:01:45 ERROR [TX-ERR-05] FROM: FR7600011122233344455566677 TO: DE89123456789012345678 AMOUNT: 10.000,00 EUR STATUS: FAILED (Insufficient funds)
2026-04-15 09:00:00 INFO [TX-1337] FROM: DE89123456789012345678 TO: CH99887766554433221100 AMOUNT: 5,99 CHF STATUS: SUCCESS
```

---

### Vorschläge für Regex-Patterns (Schritt-für-Schritt Demo)

Stelle sicher, dass auf regex101.com links der Flavor **"Python"** ausgewählt ist.

| Ziel | Regex-Pattern | Erklärung |
| :--- | :--- | :--- |
| **Datum isolieren** | `\d{4}-\d{2}-\d{2}` | Sucht exakt nach dem Format YYYY-MM-DD. |
| **Log-Level finden** | `(INFO\|WARN\|ERROR)` | **Alternation:** Findet eines der drei Schlüsselwörter. |
| **Transaktions-ID** | `\[TX-[\w-]+\]` | **Escaping & Character Class:** Findet IDs in eckigen Klammern. |
| **IBANs extrahieren** | `[A-Z]{2}\d{10,32}` | Sucht zwei Großbuchstaben gefolgt von 10 bis 32 Ziffern. |
| **Währungsbeträge** | `\d{1,3}(\.\d{3})*,\d{2}` | **Quantifiers & Groups:** Matcht deutsche Tausendertrennung (Punkt) und Dezimalkomma. |
| **Währung (3 Letter)** | `[A-Z]{3}(?=\sSTATUS)` | **Positive Lookahead:** Findet Währungskürzel, aber nur wenn danach "STATUS" folgt. |
| **Status-Meldung** | `STATUS:\s(\w+)` | **Capturing Group:** Extrahiert nur das Wort nach dem Doppelpunkt. |

---

### Tipps für die Kursleitung
* **Case Sensitivity:** Demonstriere den `(?i)` Flag oder den Checkbox-Haken bei regex101, um `info` vs. `INFO` zu zeigen.
* **Gieriges vs. Genügsames Matchen:** Nutze `FROM:.*TO:` (greedy) vs. `FROM:.*?TO:` (lazy), um zu zeigen, wie der Match bei mehreren IBANs in einer Zeile reagiert.
* **Raw Strings:** Erinnere die Teilnehmer daran, in Python immer `r'pattern'` zu nutzen, um Probleme mit Backslashes zu vermeiden.