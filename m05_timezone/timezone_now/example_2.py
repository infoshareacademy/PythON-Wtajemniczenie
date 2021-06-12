from datetime import datetime
from zoneinfo import ZoneInfo


def run_example():
    timestamp = 1611075878
    naive = datetime.fromtimestamp(timestamp)
    aware_pl = datetime.fromtimestamp(timestamp, tz=ZoneInfo("Europe/Warsaw"))
    aware_usa = datetime.fromtimestamp(timestamp, tz=ZoneInfo("America/New_York"))

    print(naive)
    print(aware_pl)
    print(aware_usa)

    # print(aware_pl == aware_usa)
    # print(aware_pl == naive)
    # print(aware_pl > naive)



if __name__ == "__main__":
    run_example()
