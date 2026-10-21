filename = "transactions_large.log"


def stream_transactions(filename):
    print("LOG: Stream startet...")
    with open(filename, "r") as f:
        for line in f:
            # yield pausiert die Ausführung und gibt die Zeile zurück
            yield line.strip()
    print("LOG: Stream beendet.")


# 1. Quelle: Zeilen lesen
raw_lines = stream_transactions("transactions_large.log")


# 2. Transformation: Nur Beträge als Float extrahieren
# (Wir simulieren eine komplexe Extraktion)
def extract_amount(lines):
    for line in lines:
        parts = line.split("|")
        amount_str = parts[2].replace("AMOUNT:", "").strip()
        yield float(amount_str)


# 3. Filter: Nur Beträge über 5000
def filter_high_value(amounts):
    for a in amounts:
        if a > 5000:
            yield a


# Die Pipeline zünden
pipeline = filter_high_value(extract_amount(raw_lines))

for val in pipeline:
    print(f"High Value gefunden: {val}")
    break  # Wir können jederzeit aufhören, die Datei wird nicht weiter gelesen!
