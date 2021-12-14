import time
from multiprocessing import Process
from threading import Thread

import requests


def calculate() -> None:
    for _ in range(50):
        previous_value = 0
        pre_previous_value = 1
        current_value = None
        for _ in range(50_000):
            current_value = previous_value + pre_previous_value
            pre_previous_value = previous_value
            previous_value = current_value


def load_person_data(person_id: int) -> None:
    swapi_people_url = "https://swapi.dev/api/people/"
    person_url = f"{swapi_people_url}{person_id}"
    requests.get(url=person_url)


# def do_work() -> None:
#     calculate_thread = Thread(target=calculate)
#     calculate_thread.start()
#
#     data_loader_threads: list[Thread] = []
#     for person_id in range(1, 10):
#         data_loader_thread = Thread(target=load_person_data, args=(person_id,))
#         data_loader_threads.append(data_loader_thread)
#         data_loader_thread.start()
#
#     calculate_thread.join()
#     for thread in data_loader_threads:
#         thread.join()


def do_work() -> None:
    calculate()
    for person_id in range(1, 10):
        load_person_data(person_id)


def run_example() -> None:
    # start_time = time.perf_counter()
    # workers: list[Process] = []
    # for _ in range(2):
    #     process = Process(target=do_work)
    #     workers.append(process)
    #     process.start()
    #
    # for process in workers:
    #     process.join()
    #
    # end_time = time.perf_counter()
    # print(f"Time: {end_time - start_time:.2f}")

    start_time = time.perf_counter()
    for _ in range(2):
        do_work()

    end_time = time.perf_counter()
    print(f"Time: {end_time - start_time:.2f}")


if __name__ == "__main__":
    run_example()
