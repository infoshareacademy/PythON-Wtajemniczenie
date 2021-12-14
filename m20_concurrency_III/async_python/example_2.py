import asyncio
import time

import aiohttp


class StarWarsData:
    people: list[str] = []


async def load_person_data(person_id: int) -> None:
    swapi_people_url = "https://swapi.dev/api/people/"
    person_url = f"{swapi_people_url}{person_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(person_url,) as response:
            try:
                response.raise_for_status()
            except Exception as error:
                print(str(error))
            if response.ok:
                response_data = await response.json()
                person_data = response_data["name"]
            else:
                person_data = f"Unable to load person with id {person_id}"
    StarWarsData.people.append(person_data)


def run_example() -> None:
    start_time = time.perf_counter()
    loop = asyncio.get_event_loop()

    tasks = [loop.create_task(load_person_data(person_id)) for person_id in range(1, 20)]
    loop.run_until_complete(asyncio.wait(tasks))

    end_time = time.perf_counter()
    print(StarWarsData.people)
    print(f"Time: {end_time - start_time:.2f}")


if __name__ == "__main__":
    run_example()
