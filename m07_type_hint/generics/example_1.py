from collections import Sequence
from typing import TypeVar

T = TypeVar("T")


def example() -> None:
    numbers = [1, 4, 5, 2, 6, 7, 3]
    letters = ["a", "b", "x", "v", "d"]
    last_number = last_element(numbers)
    last_letter = last_element(letters)
    reveal_type(last_number)
    reveal_type(last_letter)


def last_element(sequence: Sequence[T]) -> T:
    return sequence[-1]
