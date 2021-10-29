from estudent.school import School
from estudent.student import Student


from unittest import TestCase


class SchoolTestCase(TestCase):
    def setUp(self):
        self.students = [
            Student(first_name="Student-0", last_name="Test"),
            Student(first_name="Student-1", last_name="Test"),
            Student(first_name="Student-2", last_name="Test"),
            Student(first_name="Student-3", last_name="Test"),
            Student(first_name="Student-4", last_name="Test"),
        ]
        for student in self.students:
            student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)
        self.school = School(name="Test School", students=self.students)

        self.new_student = Student(first_name="Student-5", last_name="Test")
        self.new_student.add_final_grade(grade=5, check_promotion_policy=lambda grades: False)

    def test_every_third_student_is_promoted_initially(self):
        self.assertTrue(self.school.students[0].promoted)
        self.assertTrue(self.school.students[3].promoted)

        self.assertFalse(self.school.students[1].promoted)
        self.assertFalse(self.school.students[2].promoted)
        self.assertFalse(self.school.students[4].promoted)

    def test_str_contains_info_about_school_and_students(self):
        school_str = str(self.school)

        self.assertIn("Szkoła: Test School, z 5 uczniami:", school_str)
        for student in self.students:
            self.assertIn(student.first_name, school_str)

    def test_assign_student_to_school(self):
        self.school.assign_student(self.new_student)

        self.assertEqual(len(self.school.students), 6)
        self.assertIn(self.new_student, self.school.students)

    def test_new_student_wont_be_assigned_when_limit_of_students_has_been_reached_already(self):
        students = [Student(first_name=f"Student-{index}", last_name="Test") for index in range(20)]
        school = School(name="Test School", students=students)

        with self.assertRaises(ValueError) as raises_context:
            school.assign_student(self.new_student)
        self.assertEqual(str(raises_context.exception), "Nie ma już miejsca!")
