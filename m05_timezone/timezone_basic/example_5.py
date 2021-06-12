from datetime import time, datetime
from zoneinfo import ZoneInfo


def run_example():
    utc_time = datetime(year=2021, month=4, day=5, hour=3, minute=20, tzinfo=ZoneInfo("UTC"))
    poland_time = datetime(
        year=2021, month=4, day=5, hour=5, minute=20, tzinfo=ZoneInfo("Europe/Warsaw")
    )
    new_york_time_1 = datetime(
        year=2021, month=4, day=4, hour=20, minute=50, tzinfo=ZoneInfo("America/New_York")
    )
    new_york_time_2 = datetime(
        year=2021, month=4, day=4, hour=23, minute=50, tzinfo=ZoneInfo("America/New_York")
    )

    print(utc_time)
    print(poland_time)
    print(new_york_time_1)
    print(new_york_time_2)

    print("utc_time < poland_time", utc_time < poland_time)
    print("utc_time == poland_time", utc_time == poland_time)
    print("new_york_time_1 > poland_time", new_york_time_1 > poland_time)
    print("new_york_time_2 > poland_time", new_york_time_2 > poland_time)


if __name__ == "__main__":
    run_example()
