from datetime import timedelta


def run_example():
    interval = timedelta(
        days=1, seconds=1, microseconds=1, milliseconds=1, minutes=1, hours=1, weeks=1
    )
    print(interval)
    print(interval.days)
    print(interval.seconds)
    print(interval.microseconds)

    positive_interval = timedelta(seconds=10)
    negative_interval = timedelta(seconds=-10)
    print("positive_interval", positive_interval)
    print("negative_interval", negative_interval)

    print("positive_interval", positive_interval.total_seconds())
    print("negative_interval", negative_interval.total_seconds())


if __name__ == "__main__":
    run_example()
