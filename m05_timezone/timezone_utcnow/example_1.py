from datetime import datetime
from zoneinfo import ZoneInfo


def run_example():
    utc_but_naive = datetime.utcnow()
    utc_aware = datetime.now(ZoneInfo("UTC"))

    print(utc_but_naive)
    print(utc_aware)

    print(utc_but_naive.astimezone(ZoneInfo("Europe/Warsaw")))
    print(utc_aware.astimezone(ZoneInfo("Europe/Warsaw")))


if __name__ == "__main__":
    run_example()
