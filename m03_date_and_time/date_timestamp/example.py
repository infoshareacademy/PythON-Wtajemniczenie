from datetime import date


def run_example():
    some_day = date.fromtimestamp(1_600_000_000)
    print(some_day)


if __name__ == "__main__":
    run_example()
