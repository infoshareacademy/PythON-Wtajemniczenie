from estudent.grade import Grade
from estudent.grade_calculator import GradeCalculator


def test_normal_policy_promote_when_there_are_less_then_3_failing_grades():
    failing_grade = Grade(value=1)
    passing_grade = Grade(value=5)
    grades = [failing_grade, failing_grade, passing_grade]
    assert GradeCalculator.normal_promotion_policy(grades) is True


def test_normal_policy_doesnt_promote_when_there_are_3_failing_grades():
    failing_grade = Grade(value=1)
    passing_grade = Grade(value=5)
    grades = [failing_grade, failing_grade, failing_grade, passing_grade]
    assert GradeCalculator.normal_promotion_policy(grades) is False


def test_strict_policy_doesnt_promote_when_there_are_3_failing_grades():
    failing_grade = Grade(value=1)
    passing_grade = Grade(value=5)
    grades = [failing_grade, failing_grade, failing_grade, passing_grade, passing_grade, passing_grade]
    assert GradeCalculator.strict_promotion_policy(grades) is False


def test_strict_policy_doesnt_promote_when_average_is_worse_then_3():
    poor_grade = Grade(value=2)
    grades = [poor_grade, poor_grade, poor_grade]
    assert GradeCalculator.strict_promotion_policy(grades) is False


def test_strict_policy_promote_when_average_is_3_and_only_2_failing_grades():
    failing_grade = Grade(value=1)
    passing_grade = Grade(value=5)
    grades = [failing_grade, failing_grade, passing_grade, passing_grade]
    assert GradeCalculator.strict_promotion_policy(grades) is True


def test_get_number_of_failing_grades_counts_only_failing_ones():
    failing_grade = Grade(value=1)
    passing_grade = Grade(value=5)
    grades = [failing_grade, passing_grade, failing_grade]
    assert GradeCalculator.get_number_of_failing_grades(grades) == 2


def test_get_number_of_failing_grades_returns_0_when_no_grades():
    assert GradeCalculator.get_number_of_failing_grades([]) == 0


def test_calculate_grades_avg():
    failing_grade = Grade(value=1)
    passing_grade = Grade(value=5)
    grades = [failing_grade, failing_grade, passing_grade, passing_grade]
    assert GradeCalculator.calculate_student_avg(grades) == 3

