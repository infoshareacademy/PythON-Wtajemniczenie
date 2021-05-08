def example_func(pos_or_key_1, pos_or_key_2, pos_or_key_3):
    print(pos_or_key_1, pos_or_key_2, pos_or_key_3)


def run_example():
    example_func(5, 10, 15)
    example_func(5, 10, pos_or_key_3=15)
    example_func(5, pos_or_key_2=10, pos_or_key_3=15)
    example_func(pos_or_key_1=5, pos_or_key_2=10, pos_or_key_3=15)


if __name__ == '__main__':
    run_example()
