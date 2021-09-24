from __future__ import annotations

from typing import cast


class Student:
    def __new__(cls, *args: str, **kwargs: str) -> Student:
        return cast(Student, super().__new__(cls))

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


def run_example() -> None:
    student_mikolaj = Student("Mikołaj", "Lewandowski")
    print(student_mikolaj)


if __name__ == "__main__":
    run_example()
