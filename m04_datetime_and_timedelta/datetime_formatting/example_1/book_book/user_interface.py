from datetime import date

from book_book import books_directory, users_directory
from book_book.book import Book
from book_book.datetime_preferences import DatetimePreference
from book_book.exceptions import UserNotFound


def print_available_books(user):
    print("Aktualnie dostępne książki: ")
    for book in books_directory.available_books:
        print(book.info_with_date_format(user.datetime_preferences.value))
    _print_separator()


def add_new_book():
    print("Dodawanie nowej książki")
    print("Wprowadź podstawowe informacje o książce")
    title = input("Tytuł: ")
    author = input("Autor: ")
    release_date_input = input("Data wydania w formacie (RRRR-MM-DD, np. 2005-05-23): ")
    release_date = date.fromisoformat(release_date_input)
    book = Book(title=title, author=author, release_date=release_date)
    books_directory.add_book(book)
    _print_separator()


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


def _print_separator():
    print(20 * "-")
    print()
