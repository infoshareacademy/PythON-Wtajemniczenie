from datetime import datetime, time


def run_example():
    current_time = datetime.now().time()
    print("Aktualny czas:", current_time)
    moment_after = datetime.now().time()
    print("current_time < moment_after", current_time < moment_after)

    primary_school_day_end = time(hour=15, minute=0)
    secondary_school_day_end = time(hour=17, minute=0)
    print(
        "primary_school_day_end > secondary_school_day_end",
        primary_school_day_end > secondary_school_day_end,
    )


if __name__ == "__main__":
    run_example()
