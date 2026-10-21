filename = "transactions_large.log"


def get_all_transactions(filename):
    results = []
    with open(filename, "r") as f:
        for line in f:
            results.append(line.strip())
    return results  # Gibt eine riesige Liste zurück


data = get_all_transactions("transactions_large.log")
print(f"Liste im RAM: {len(data)} Einträge")


def stream_transactions(filename):
    print("LOG: Stream startet...")
    with open(filename, "r") as f:
        for line in f:
            # yield pausiert die Ausführung und gibt die Zeile zurück
            yield line.strip()
    print("LOG: Stream beendet.")


# Anwendung
log_gen = stream_transactions("transactions_large.log")

print(next(log_gen))  # Holt die erste Zeile
print(next(log_gen))  # Holt die zweite Zeile

amounts_list = [
    line.split(" | ")[2] for line in stream_transactions("transactions_large.log")
]
print(amounts_list)

amounts_gen = (
    line.split("|")[2] for line in stream_transactions("transactions_large.log")
)

print(next(amounts_gen))
