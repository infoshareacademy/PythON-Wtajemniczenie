from datetime import date


def run_example():
    # Tworzenie daty za pomocą konstruktora
    march_5_2020 = date(2020, 3, 5)
    march_5_2020_keywords = date(year=2020, month=3, day=5)
    march_5_2020_keywords = date(day=5, month=3, year=2020)
    future = date(year=5840, month=2, day=29)

    print(march_5_2020)
    print(march_5_2020_keywords)
    print(future)

    # Data musi być poprawna (według kalendarza gregoriańskiego)
    # april_31_2020 = date(year=2020, month=4, day=31)
    # future_wrong = date(year=5841, month=2, day=29)
    # wrong = date(year=2020, month=-2, day=30)

    # Właściwości daty
    next_birthday = date(year=2021, month=11, day=5)
    print(f"Day: {next_birthday.day}, Month: {next_birthday.month}, Year: {next_birthday.year}")

    # Obiekt date jest immutable
    # next_birthday.year = 2022
    # print(next_birthday)


if __name__ == "__main__":
    run_example()
