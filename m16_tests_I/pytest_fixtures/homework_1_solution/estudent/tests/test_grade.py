def test_grade_above_1_is_passing(passing_grade):
    assert passing_grade.is_passing() is True


def test_grade_below_2_is_failing(failing_grade):
    assert failing_grade.is_passing() is False
