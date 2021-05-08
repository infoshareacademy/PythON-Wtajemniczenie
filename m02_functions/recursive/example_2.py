def factorial_recursive(number):
    return number * factorial_recursive(number - 1)


def factorial_iterative(number):
    result = 1
    for current_number in range(1, number + 1):
        result *= current_number
    return result


def run_example():
    result = factorial_recursive(5)
    # result = factorial_iterative(5)
    print(result)


if __name__ == "__main__":
    run_example()
