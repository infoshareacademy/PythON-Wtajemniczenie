# Wykorzystaj type do dynamicznego zadeklarowania własnej klasy.
# Klasa powinna nazywać się Student oraz posiadać pola first_name oraz last_name. Utwórz obiekt tej klasy.

from typing import Any


def _student__init__(self: Any, first_name: str, last_name: str) -> None:
    self.first_name = first_name
    self.last_name = last_name


Student = type("Student", (), {"__init__": _student__init__})


def run_example() -> None:
    student_mikolaj = Student("Mikołaj", "Lewandowski")
    print(student_mikolaj.first_name)
    print(student_mikolaj.last_name)


if __name__ == "__main__":
    run_example()
