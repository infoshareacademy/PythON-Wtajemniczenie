from estudent.grade import Grade


def test_grade_above_1_is_passing():
    passing_grade = Grade(value=2)

    assert passing_grade.is_passing() is True


def test_grade_below_2_is_failing():
    failing_grade = Grade(value=1)

    assert failing_grade.is_passing() is False
