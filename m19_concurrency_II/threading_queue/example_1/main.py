from threading import Thread

import random

import time

from ebike.bikes import rent_a_bike, bikes_manager, bikes_requests_queue
from ebike.printer import print_text, printer_manager, print_requests_queue


def worker(name: str) -> None:
    print_text(f"Hi! I am handling client {name}. First will do some work...")
    time.sleep(random.randint(1, 2))
    print_text(f"Now will try to rent a bike for {name}")
    rent_a_bike(name)


def run_example() -> None:
    clients = [
        "John",
        "Liam",
        "Olivia",
        "Emma",
        "Ava",
        "Alexander",
        "Henry",
        "Amelia",
        "Isabella",
        "Evelyn",
    ]

    printer_manager_thread = Thread(target=printer_manager, daemon=True)
    printer_manager_thread.start()
    bikes_manager_thread = Thread(target=bikes_manager, daemon=True)
    bikes_manager_thread.start()

    threads = [Thread(target=worker, args=(client,)) for client in clients]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    bikes_requests_queue.join()
    print_requests_queue.join()


if __name__ == "__main__":
    run_example()
