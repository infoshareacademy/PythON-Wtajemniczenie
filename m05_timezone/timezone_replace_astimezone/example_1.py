from datetime import datetime
from zoneinfo import ZoneInfo


def run_example():
    datetime_utc_4 = datetime.fromisoformat("2021-01-19 18:04:38+04:00")
    print(datetime_utc_4.replace(tzinfo=ZoneInfo("America/New_York")))

    naive_datetime = datetime.fromisoformat("2021-01-19 18:04:38")
    print(naive_datetime.replace(tzinfo=ZoneInfo("America/New_York")))

    time_utc_4 = datetime_utc_4.timetz()
    print(time_utc_4.replace(tzinfo=ZoneInfo("UTC")))


if __name__ == "__main__":
    run_example()
