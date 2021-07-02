from __future__ import annotations

from typing import Callable, TypedDict, Optional

from estudent.grade import FinalGrade
from estudent.grade_calculator import GradeCalculator

FinalGradesDict = TypedDict("FinalGradesDict", {"value": int, "subject": str})
PromotionPolicyFunc = Callable[[list[FinalGrade]], bool]


class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self._final_grades: list[FinalGrade] = []

    @staticmethod
    def from_csv(
        first_name: str, last_name: str, promoted: bool, grades_values: list[int]
    ) -> Student:
        student = Student(first_name, last_name)
        student.promoted = promoted
        student._final_grades = [
            FinalGrade(value=grade_value, subject="") for grade_value in grades_values
        ]
        return student

    @staticmethod
    def from_json(
        first_name: str, last_name: str, promoted: bool, final_grades: list[FinalGradesDict],
    ) -> Student:
        student = Student(first_name, last_name)
        student.promoted = promoted
        student._final_grades = [FinalGrade(**grade) for grade in final_grades]
        return student

    def __str__(self) -> str:
        return f"Student: {self.first_name} {self.last_name}, promowany: {self.promoted}, średnia: {self.grades_avg:.2f}"

    @property
    def final_grades(self) -> list[FinalGrade]:
        return self._final_grades

    def final_grade_from_subject(self, subject: str) -> Optional[FinalGrade]:
        for final_grade in self._final_grades:
            if final_grade.subject == subject:
                return final_grade
        return None

    @property
    def grades_avg(self) -> float:
        return GradeCalculator.calculate_student_avg(self._final_grades)

    def promote(self) -> None:
        self.promoted = True
        self.add_final_grade(10, "eee", None)

    def add_final_grade(
        self,
        grade: int,
        subject: str,
        check_promotion_policy: Optional[PromotionPolicyFunc] = None,
    ) -> None:
        if check_promotion_policy is None:
            check_promotion_policy = GradeCalculator.normal_promotion_policy
        self._final_grades.append(FinalGrade(value=grade, subject=subject))

        if check_promotion_policy(self._final_grades):
            self.promoted = True
        else:
            self.promoted = False
