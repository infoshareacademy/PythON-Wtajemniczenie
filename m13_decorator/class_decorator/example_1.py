from typing import Protocol, Type, TypeVar


class Named(Protocol):
    first_name: str
    last_name: str


T = TypeVar("T", bound=Type[Named])


def name_based_str(cls: T) -> T:
    def str_from_name(self: Named) -> str:
        return f"{self.first_name} {self.last_name}"

    # setattr(cls, "__str__", str_from_name)
    cls.__str__ = str_from_name
    return cls


@name_based_str
class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self) -> None:
        print(f"Hi my name is {self.first_name}")


def run_example() -> None:
    student_mikolaj = Student("Mikołaj", "Lewandowski")
    print(student_mikolaj)


if __name__ == "__main__":
    run_example()
