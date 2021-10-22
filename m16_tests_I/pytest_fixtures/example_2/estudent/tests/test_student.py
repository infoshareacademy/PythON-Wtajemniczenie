from estudent.student import Student


def test_str_contains_required_info():
    student = Student(first_name="Student-0", last_name="Test")
    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)

    student_str = str(student)

    assert "Student-0" in student_str
    assert "Test" in student_str
    assert "promowany: False" in student_str
    assert "średnia: 5" in student_str


def test_grades_average():
    student = Student(first_name="Student-0", last_name="Test")
    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
    student.add_final_grade(grade=3, check_promotion_policy=lambda grades: False)

    assert student.grades_avg() == 4


def test_promote_student():
    student = Student(first_name="Student-0", last_name="Test")
    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)

    student.promote()

    assert student.promoted is True


def test_add_final_grade_register_new_student_grade():
    student = Student(first_name="Student-0", last_name="Test")

    student.add_final_grade(grade=5)

    assert student.grades_avg() == 5


def test_add_final_grade_uses_normal_promotion_policy_as_default():
    student = Student(first_name="Student-0", last_name="Test")

    student.add_final_grade(grade=5)

    assert student.promoted is True


def test_add_final_promote_student_when_have_proper_grades():
    student = Student(first_name="Student-0", last_name="Test")

    student.add_final_grade(grade=5, check_promotion_policy=lambda grades: grades[0].value == 5)

    assert student.promoted is True


def test_add_final_wont_promote_student_when_doesnt_have_proper_grades():
    student = Student(first_name="Student-0", last_name="Test")

    student.add_final_grade(grade=4, check_promotion_policy=lambda grades: grades[0].value == 5)

    assert student.promoted is False
