# Stwórz prostą metaklasę, która wypisuje dane otrzymane w argumentach metody __new__
# Utwórz dwie klasy wykorzystujące tę metaklasę. Utwórz obiekty tych klas.
# Zwróć uwagę na to w którym momencie wywoływana jest metoda __new__ metaklasy.

from typing import Any


class SimpleMetaclass(type):
    def __new__(mcs, name: str, bases: tuple[type], class_dict: dict[str, Any]) -> Any:
        print(f"Creating class definition: {name}")
        print(f"Class bases: {bases}")
        print(f"Class dict: {class_dict}")
        return super().__new__(mcs, name, bases, class_dict)


class Human(metaclass=SimpleMetaclass):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(metaclass=SimpleMetaclass):

    MIN_ALLOWED_RATE = 1
    MAX_ALLOWED_RATE = 5

    def __init__(self, name: str, category: str) -> None:
        self.name = name
        self.category = category
        self._rates: list[int] = []
        self._viewers: list[str] = []

    def __str__(self) -> str:
        return f"{self.name} - {self.category} Movie, rate: {self.rate:.2f}"

    @property
    def rate(self) -> float:
        if len(self._viewers):
            return sum(self._rates) / len(self._viewers)
        return 0

    def vote(self, viewer_name: str, rate: int) -> None:
        self._viewers.append(viewer_name)
        self._rates.append(rate)


def run_example() -> None:
    print("Zaczynamy!")
    jan_kowalski = Human("Jan", "Kowalski")
    example_movie = Movie("Magic stone", "Fantasy")
    print(jan_kowalski)
    print(example_movie)


if __name__ == "__main__":
    run_example()
