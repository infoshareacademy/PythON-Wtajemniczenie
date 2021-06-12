from datetime import datetime, date, time
from zoneinfo import ZoneInfo


def run_example():
    naive_date = date.fromisoformat("2021-01-19")
    naive_time = time.fromisoformat("18:04:38")
    aware_time = time.fromisoformat("18:04:38+01:00")

    # naive time + no timezone = naive datetime
    print(datetime.combine(naive_date, naive_time))

    # naive time + timezone = aware datetime
    print(datetime.combine(naive_date, naive_time, tzinfo=ZoneInfo("America/New_York")))

    # aware time + no timezone = aware datetime
    print(datetime.combine(naive_date, aware_time))


if __name__ == "__main__":
    run_example()
