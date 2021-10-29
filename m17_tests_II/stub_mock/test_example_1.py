import pytest
from unittest.mock import MagicMock, create_autospec


def test_as_stub():
    mock = MagicMock(return_value=10)

    assert mock("something") == 10


def test_as_stub_side_effect():
    mock = MagicMock(side_effect=ValueError("Wrong Value"))

    # mock("something")

    with pytest.raises(ValueError):
        mock()


def test_magic_mock():
    mock = MagicMock(return_value=10)

    # mock("abc")
    mock("abc")

    mock.assert_called_once()
    mock.assert_any_call("abc")
    mock.assert_called_once_with("abc")
    # mock.assert_called_once_with("XYZ")


class Grade:

    FAILING_GRADE = 1

    def __init__(self, value: int) -> None:
        self.value = value

    def is_passing(self) -> bool:
        return self.value > Grade.FAILING_GRADE

    def __repr__(self) -> str:
        return str(self.value)



def test_autospec():
    grade = Grade(value=5)
    mock = create_autospec(grade)

    mock.is_passing()
    # mock.is_passing("something")

    mock.is_passing.assert_called_once()

