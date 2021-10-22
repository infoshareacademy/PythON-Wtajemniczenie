def fibonacci(number: int) -> int:
    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


def run_example() -> None:
    print(fibonacci(35))


if __name__ == "__main__":
    run_example()
