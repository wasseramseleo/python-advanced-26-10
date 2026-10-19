"""Demo „PyCharm & Debugging“: Notenauswertung zweier Schulklassen.

Das Skript berechnet aus den Testergebnissen (in Prozent) den Schnitt jeder
Schülerin und jedes Schülers, die Note nach der österreichischen Notenskala
und den Klassenschnitt.

Achtung: Das Skript enthält absichtlich Fehler und Stilmängel. Die mit
„# Demo: …“ markierten Stellen probieren wir im Kurs gemeinsam aus.
Lassen Sie die Markierungen stehen, bis wir sie besprochen haben.

Start aus dem Lab-Ordner:
    uv run python demo_pycharm.py
"""

import os  # Demo: Inspection mit Quick-Fix
from statistics import median

# Testergebnisse in Prozent: Klasse -> Schüler/in -> Fach -> Tests
GRADEBOOK = {
    "4A": {
        "Anna Gruber": {"Mathematik": [92, 88, 95], "Englisch": [90, 94]},
        "Jonas Huber": {"Mathematik": [88, 87, 88], "Englisch": [87, 88, 88]},
        "Lena Wagner": {"Mathematik": [70, 80], "Englisch": [74, 76]},
        "Elias Pichler": {"Mathematik": [64, 58, 70], "Englisch": [61, 66]},
    },
    "4B": {
        "Sophie Berger": {"Mathematik": [45, 52], "Englisch": [48, 40]},
        "David Moser": {"Mathematik": [81, 77, 79], "Englisch": [83, 80]},
        "Marie Hofer": {"Mathematik": [97, 99], "Englisch": [94, 96]},
        "Paul Bauer": {"Mathematik": [55, 61, 58], "Englisch": []},
    },
}

# Untergrenze in Prozent -> Note (darunter: 5)
GRADE_THRESHOLDS = [(87.5, 1), (75.0, 2), (62.5, 3), (50.0, 4)]

# Demo: Reformat Code
GRADE_LABELS={1:"Sehr gut",2 :"Gut",  3:"Befriedigend",
        4 : "Genügend",5:"Nicht genügend"}


# Demo: Rename (der Funktionsname sagt nicht, was sie tut)
def calc(node: dict | list[int]) -> float:
    """Berechnet den Schnitt eines Knotens im Notenbuch.

    Eine Liste enthält Testergebnisse eines Fachs. Ein dict (Klasse,
    Schüler/in) hat als Schnitt den Mittelwert der Schnitte seiner Einträge.
    """
    if isinstance(node, list):
        # Demo: Watches und Evaluate Expression
        return sum(node) // len(node)
    # Demo: Call Stack (rekursiver Aufruf)
    child_averages = [calc(child) for child in node.values()]
    return sum(child_averages) / len(child_averages)


# Demo: Type-Hint-Warnung
def percent_to_grade(percent: float) -> str:
    """Wandelt einen Schnitt in Prozent in eine Note von 1 bis 5 um."""
    for threshold, grade in GRADE_THRESHOLDS:
        if percent > threshold:
            return grade  # Demo: Run to Cursor
    return 5


def print_header() -> None:
    print("Notenauswertung Schuljahr 2026/27")
    scale = ", ".join(
        f"ab {threshold} % {GRADE_LABELS[grade]}"
        for threshold, grade in GRADE_THRESHOLDS
    )
    print(f"Notenskala: {scale}, darunter {GRADE_LABELS[5]}")
    print()


def print_summary(averages: dict[str, float]) -> None:
    best_name = max(averages, key=averages.__getitem__)
    print(f"Bester Schnitt: {best_name} ({averages[best_name]:.1f} %)")
    # Demo: Go to Definition (auch in die Standardbibliothek)
    print(f"Median aller Schnitte: {median(averages.values()):.1f} %")


def main() -> None:
    print_header()
    averages: dict[str, float] = {}
    id = 0  # Demo: Inspection mit Quick-Fix
    for class_name, students in GRADEBOOK.items():
        for student_name, subjects in students.items():
            id += 1
            average = calc(subjects)  # Demo: Breakpoint, Step Over/Into/Out
            grade = percent_to_grade(average)  # Demo: bedingter Breakpoint
            averages[student_name] = average

            # Demo: Extract Method (die nächsten drei Zeilen)
            label = GRADE_LABELS[grade]
            marker = "  <- Nachprüfung" if grade == 5 else ""
            print(f"{id:>2}. {student_name:<14} {class_name}  {average:5.1f} %  {grade} ({label}){marker}")

        print(f"    Klassenschnitt {class_name}: {calc(students):.1f} %")
        print()
    print_summary(averages)


if __name__ == "__main__":
    main()
