"""
Lab 13 — Basis: Daten-Analyse mit Pandas.

Lädt die mitgelieferte `transactions.csv` in den DataFrame `df`. Die
Schritte 1 bis 4 aus der Angabe (Inspizieren, Bereinigen, Filtern,
Gruppieren) schreiben Sie selbst.
"""

from pathlib import Path

import pandas as pd

# 1. Laden und Inspizieren
#    Die Ladezeile ist bereits fertig. `Path(__file__).parent` ist der
#    Lab-Ordner, daher wird die CSV-Datei gefunden, egal von wo Sie starten.
df = pd.read_csv(Path(__file__).parent / "transactions.csv")

#    TODO: Verschaffen Sie sich mit `df.head()`, `df.info()` und
#    `df.describe()` einen Überblick über die Daten. (Im Skript geben Sie
#    die Ergebnisse mit `print(...)` aus; `df.info()` gibt selbst aus.)


# 2. Datenbereinigung (Filtern)
#    TODO: Erstellen Sie einen neuen DataFrame `df_completed`, der nur die
#    Zeilen aus `df` enthält, deren `status` den Wert `COMPLETED` hat.


# 3. Selektion und Filterung (Masking)
#    TODO: Arbeiten Sie ab jetzt nur noch mit `df_completed`. Erstellen Sie
#    eine Maske für alle `DEPOSIT`-Transaktionen mit einem `amount` größer
#    als 500 und geben Sie nur diese Zeilen aus.


# 4. Analyse (Groupby)
#    TODO: Gruppieren Sie `df_completed` nach `account_id` und berechnen Sie
#    die Summe der `amount`-Spalte pro Konto. Geben Sie das Ergebnis aus.
