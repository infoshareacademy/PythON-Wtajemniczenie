import zoneinfo


def run_example():
    for timezone in zoneinfo.available_timezones():
        print(timezone)


if __name__ == "__main__":
    run_example()
