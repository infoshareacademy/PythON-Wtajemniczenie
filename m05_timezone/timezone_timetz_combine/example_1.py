from datetime import datetime


def run_example():
    aware_datetime = datetime.fromisoformat("2021-01-19 18:04:38+01:00")
    print(aware_datetime)

    print(aware_datetime.time())
    print(aware_datetime.timetz())


if __name__ == "__main__":
    run_example()
