from special_accounts import SavingsAccount, CheckingAccount
from account import Account  # Optional für Vergleich

# 1. Test der Basisklasse (wie in Lab 1)
print("--- Test Basis-Account ---")
acc_base = Account("AT001", "Basis Kunde", 100.0)
acc_base.withdraw(50.0)
print(acc_base)


# 5. Test der Subklasse SavingsAccount
print("\n--- Test SavingsAccount ---")
# Erstellen eines SavingsAccount-Objekts
# Beachten Sie das zusätzliche Argument 'interest_rate'
sa1 = SavingsAccount(
    account_number="AT100",
    account_holder="Ina Sparfuchs",
    initial_balance=1000.0,
    interest_rate=0.05,  # 5% Zinsen
)

print(sa1)  # Nutzt die __str__ Methode von Account (geerbt)

# 5. Test der neuen Methode 'apply_interest'
sa1.apply_interest()  # Sollte 50.0 EUR Zinsen hinzufügen
print(f"Neuer Stand nach Zinsen: {sa1.get_balance():.2f} EUR")  # Erwartet: 1050.0

# 5. Test der geerbten Methode 'withdraw'
sa1.withdraw(200.0)
print(f"Neuer Stand nach Abhebung: {sa1.get_balance():.2f} EUR")  # Erwartet: 850.0


# Bonus: Test der Subklasse CheckingAccount
print("\n--- Test CheckingAccount (Bonus) ---")
ca1 = CheckingAccount(
    account_number="AT200",
    account_holder="Gabi Giro",
    initial_balance=100.0,
    overdraft_limit=500.0,
)
print("Verfügbares Limit: (100 Saldo + 500 Dispo) = 600 EUR")

# Test der überschriebenen 'withdraw'-Methode
print("\nVersuche Abhebung von 300 EUR (sollte gelingen):")
ca1.withdraw(300.0)
print(f"Aktueller Saldo: {ca1.get_balance():.2f} EUR")  # Erwartet: -200.0

print("\nVersuche Abhebung von 400 EUR (sollte scheitern):")
# Verfügbar sind nur noch: -200 (Saldo) + 500 (Dispo) = 300 EUR
ca1.withdraw(400.0)
print(f"Aktueller Saldo: {ca1.get_balance():.2f} EUR")  # Erwartet: -200.0

print("\nTeste die geerbte 'deposit'-Methode:")
ca1.deposit(1000.0)  # Saldo steigt von -200 auf 800
print(f"Aktueller Saldo: {ca1.get_balance():.2f} EUR")
