from datetime import date

from book_book.book import Book

available_books = [
    Book(title="Diamond Door", author="AA", release_date=date(year=1991, month=6, day=19)),
    Book(title="The Sorcerer's Fire", author="AB", release_date=date(year=2011, month=12, day=17)),
    Book(title="Whispers Of My Leader", author="FF", release_date=date(year=2006, month=11, day=10)),
    Book(title="Tale of Servant", author="DD", release_date=date(year=1994, month=2, day=4)),
    Book(title="The Wanton Flight", author="EF", release_date=date(year=2000, month=11, day=7)),
    Book(title="Shelter At The King", author="BW", release_date=date(year=2011, month=7, day=8)),
    Book(title="Emperor of Tower", author="BB", release_date=date(year=2017, month=9, day=5)),
    Book(title="Force in the Dreaming", author="AE", release_date=date(year=1984, month=5, day=16)),
    Book(title="Healing The Beginning", author="BG", release_date=date(year=2010, month=9, day=24)),
    Book(title="Last Day of the Winter", author="HH", release_date=date(year=1980, month=10, day=4)),
]


def add_book(book):
    available_books.append(book)
