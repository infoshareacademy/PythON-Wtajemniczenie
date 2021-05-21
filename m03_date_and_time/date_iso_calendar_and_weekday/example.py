from datetime import date


def run_example():
    march_2020_15 = date(year=2020, month=3, day=15)
    print("march_2020_15.toordinal():", march_2020_15.toordinal())
    print("march_2020_15.isocalendar():", march_2020_15.isocalendar())


if __name__ == "__main__":
    run_example()
