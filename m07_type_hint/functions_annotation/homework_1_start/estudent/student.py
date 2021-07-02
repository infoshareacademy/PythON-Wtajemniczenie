from __future__ import annotations

from typing import Callable

from estudent.grade import FinalGrade, Grade
from estudent.grade_calculator import GradeCalculator


class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self._final_grades = []

    @staticmethod
    def from_csv(
        first_name: str, last_name: str, promoted: bool, grades_values: list[int]
    ) -> Student:
        student = Student(first_name, last_name)
        student.promoted = promoted
        student._final_grades = [Grade(value=grade_value) for grade_value in grades_values]
        return student

    # Dict którego wartości mają różne typy?
    @staticmethod
    def from_json(
        first_name: str, last_name: str, promoted: bool, final_grades: list[dict[str, str]]
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

    def final_grade_from_subject(self, subject: str) -> FinalGrade:
        for final_grade in self._final_grades:
            if final_grade.subject == subject:
                return final_grade

    @property
    def grades_avg(self) -> float:
        return GradeCalculator.calculate_student_avg(self._final_grades)

    def promote(self) -> None:
        self.promoted = True

    # Promotion policy albo None?
    def add_final_grade(
        self,
        grade: int,
        subject: str,
        check_promotion_policy: Callable[[list[FinalGrade]], bool] = None,
    ) -> None:
        if check_promotion_policy is None:
            check_promotion_policy = GradeCalculator.normal_promotion_policy
        self._final_grades.append(FinalGrade(value=grade, subject=subject))

        if check_promotion_policy(self._final_grades):
            self.promoted = True
        else:
            self.promoted = False
