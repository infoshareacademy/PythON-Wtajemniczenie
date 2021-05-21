from datetime import date

from book_book import books_directory
from book_book.book import Book


def print_available_books():
    print("Aktualnie dostępne książki: ")
    for book in books_directory.available_books:
        print(book)
    _print_separator()


def add_new_book():
    print("Dodawanie nowej książki")
    print("Wprowadź podstawowe informacje o książce")
    title = input("Tytuł: ")
    author = input("Autor: ")
    year = int(input("Rok wydania: "))
    month = int(input("Miesiąc wydania: "))
    day = int(input("Dzień wydania: "))
    book = Book(title=title, author=author, release_date=date(year=year, month=month, day=day))
    books_directory.add_book(book)
    _print_separator()

#
# def add_new_book():
#     print("Dodawanie nowej książki")
#     print("Wprowadź podstawowe informacje o książce")
#     title = input("Tytuł: ")
#     author = input("Autor: ")
#     release_date_input = input("Data wydania w formacie (RRRR-MM-DD, np. 2005-05-23): ")
#     release_date = date.fromisoformat(release_date_input)
#     book = Book(title=title, author=author, release_date=release_date)
#     books_directory.add_book(book)
#     _print_separator()


def _print_separator():
    print(20 * "-")
    print()
