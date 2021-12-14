import time
import queue

from book_book.book import Book
from book_book.printer import print_text
from book_book.rental_request import RentalRequest

books_requests_queue: queue.Queue[RentalRequest] = queue.Queue()

available_books = [
    Book(author="Jan", title="O słowikach"),
    Book(author="Jan", title="O jaskółkach"),
    Book(author="Jan", title="O krukach"),
    Book(author="Jan", title="O gołębiach"),
    Book(author="Aleksandra", title="Nauka - o kosmosie"),
    Book(author="Aleksandra", title="Nauka - o górach"),
    Book(author="Karolina", title="Przygody Oli i Tomka"),
]


def books_manager() -> None:
    while True:
        rental_request = books_requests_queue.get()
        author = rental_request.author
        title = rental_request.title
        renter_name = rental_request.renter_name
        for book in available_books:
            if book.author == author and book.title == title:
                time.sleep(1)
                if book.is_available:
                    time.sleep(1)
                    print_text(f"Wypożyczenie książki: {title} przez {renter_name} powiodło się")
                    book.is_available = False
                    break
                else:
                    print_text(
                        f"{renter_name} - niestety ta książka ({title}) jest już wypożyczona..."
                    )
                    break
        else:
            print(f"Niestety nie mamy tej książki ({title})")
        books_requests_queue.task_done()
