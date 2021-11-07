import threading

from book_book.actions import rent_a_book


def run_example() -> None:
    threading.Thread(target=rent_a_book, args=("Aleksandra", "Nauka - o kosmosie")).start()
    threading.Thread(target=rent_a_book, args=("Aleksandra", "Nauka - o kosmosie")).start()
    threading.Thread(target=rent_a_book, args=("Aleksandra", "Nauka - o kosmosie")).start()


if __name__ == "__main__":
    run_example()
