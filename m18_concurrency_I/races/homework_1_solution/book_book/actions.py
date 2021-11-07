import threading

import time

from book_book.books_directory import available_books, books_lock

print_lock = threading.Lock()


def rent_a_book(author: str, title: str) -> None:
    with books_lock:
        for book in available_books:
            if book.author == author and book.title == title:
                time.sleep(1)
                if book.is_available:
                    time.sleep(1)
                    with print_lock:
                        print(f"Wypożyczenie książki: {title} powiodło się")
                    book.is_available = False
                    return
                else:
                    with print_lock:
                        print("Niestety ta książka jest już wypożyczona...")
                    return
    with print_lock:
        print("Niestety nie mamy tej książki")
