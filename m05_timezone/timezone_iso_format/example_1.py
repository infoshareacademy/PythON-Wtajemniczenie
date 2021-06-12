from datetime import datetime, time


def run_example():
    from_iso_aware_datetime = datetime.fromisoformat("2021-01-19 18:04:38+01:00")
    print(from_iso_aware_datetime)
    print(from_iso_aware_datetime.tzinfo)

    from_iso_aware_time = time.fromisoformat("18:04:38+01:00")
    print(from_iso_aware_time)
    print(from_iso_aware_time.tzinfo)


if __name__ == '__main__':
    run_example()
