import time

from book_book.books_directory import available_books


def rent_a_book(author: str, title: str) -> None:
    for book in available_books:
        if book.author == author and book.title == title:
            time.sleep(1)
            if book.is_available:
                time.sleep(1)
                print(f"Wypożyczenie książki: {title} powiodło się")
                book.is_available = False
                return
            else:
                print("Niestety ta książka jest już wypożyczona...")
                return 
    print("Niestety nie mamy tej książki")
