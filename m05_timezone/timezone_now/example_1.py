from datetime import datetime
from zoneinfo import ZoneInfo


def run_example():
    naive_today = datetime.today()
    naive_now = datetime.now()
    aware_now_pl = datetime.now(tz=ZoneInfo("Europe/Warsaw"))
    aware_now_usa = datetime.now(tz=ZoneInfo("America/New_York"))

    print(naive_today)
    print(naive_now)
    print(aware_now_pl)
    print(aware_now_usa)

    # print(aware_now_pl == aware_now_usa)
    # print(aware_now_pl.replace(microsecond=0) == aware_now_usa.replace(microsecond=0))


if __name__ == '__main__':
    run_example()
