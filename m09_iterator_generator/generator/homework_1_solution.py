from __future__ import annotations

from collections.abc import Generator


def fibonacci_generator(number_of_elements: int) -> Generator[int, None, None]:
    previous_element = 0
    current_element = 1
    current_element_index = 1
    while current_element_index <= number_of_elements:
        current_element_index += 1
        new_current_element = previous_element + current_element
        previous_element = current_element
        current_element = new_current_element
        yield current_element
        # current_element_index += 1
        # current_element, previous_element = previous_element + current_element, current_element
        # yield current_element


def run_example() -> None:
    fibo_8 = fibonacci_generator(8)
    for element in fibo_8:
        print(element)
    print(20 * "-")
    for element in fibo_8:
        print(element)


if __name__ == "__main__":
    run_example()
