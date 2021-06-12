from datetime import datetime
from zoneinfo import ZoneInfo


def run_example():
    aware_datetime_warsaw_summer = datetime(
        year=2020, month=10, day=20, hour=10, tzinfo=ZoneInfo("Europe/Warsaw")
    )
    aware_datetime_warsaw_winter = datetime(
        year=2020, month=10, day=30, hour=10, tzinfo=ZoneInfo("Europe/Warsaw")
    )

    print(aware_datetime_warsaw_summer)
    print(aware_datetime_warsaw_winter)

    before_time_change = datetime(
        year=2020, month=10, day=25, hour=2, minute=30, tzinfo=ZoneInfo("Europe/Warsaw"), fold=0
    )

    after_time_change = datetime(
        year=2020, month=10, day=25, hour=2, minute=30, tzinfo=ZoneInfo("Europe/Warsaw"), fold=1
    )

    print(before_time_change)
    print(after_time_change)


if __name__ == "__main__":
    run_example()
