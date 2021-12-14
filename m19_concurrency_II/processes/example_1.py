from multiprocessing import Process
from typing import Optional

import time


def calculate() -> None:
    for _ in range(500):
        previous_value = 0
        pre_previous_value = 1
        current_value: Optional[int] = None
        for _ in range(50_000):
            current_value = previous_value + pre_previous_value
            pre_previous_value = previous_value
            previous_value = current_value


def run_example() -> None:
    start_time = time.perf_counter()
    worker_processes: list[Process] = []
    for _ in range(2):
        worker_process = Process(target=calculate)
        worker_processes.append(worker_process)
        worker_process.start()

    for process in worker_processes:
        process.join()

    end_time = time.perf_counter()
    print(f"Time: {end_time - start_time:.2f}")


if __name__ == "__main__":
    run_example()
