from typing import Any


class DummyMetaclass(type):
    def __new__(mcs, name: str, bases: tuple[type], class_dict: dict[str, Any]) -> Any:
        print(f"Creating class definition: {name}")
        print(f"Class bases: {bases}")
        print(f"Class dict: {class_dict}")
        return super().__new__(mcs, name, bases, class_dict)


class Student(metaclass=DummyMetaclass):
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
