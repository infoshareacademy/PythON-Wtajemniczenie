from datetime import datetime

from book_book import books_directory, users_directory
from book_book.book import Book
from book_book.datetime_preferences import DatetimePreference
from book_book.exceptions import UserNotFound


def login():
    while True:
        user_login = input("Podaj login: ")
        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            print("Nie znaleziono użytkownika o podanym loginie - spróbuj ponownie")


def select_datetime_preferences(user):
    print("Dostępne formaty daty i czasu:")
    for option_index, datetime_preference in enumerate(DatetimePreference):
        print(f"{option_index}) {datetime_preference}")

    selected_option = int(input("Wybierz opcje: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(selected_option)


def find_books_by_added_at_datetime(user):
    date_and_time_format = user.datetime_preferences.value
    print("Podaj daty dodania, pomiędzy którymi szukać książek")
    print(f"W formacie {date_and_time_format.datetime_format}")
    start_band_input = input("Książki dodane później niż: ")
    start_datetime_band = datetime.strptime(start_band_input, date_and_time_format.datetime_format)
    end_band_input = input("Książki dodane wcześniej niż: ")
    end_datetime_band = datetime.strptime(end_band_input, date_and_time_format.datetime_format)

    for book in books_directory.available_books:
        if start_datetime_band <= book.added_at_datetime <= end_datetime_band:
            print(book.info_with_date_format(user.datetime_preferences.value))


def print_available_books(user):
    print("Aktualnie dostępne książki: ")
    for book in books_directory.available_books:
        print(book.info_with_date_format(user.datetime_preferences.value))
    _print_separator()


def add_new_book(user):
    print("Dodawanie nowej książki")
    print("Wprowadź podstawowe informacje o książce")
    title = input("Tytuł: ")
    author = input("Autor: ")
    date_and_time_format = user.datetime_preferences.value
    release_date_input = input(f"Data wydania w formacie ({date_and_time_format.date_format}): ")
    release_date = datetime.strptime(release_date_input, date_and_time_format.date_format).date()
    book = Book(title=title, author=author, release_date=release_date)
    books_directory.add_book(book)
    _print_separator()


def _print_separator():
    print(20 * "-")
    print()
