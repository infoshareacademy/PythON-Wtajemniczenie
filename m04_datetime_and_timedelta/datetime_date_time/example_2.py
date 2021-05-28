from datetime import datetime, date, time


def run_example():
    book_added_at_date = date(year=2021, month=1, day=5)
    book_added_at_time = time(hour=10, minute=25, second=37)
    print("Czas dodania książki do systemu:", book_added_at_time, type(book_added_at_time))
    print("Data dodania książki do systemu:", book_added_at_date, type(book_added_at_date))
    book_added_at = datetime.combine(book_added_at_date, book_added_at_time)
    print("Książkę dodano do systemu:", book_added_at, type(book_added_at))


if __name__ == "__main__":
    run_example()
