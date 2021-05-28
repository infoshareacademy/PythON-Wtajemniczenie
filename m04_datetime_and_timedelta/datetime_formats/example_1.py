from datetime import datetime


def run_example():
    moment_in_time = datetime.fromordinal(256)
    print(moment_in_time)
    print(moment_in_time.toordinal())
    print(moment_in_time.weekday())
    print(moment_in_time.isoweekday())

    other_moment = datetime.fromtimestamp(16_000_000)
    print(other_moment)
    print(other_moment.timestamp())
    print(other_moment.isocalendar())


if __name__ == "__main__":
    run_example()
