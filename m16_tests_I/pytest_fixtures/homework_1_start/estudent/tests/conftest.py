import pytest

from estudent.school import School
from estudent.student import Student


@pytest.fixture
def students() -> list[Student]:
    return [
        Student(first_name="Student-0", last_name="Test"),
        Student(first_name="Student-1", last_name="Test"),
        Student(first_name="Student-2", last_name="Test"),
        Student(first_name="Student-3", last_name="Test"),
        Student(first_name="Student-4", last_name="Test"),
    ]


@pytest.fixture
def school(students) -> School:
    for student in students:
        student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    return School(name="Test School", students=students)


@pytest.fixture
def new_student() -> Student:
    new_student = Student(first_name="Student-5", last_name="Test")
    new_student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    return new_student
