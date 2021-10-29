import pytest

from estudent.student import Student

@pytest.fixture
def student() -> Student:
    return Student(first_name="Student-0", last_name="Test")

@pytest.fixture
def student_with_grade(student) -> Student:
    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    return student


def test_str_contains_required_info(student_with_grade):
    student_str = str(student_with_grade)

    assert "Student-0" in student_str
    assert "Test" in student_str
    assert "promowany: False" in student_str
    assert "średnia: 5" in student_str


def test_grades_average(student):
    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    student.add_final_grade(grade=3, check_promotion_policy=lambda grades: False)

    assert student.grades_avg() == 4


def test_promote_student(student_with_grade):
    student_with_grade.promote()

    assert student_with_grade.promoted is True


def test_add_final_grade_register_new_student_grade(student):
    student.add_final_grade(grade=5)

    assert student.grades_avg() == 5


def test_add_final_grade_uses_normal_promotion_policy_as_default(student):
    student.add_final_grade(grade=5)

    assert student.promoted is True


def test_add_final_promote_student_when_have_proper_grades(student):
    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: grades[0].value == 5)

    assert student.promoted is True


def test_add_final_wont_promote_student_when_doesnt_have_proper_grades(student):
    student.add_final_grade(grade=4, check_promotion_policy=lambda grades: grades[0].value == 5)

    assert student.promoted is False
