def example_func(pos_1, pos_2, /, pos_or_key):
    print(pos_1, pos_2, pos_or_key)


def run_example():
    example_func(5, 10, 15)
    example_func(5, 10, pos_or_key=15)
    # example_func(5, pos_2=10, pos_or_key=15)
    # example_func(pos_1=5, pos_2=10, pos_or_key=15)


if __name__ == '__main__':
    run_example()
