from account import Account
from utils import CodeTimer  # 1. Bonus-Import
import os

# --- Setup (Alte Logs löschen) ---
acc1_id = "AT001"
if os.path.exists(f"log_account_{acc1_id}.txt"):
    os.remove(f"log_account_{acc1_id}.txt")

# --- Kern-Tests (wie oben) ---
print("Führe einzelne Transaktionen durch...")
acc1 = Account(
    account_number=acc1_id, account_holder="Max Mustermann", initial_balance=500.0
)
acc1.deposit(100.0)
acc1.withdraw(50.0)


# 2. Anwendung des Bonus Context Managers
print("\nStarte Batch-Einzahlungstest...")

# Wir messen, wie lange 10 Einzahlungen dauern
# (Logging in eine Datei kann die Ausführung verlangsamen!)
with CodeTimer(name="10x Einzahlungen"):  # ruft CodeTimer.__enter__() auf
    for _ in range(10):
        acc1.deposit(1.0)
# Verlassen des with-Blocks ruft CodeTimer.__exit__() auf

print(f"Test beendet. Aktueller Saldo: {acc1.get_balance():.2f} EUR")
