from estudent.grade import Grade
from estudent.grade_calculator import GradeCalculator

from unittest import TestCase


class GradeCalculatorTestCase(TestCase):
    def setUp(self):
        self.failing_grade = Grade(value=1)
        self.passing_grade = Grade(value=5)
        self.poor_grade = Grade(value=2)

    def test_normal_policy_promote_when_there_are_less_then_3_failing_grades(self):
        grades = [self.failing_grade, self.failing_grade, self.passing_grade]
        self.assertTrue(GradeCalculator.normal_promotion_policy(grades))

    def test_normal_policy_doesnt_promote_when_there_are_3_failing_grades(self):
        grades = [self.failing_grade, self.failing_grade, self.failing_grade, self.passing_grade]
        self.assertFalse(GradeCalculator.normal_promotion_policy(grades))

    def test_strict_policy_doesnt_promote_when_there_are_3_failing_grades(self):
        grades = [
            self.failing_grade,
            self.failing_grade,
            self.failing_grade,
            self.passing_grade,
            self.passing_grade,
            self.passing_grade,
        ]
        self.assertFalse(GradeCalculator.strict_promotion_policy(grades))

    def test_strict_policy_doesnt_promote_when_average_is_worse_then_3(self):
        grades = [self.poor_grade, self.poor_grade, self.poor_grade]
        self.assertFalse(GradeCalculator.strict_promotion_policy(grades))

    def test_strict_policy_promote_when_average_is_3_and_only_2_failing_grades(self):
        grades = [self.failing_grade, self.failing_grade, self.passing_grade, self.passing_grade]
        self.assertTrue(GradeCalculator.strict_promotion_policy(grades))

    def test_get_number_of_failing_grades_counts_only_failing_ones(self):
        grades = [self.failing_grade, self.passing_grade, self.failing_grade]
        self.assertEqual(GradeCalculator.get_number_of_failing_grades(grades), 2)

    def test_get_number_of_failing_grades_returns_0_when_no_grades(self):
        self.assertEqual(GradeCalculator.get_number_of_failing_grades([]), 0)

    def test_calculate_grades_avg(self):
        grades = [self.failing_grade, self.failing_grade, self.passing_grade, self.passing_grade]
        self.assertEqual(GradeCalculator.calculate_student_avg(grades), 3)
