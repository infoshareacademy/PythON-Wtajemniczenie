from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class Grade:
    value: int
    FAILING_GRADE: ClassVar = 1

    def is_passing(self):
        return self.value > Grade.FAILING_GRADE
    @classmethod
    def create(cls) -> Grade:
        pass


def run_example():
    variable = None
    variable = Grade(value=3)
    variable.is_passing()
    # variable = 3
    # print("Something")
    # variable.is_passing()


if __name__ == "__main__":
    run_example()
