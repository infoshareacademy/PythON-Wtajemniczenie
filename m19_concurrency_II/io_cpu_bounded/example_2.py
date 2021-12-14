from threading import Thread
import time

import requests


class StarWarsData:
    people: list[str] = []


def load_person_data(person_id: int) -> None:
    swapi_people_url = "https://swapi.dev/api/people/"
    person_url = f"{swapi_people_url}{person_id}"
    response = requests.get(url=person_url)
    if response.ok:
        person_data = response.json()["name"]
    else:
        person_data = f"Unable to load person with id {person_id}"
    StarWarsData.people.append(person_data)


def run_example() -> None:
    start_time = time.perf_counter()
    worker_threads: list[Thread] = []
    for person_id in range(1, 20):
        worker_thread = Thread(target=load_person_data, args=(person_id,))
        worker_threads.append(worker_thread)
        worker_thread.start()

    for thread in worker_threads:
        thread.join()

    end_time = time.perf_counter()
    print(StarWarsData.people)
    print(f"Time: {end_time - start_time:.2f}")


if __name__ == "__main__":
    run_example()
