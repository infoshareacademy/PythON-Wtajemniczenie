from typing import TypeVar

from threading import Thread

import random
from multiprocessing import Process

import time

T = TypeVar("T")


def calculate_factorial_for_numbers(numbers: list[int]) -> None:
    results = [factorial(number) for number in numbers]


def factorial(number: int) -> int:
    result = 1
    for current_number in range(1, number + 1):
        result *= current_number
    return result


def split_data_into_parts(number_of_portions: int, data: list[T]) -> list[list[T]]:
    portion_size = int(len(data) / number_of_portions)
    return [
        data[portion_number * portion_size : (portion_number + 1) * portion_size]
        for portion_number in range(number_of_portions)
    ]


def run_example() -> None:
    random_numbers = [random.randint(10_000, 50_000) for _ in range(200)]
    start_time = time.perf_counter()
    worker_processes: list[Process] = []

    data_for_processes = split_data_into_parts(number_of_portions=2, data=random_numbers)
    for numbers_data in data_for_processes:
        worker_process = Process(target=calculate_factorial_for_numbers, args=(numbers_data,))
        worker_processes.append(worker_process)
        worker_process.start()

    for process in worker_processes:
        process.join()

    end_time = time.perf_counter()
    print(f"Time: {end_time - start_time:.2f}")

    start_time = time.perf_counter()
    worker_threads: list[Thread] = []
    data_for_threads = split_data_into_parts(number_of_portions=100, data=random_numbers)
    for numbers_data in data_for_threads:
        worker_thread = Thread(target=calculate_factorial_for_numbers, args=(numbers_data,))
        worker_threads.append(worker_thread)
        worker_thread.start()

    for thread in worker_threads:
        thread.join()

    end_time = time.perf_counter()
    print(f"Time: {end_time - start_time:.2f}")


if __name__ == "__main__":
    run_example()
