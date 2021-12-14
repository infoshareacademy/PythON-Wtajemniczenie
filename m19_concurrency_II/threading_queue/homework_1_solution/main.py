from threading import Thread

from book_book.actions import rent_a_book
from book_book.books_directory import books_requests_queue, books_manager
from book_book.printer import print_requests_queue, printer_manager


def run_example() -> None:
    clients = [
        "Jan",
        "Karolina",
        "Krzysztof",
        "Barbara",
        "Paweł",
        "Paulina",
        "Filip",
        "Joanna",
        "Maciej",
        "Elwira",
    ]
    printer_manager_thread = Thread(target=printer_manager, daemon=True)
    printer_manager_thread.start()
    books_manager_thread = Thread(target=books_manager, daemon=True)
    books_manager_thread.start()

    clients_threads = [
        Thread(target=rent_a_book, args=("Aleksandra", "Nauka - o kosmosie", client))
        for client in clients
    ]
    for client_thread in clients_threads:
        client_thread.start()

    for client_thread in clients_threads:
        client_thread.join()

    books_requests_queue.join()
    print_requests_queue.join()


if __name__ == "__main__":
    run_example()
