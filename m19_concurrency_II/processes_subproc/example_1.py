import os

import time

import subprocess


def run_example() -> None:
    result = subprocess.run(["ls", "-l", "."], capture_output=True)
    print(result.stdout)

    start_time = time.perf_counter()
    for _ in range(1_000):
        result = subprocess.run(["ls", "."], capture_output=True)

    end_time = time.perf_counter()
    print(f"Time: {end_time - start_time:.2f}")

    start_time = time.perf_counter()
    for _ in range(1_000):
        python_func_results = os.listdir()

    end_time = time.perf_counter()
    print(f"Time: {end_time - start_time:.2f}")


if __name__ == "__main__":
    run_example()
