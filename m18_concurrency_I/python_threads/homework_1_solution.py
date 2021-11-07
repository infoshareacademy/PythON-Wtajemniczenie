import random

import threading


def calculate_average() -> None:
    numbers = [random.randint(0, 100) for _ in range(10)]
    average = sum(numbers) / len(numbers)
    print(f"Wynik mojego działania to: {average}")


def run_example() -> None:
    for _ in range(10):
        threading.Thread(target=calculate_average).start()


if __name__ == "__main__":
    run_example()
