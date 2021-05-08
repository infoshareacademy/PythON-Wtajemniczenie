def fibonacci(number):
    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


def run_example():
    result = fibonacci(6)
    print(result)


if __name__ == "__main__":
    run_example()
