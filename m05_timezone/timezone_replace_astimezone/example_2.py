from datetime import datetime
from zoneinfo import ZoneInfo


def run_example():
    datetime_utc_4 = datetime.fromisoformat("2021-01-19 18:04:38+04:00")
    replace_result = datetime_utc_4.replace(tzinfo=ZoneInfo("America/New_York"))
    astimezone_result = datetime_utc_4.astimezone(tz=ZoneInfo("America/New_York"))
    print(replace_result)
    print(astimezone_result)
    print(replace_result - astimezone_result)

    # naive_datetime = datetime.fromisoformat("2021-01-19 18:04:38")
    # print(naive_datetime.astimezone(tz=ZoneInfo("America/New_York")))

    # print(datetime_utc_4.astimezone())


if __name__ == "__main__":
    run_example()
