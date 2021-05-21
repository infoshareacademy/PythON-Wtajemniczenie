from datetime import date


def run_example():
    this_year_birthday = date(year=2021, month=11, day=5)
    next_year_birthday = date(
        year=this_year_birthday.year + 1, month=this_year_birthday.month, day=this_year_birthday.day
    )
    print(next_year_birthday)

    next_year_birthday = this_year_birthday.replace(year=this_year_birthday.year + 1)
    print(next_year_birthday)


if __name__ == "__main__":
    run_example()
