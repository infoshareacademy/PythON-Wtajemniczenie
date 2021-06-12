from datetime import datetime
from zoneinfo import ZoneInfo


def run_example():
    naive_datetime = datetime(year=2020, month=10, day=30, hour=10)
    aware_datetime_warsaw = datetime(
        year=2020, month=10, day=30, hour=10, tzinfo=ZoneInfo("Europe/Warsaw")
    )
    aware_datetime_utc = datetime(year=2020, month=10, day=30, hour=10, tzinfo=ZoneInfo("UTC"))

    print(naive_datetime)
    print(aware_datetime_warsaw)
    print(aware_datetime_utc)


if __name__ == "__main__":
    run_example()
