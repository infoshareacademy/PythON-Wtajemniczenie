def fibonacci(number):
    if number == 0:
        return 0

    if number == 1:
        return 1

    pre_previous_value = 0
    previous_value = 1
    current_value = None

    for current_index in range(2, number + 1):
        current_value = previous_value + pre_previous_value
        pre_previous_value = previous_value
        previous_value = current_value

    return current_value


def run_example():
    result = fibonacci(6)
    print(result)


if __name__ == "__main__":
    run_example()
