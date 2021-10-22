from estudent.school import School
from estudent.student import Student


def test_every_third_student_is_promoted_initially():
    students = [
        Student(first_name="Student-0", last_name="Test"),
        Student(first_name="Student-1", last_name="Test"),
        Student(first_name="Student-2", last_name="Test"),
        Student(first_name="Student-3", last_name="Test"),
        Student(first_name="Student-4", last_name="Test"),
    ]

    # Czy testować w ogóle __init__ ?
    school = School(name="Test School", students=students)

    # Jaki jest limit asercji na test?
    assert school.students[0].promoted is True
    assert school.students[3].promoted is True

    assert school.students[1].promoted is False
    assert school.students[2].promoted is False
    assert school.students[4].promoted is False


def test_str():
    students = [
        Student(first_name="Student-0", last_name="Test"),
        Student(first_name="Student-1", last_name="Test"),
        Student(first_name="Student-2", last_name="Test"),
        Student(first_name="Student-3", last_name="Test"),
        Student(first_name="Student-4", last_name="Test"),
    ]
    for student in students:
        student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    school = School(name="Test School", students=students)

    # 1) Czy testować w ogóle str?
    # 2) Problematyczna asercja w przypadku długiego tekstu
    assert str(school) == "Szkoła: Test School, z 5 uczniami: \n ..."


def test_str_contains_info_about_school_and_students():
    students = [
        Student(first_name="Student-0", last_name="Test"),
        Student(first_name="Student-1", last_name="Test"),
        Student(first_name="Student-2", last_name="Test"),
        Student(first_name="Student-3", last_name="Test"),
        Student(first_name="Student-4", last_name="Test"),
    ]
    for student in students:
        student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    school = School(name="Test School", students=students)

    # Str wykonany jednorazowo - większa czytelność i darmowa optymalizacja
    school_str = str(school)

    assert "Szkoła: Test School, z 5 uczniami:" in school_str
    assert students[0].first_name in school_str
    assert students[1].first_name in school_str

    # Asercje w pętli?
    # for student in students:
    #     assert student.first_name in school_str


def test_assign_student_to_school():
    students = [
        Student(first_name="Student-0", last_name="Test"),
        Student(first_name="Student-1", last_name="Test"),
        Student(first_name="Student-2", last_name="Test"),
        Student(first_name="Student-3", last_name="Test"),
        Student(first_name="Student-4", last_name="Test"),
    ]
    for student in students:
        student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    school = School(name="Test School", students=students)
    new_student = Student(first_name="Student-5", last_name="Test")
    new_student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)

    school.assign_student(new_student)

    assert len(school.students) == 6
    assert new_student in school.students
    assert "Student-5" in str(school)


# def test_new_student_wont_be_assigned_when_limit_of_students_has_been_reached_already():
#     students = [
#         Student(first_name=f"Student-{index}", last_name="Test") for index in range(20)
#     ]
#     school = School(name="Test School", students=students)
#     new_student = Student(first_name="Student-5", last_name="Test")
#
#     # Aserscja na wyjątek?
#     school.assign_student(new_student)


# Czy testować prywatne części obiektu?
def test_promote_lucky_students():
    students = [
        Student(first_name="Student-0", last_name="Test"),
        Student(first_name="Student-1", last_name="Test"),
        Student(first_name="Student-2", last_name="Test"),
        Student(first_name="Student-3", last_name="Test"),
        Student(first_name="Student-4", last_name="Test"),
    ]
    school = School(name="Test School", students=[])
    school.students = students

    school._promote_lucky_students()

    assert school.students[0].promoted is True
    assert school.students[3].promoted is True
