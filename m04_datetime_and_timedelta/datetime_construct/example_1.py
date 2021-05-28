from datetime import datetime


def run_example():
    july_15_2020_10_33 = datetime(2020, 7, 15, 10, 33, 0)
    print(july_15_2020_10_33)

    july_15_2020_10_33 = datetime(year=2020, month=7, day=15, hour=10, minute=33, second=0)
    print(july_15_2020_10_33)

    july_15_2020_10_33 = datetime(year=2020, month=7, day=15, hour=10, minute=33)
    print(july_15_2020_10_33)

    # july_15_2020_10_33 = datetime(year=2020, month=7, hour=10, minute=33)
    # print(july_15_2020_10_33)

    moment = datetime(year=2020, month=7, day=15, hour=10, minute=33)

    print(
        f"Rok: {moment.year}, Miesiąc: {moment.month}, Dzień: {moment.day}, "
        f"Godzina: {moment.hour}, Minuty: {moment.minute}, Sekundy: {moment.second}, Mikrosekundy: {moment.microsecond}"
    )

    # moment.hour = 15
    # print(moment)

    same_day_but_5_hours_later = moment.replace(hour=moment.hour + 5)
    print(same_day_but_5_hours_later)


if __name__ == "__main__":
    run_example()
