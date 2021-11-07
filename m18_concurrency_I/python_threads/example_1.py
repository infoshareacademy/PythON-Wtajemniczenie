import time

import threading


def do_some_work() -> None:
    time.sleep(2)


def say_something() -> None:
    print(f"Hej! To ja wątek! Mój identyfikator to: {threading.get_ident()}")
    do_some_work()


def run_example() -> None:
    for _ in range(10):
        threading.Thread(target=say_something).start()


if __name__ == "__main__":
    run_example()
