from datetime import datetime


def run_example():
    datetime_iso_string = input("Podaj datę i czas (YYYY-MM-DD hh:mm:ss): ")
    datetime_object = datetime.fromisoformat(datetime_iso_string)
    print("Rok:", datetime_object.year)
    print("Miesiąc:", datetime_object.month)
    print("Dzień:", datetime_object.day)
    print("Godziny:", datetime_object.hour)
    print("Minuty:", datetime_object.minute)
    print("Sekundy:", datetime_object.second)


if __name__ == '__main__':
    run_example()
