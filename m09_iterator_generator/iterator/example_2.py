from __future__ import annotations


class EvenNumbersIterator:
    def __init__(self, max_number: int) -> None:
        self.max_number = max_number
        self.current_number = 0

    def __iter__(self) -> EvenNumbersIterator:
        return self

    def __next__(self) -> int:
        self.current_number += 2
        if self.current_number > self.max_number:
            raise StopIteration()
        return self.current_number


def run_example() -> None:
    even_numbers_iterator = EvenNumbersIterator(6)
    another_even_numbers_iterator = EvenNumbersIterator(20)

    for number in even_numbers_iterator:
        print(number)

    # print(next(even_numbers_iterator))

    # for number in another_even_numbers_iterator:
    #     print(number)


if __name__ == "__main__":
    run_example()
