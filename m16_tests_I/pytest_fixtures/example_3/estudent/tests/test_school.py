import pytest

from estudent.school import School
from estudent.student import Student


@pytest.fixture
def new_student() -> Student:
    new_student = Student(first_name="Inny Student", last_name="Test")
    new_student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    return new_student


# @pytest.fixture
# def new_student(new_student) -> Student:
#     new_student.first_name = "Inny Student"
#     return new_student


def test_every_third_student_is_promoted_initially(school):
    assert school.students[0].promoted is True
    assert school.students[3].promoted is True

    assert school.students[1].promoted is False
    assert school.students[2].promoted is False
    assert school.students[4].promoted is False


def test_str_contains_info_about_school_and_students(school, students):
    school_str = str(school)

    assert "Szkoła: Test School, z 5 uczniami:" in school_str
    for student in students:
        assert student.first_name in school_str


def test_assign_student_to_school(school, new_student):
    school.assign_student(new_student)

    assert len(school.students) == 6
    assert new_student in school.students
    assert "Inny Student" in str(school)


def test_new_student_wont_be_assigned_when_limit_of_students_has_been_reached_already(new_student):
    students = [Student(first_name=f"Student-{index}", last_name="Test") for index in range(20)]
    school = School(name="Test School", students=students)

    with pytest.raises(ValueError) as error:
        school.assign_student(new_student)
    assert str(error.value) == "Nie ma już miejsca!"
