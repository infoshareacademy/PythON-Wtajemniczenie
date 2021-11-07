import threading

from book_book.book import Book

books_lock = threading.Lock()

available_books = [
    Book(author="Jan", title="O słowikach"),
    Book(author="Jan", title="O jaskółkach"),
    Book(author="Jan", title="O krukach"),
    Book(author="Jan", title="O gołębiach"),
    Book(author="Aleksandra", title="Nauka - o kosmosie"),
    Book(author="Aleksandra", title="Nauka - o górach"),
    Book(author="Karolina", title="Przygody Oli i Tomka"),
]