from __future__ import annotations


class EvenNumbersIterator:
    def __init__(self) -> None:
        self.current_number = 0

    def __iter__(self) -> EvenNumbersIterator:
        return self

    def __next__(self) -> int:
        self.current_number += 2
        return self.current_number


def run_example() -> None:
    even_numbers_iterator = EvenNumbersIterator()
    another_even_numbers_iterator = EvenNumbersIterator()

    print(next(even_numbers_iterator))
    print(next(even_numbers_iterator))
    print(next(even_numbers_iterator))
    print(next(even_numbers_iterator))

    print(next(another_even_numbers_iterator))

    # for number in even_numbers_iterator:
    #     print(number)


if __name__ == "__main__":
    run_example()
