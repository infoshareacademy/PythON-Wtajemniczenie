from datetime import time


def run_example():
    lessons_start = time(8, 15, 0)
    print(f"Lekcje zaczynają się o {lessons_start}")

    lessons_start = time(hour=8, minute=15, second=0)
    print(f"Lekcje zaczynają się o {lessons_start}")

    lessons_start = time(hour=8, minute=15)
    print(f"Lekcje zaczynają się o {lessons_start}")

    lessons_start = time(hour=8)
    print(f"Lekcje zaczynają się o {lessons_start}")

    lessons_start = time(minute=15)
    print(f"Lekcje zaczynają się o {lessons_start}")

    lessons_start = time(hour=8, minute=15, second=0, microsecond=1_500)
    print(f"Lekcje zaczynają się o {lessons_start}")

    # lessons_start = time(hour=8, minute=15, second=0, microsecond=1_500)
    # print(
    #     "Godziny:",
    #     lessons_start.hour,
    #     "Minuty:",
    #     lessons_start.minute,
    #     "Sekundy:",
    #     lessons_start.second,
    #     "Mikrosekundy:",
    #     lessons_start.microsecond,
    # )

    # lessons_start = time(hour=8, minute=15)
    # lessons_start.hour = 9
    # print(lessons_start)

    # high_school_lessons_start = lessons_start.replace(hour=9)
    # print(f"Lekcje zaczynają się o {lessons_start}")
    # print(f"Jednak w liceum lekcje zaczynają się godzinę później, czyli o {high_school_lessons_start}")


if __name__ == "__main__":
    run_example()
