from collections.abc import Sequence
from typing import Optional, Callable

from estudent.grade import Grade
from estudent.grade_calculator import GradeCalculator

PromotionPolicy = Callable[[Sequence[Grade]], bool]


class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self._final_grades: list[Grade] = []

    def __str__(self) -> str:
        return f"Student: {self.first_name} {self.last_name}, promowany: {self.promoted}, średnia: {self.grades_avg():.2f}"

    def grades_avg(self) -> float:
        return GradeCalculator.calculate_student_avg(self._final_grades)

    def promote(self) -> None:
        self.promoted = True

    def add_final_grade(
        self, grade: int, check_promotion_policy: Optional[PromotionPolicy] = None
    ) -> None:
        if check_promotion_policy is None:
            check_promotion_policy = GradeCalculator.normal_promotion_policy
        self._final_grades.append(Grade(value=grade))
        if check_promotion_policy(self._final_grades):
            self.promoted = True
        else:
            self.promoted = False
