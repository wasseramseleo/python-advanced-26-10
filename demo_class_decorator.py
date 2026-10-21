import time
import functools


class TransactionAudit:
    """
    Ein Decorator (als Klasse), der die Ausführungszeit
    und den Erfolg von Kontobewegungen auditiert.
    """

    def __init__(self, func):
        # Speichert die Methode, die dekoriert wird (z.B. deposit)
        self.func = func

    def __get__(self, instance, owner):
        # Wichtig für Methoden: Bindet den Decorator an die Instanz (self)
        return functools.partial(self.__call__, instance)

    def __call__(self, instance, *args, **kwargs):
        start_time = time.perf_counter()

        # Aufruf der ursprünglichen Methode (z.B. account.deposit(amount))
        result = self.func(instance, *args, **kwargs)

        end_time = time.perf_counter()
        duration = (end_time - start_time) * 1000  # in Millisekunden

        # Audit-Log (Konsole)
        status = "ERFOLGREICH" if result else "FEHLGESCHLAGEN"
        print(f"[AUDIT] Methode '{self.func.__name__}' ausgeführt.")
        print(f"[AUDIT] Status: {status} | Dauer: {duration:.4f} ms")

        return result
