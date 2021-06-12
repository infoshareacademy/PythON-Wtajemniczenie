from datetime import time, datetime
from zoneinfo import ZoneInfo


def run_example():
    naive_time = time(hour=10, minute=45)
    aware_time_warsaw = time(hour=10, minute=45, tzinfo=ZoneInfo("Europe/Warsaw"))
    aware_time_utc = time(hour=10, minute=45, tzinfo=ZoneInfo("UTC"))

    print(naive_time, naive_time.tzinfo)
    print(aware_time_warsaw, aware_time_warsaw.tzinfo)
    print(aware_time_utc, aware_time_utc.tzinfo)

    # aware_time_warsaw = time(hour=10, minute=45, tzinfo=ZoneInfo("Etc/GMT-2"))
    # print(aware_time_warsaw, aware_time_warsaw.tzinfo)
    #
    # before_time_change = time(hour=2, minute=30, tzinfo=ZoneInfo("Europe/Warsaw"), fold=0)
    # after_time_change = time(hour=2, minute=30, tzinfo=ZoneInfo("Europe/Warsaw"), fold=1)
    # print(before_time_change, before_time_change.tzinfo)
    # print(after_time_change, after_time_change.tzinfo)
    #
    # before_time_change = time(hour=2, minute=30, tzinfo=ZoneInfo("Etc/GMT-2"), fold=0)
    # after_time_change = time(hour=2, minute=30, tzinfo=ZoneInfo("Etc/GMT-1"), fold=1)
    # print(before_time_change, before_time_change.tzinfo)
    # print(after_time_change, after_time_change.tzinfo)

    # aware_datetime_warsaw_winter = datetime(
    #     year=2020, month=10, day=30, hour=10, tzinfo=ZoneInfo("Europe/Warsaw")
    # )
    # print(aware_time_utc.tzinfo.utcoffset(None))
    # print(aware_time_warsaw.tzinfo.utcoffset(None))
    # print(aware_datetime_warsaw_winter.tzinfo.utcoffset(aware_datetime_warsaw_winter))


if __name__ == "__main__":
    run_example()
