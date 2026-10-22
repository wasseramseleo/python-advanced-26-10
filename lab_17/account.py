import datetime

from exceptions import InvalidAmountError, InsufficientFundsError


class Account:
    """
    Bankkonto auf dem Stand von Lab 4: Fehler werden als Exceptions
    ausgelöst, jede Transaktion wird in eine Log-Datei geschrieben.
    """

    def __init__(
        self, account_number: str, account_holder: str, initial_balance: float = 0.0
    ):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_balance
        self.log_file_path = f"log_account_{self.account_number}.txt"
        self._log_transaction(
            f"Konto erstellt mit Startsaldo: {initial_balance:.2f} EUR"
        )

    def _log_transaction(self, message: str):
        """Schreibt eine Nachricht mit Zeitstempel in die Log-Datei."""
        timestamp = datetime.datetime.now().isoformat()
        log_entry = f"[{timestamp}] {message}\n"
        try:
            with open(self.log_file_path, mode="a", encoding="utf-8") as f:
                f.write(log_entry)
        except IOError as e:
            print(f"WARNUNG: Logging fehlgeschlagen: {e}")

    def deposit(self, amount: float):
        """
        Zahlt einen Betrag ein.
        Löst InvalidAmountError bei ungültigem Betrag aus.
        """
        if amount <= 0:
            msg = f"Einzahlung fehlgeschlagen: Betrag ({amount:.2f} EUR) muss positiv sein."
            self._log_transaction(msg)
            raise InvalidAmountError(msg)

        self._balance += amount
        print(f"Einzahlung von {amount:.2f} EUR erfolgreich.")
        self._log_transaction(
            f"Einzahlung: +{amount:.2f} EUR. Neuer Saldo: {self._balance:.2f} EUR"
        )

    def withdraw(self, amount: float):
        """
        Hebt einen Betrag ab.
        Löst InvalidAmountError oder InsufficientFundsError aus.
        """
        if amount <= 0:
            msg = (
                f"Abhebung fehlgeschlagen: Betrag ({amount:.2f} EUR) muss positiv sein."
            )
            self._log_transaction(msg)
            raise InvalidAmountError(msg)

        if self._balance < amount:
            msg = f"Abhebung fehlgeschlagen. Guthaben nicht ausreichend. Benötigt: {amount:.2f} EUR, Verfügbar: {self._balance:.2f} EUR"
            self._log_transaction(msg)
            raise InsufficientFundsError(msg)

        self._balance -= amount
        print(f"Abhebung von {amount:.2f} EUR erfolgreich.")
        self._log_transaction(
            f"Abhebung: -{amount:.2f} EUR. Neuer Saldo: {self._balance:.2f} EUR"
        )

    def get_balance(self) -> float:
        return self._balance

    def __str__(self) -> str:
        return f"Konto {self.account_number} (Inhaber: {self.account_holder}), Stand: {self._balance:.2f} EUR"
