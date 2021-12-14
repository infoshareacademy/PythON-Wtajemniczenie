import random

import time

from book_book.books_directory import books_requests_queue
from book_book.rental_request import RentalRequest


def rent_a_book(author: str, title: str, renter_name: str) -> None:
    time.sleep(random.randint(0, 1))
    rental_request = RentalRequest(author=author, title=title, renter_name=renter_name)
    books_requests_queue.put(rental_request)
