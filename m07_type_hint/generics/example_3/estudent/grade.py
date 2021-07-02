from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class Grade:
    value: int
    FAILING_GRADE: ClassVar[int] = 1

    def is_passing(self) -> bool:
        return self.value > Grade.FAILING_GRADE

    def __repr__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class FinalGrade(Grade):
    subject: str

    def __repr__(self) -> str:
        return f"{self.subject}: {self.value}"
