from estudent.student import Student


from unittest import TestCase


class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student(first_name="Student-0", last_name="Test")
        self.student_with_grade = Student(first_name="Student-0", last_name="Test")
        self.student_with_grade.add_final_grade(
            grade=5, check_promotion_policy=lambda grades: False
        )

    def test_str_contains_required_info(self):
        student_str = str(self.student_with_grade)

        self.assertIn("Student-0", student_str)
        self.assertIn("Test", student_str)
        self.assertIn("promowany: False", student_str)
        self.assertIn("średnia: 5", student_str)

    def test_grades_average(self):
        student = self.student
        student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
        student.add_final_grade(grade=3, check_promotion_policy=lambda grades: False)

        self.assertEqual(student.grades_avg(), 4)

    def test_promote_student(self):
        self.student_with_grade.promote()

        self.assertTrue(self.student_with_grade.promoted)

    def test_add_final_grade_register_new_student_grade(self):
        self.student.add_final_grade(grade=5)

        self.assertEqual(self.student.grades_avg(), 5)

    def test_add_final_grade_uses_normal_promotion_policy_as_default(self):
        self.student.add_final_grade(grade=5)

        self.assertTrue(self.student.promoted)

    def test_add_final_promote_student_when_have_proper_grades(self):
        self.student.add_final_grade(
            grade=5, check_promotion_policy=lambda grades: grades[0].value == 5
        )

        self.assertTrue(self.student.promoted)

    def test_add_final_wont_promote_student_when_doesnt_have_proper_grades(self):
        self.student.add_final_grade(
            grade=4, check_promotion_policy=lambda grades: grades[0].value == 5
        )

        self.assertFalse(self.student.promoted)
