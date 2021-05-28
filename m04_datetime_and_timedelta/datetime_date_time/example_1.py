from datetime import datetime


def run_example():
    book_added_at = datetime(year=2021, month=2, day=3, hour=17, minute=5, second=19)
    print("Książkę dodano do systemu:", book_added_at, type(book_added_at))
    book_added_at_date = book_added_at.date()
    print("Data dodania książki do systemu:", book_added_at_date, type(book_added_at_date))
    book_added_at_time = book_added_at.time()
    print("Czas dodania książki do systemu:", book_added_at_time, type(book_added_at_time))


if __name__ == "__main__":
    run_example()
