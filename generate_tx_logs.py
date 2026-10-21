import random
import uuid

# Konfiguration
FILENAME = "transactions_large.log"
NUM_ENTRIES = 100_000  # Anzahl der Zeilen
TYPES = ["DEPOSIT", "WITHDRAW", "PAYMENT"]
CURRENCIES = ["EUR", "USD", "GBP", "CHF"]


def generate_logs(filename, count):
    print(f"Generiere {count} Transaktionen in '{filename}'...")

    with open(filename, "w", encoding="utf-8") as f:
        # Header optional, falls du CSV-Stil bevorzugst
        # f.write("id,type,amount,currency\n")

        for i in range(count):
            # Daten generieren
            tx_id = f"T{1000 + i}"  # Fortlaufende ID
            tx_type = random.choice(TYPES)
            amount = round(random.uniform(1.0, 10000.0), 2)
            currency = random.choice(CURRENCIES)

            # Formatierung als Log-Zeile
            log_entry = f"ID: {tx_id} | TYPE: {tx_type} | AMOUNT: {amount:.2f} | CURRENCY: {currency}\n"

            f.write(log_entry)

            # Fortschrittsanzeige alle 10%
            if (i + 1) % (count // 10) == 0:
                print(f"Status: {((i + 1) / count) * 100:.0f}% abgeschlossen.")


if __name__ == "__main__":
    generate_logs(FILENAME, NUM_ENTRIES)
    print("Fertig! Die Datei ist bereit für die Demo.")
