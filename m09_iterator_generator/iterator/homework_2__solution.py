from __future__ import annotations


class FibonacciIterator:
    def __init__(self, max_element_number: int) -> None:
        self.previous_element = 0
        self.current_element = 1
        self.current_element_number = 1
        self.max_element_number = max_element_number

    def __iter__(self) -> FibonacciIterator:
        return self

    def __next__(self) -> int:
        if self.current_element_number > self.max_element_number:
            raise StopIteration()
        self.current_element_number += 1
        current_element = self.previous_element + self.current_element
        self.previous_element = self.current_element
        self.current_element = current_element
        return current_element


def run_example() -> None:
    fibo_8 = FibonacciIterator(8)
    for element in fibo_8:
        print(element)
    print(20 * "-")
    for element in fibo_8:
        print(element)


if __name__ == "__main__":
    run_example()
