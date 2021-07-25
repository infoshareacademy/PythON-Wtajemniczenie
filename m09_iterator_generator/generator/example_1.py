from collections.abc import Generator


def numbers_generator(max_number: int) -> Generator[int, None, None]:
    number = 0
    while number < max_number:
        number += 1
        yield number


def run_example() -> None:
    generator_iterator_5 = numbers_generator(max_number=5)
    generator_iterator_7 = numbers_generator(max_number=7)
    for number in generator_iterator_5:
        print(number)

    print(next(generator_iterator_7))
    print(next(generator_iterator_7))

    for number in numbers_generator(max_number=4):
        print(number)


if __name__ == "__main__":
    run_example()
