import asyncio
import time

import aiohttp


class StarWarsData:
    planets: list[str] = []


async def load_planet_data(planet_id: int) -> None:
    swapi_planets_url = "https://swapi.dev/api/planets/"
    planet_url = f"{swapi_planets_url}{planet_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(planet_url,) as response:
            try:
                response.raise_for_status()
            except Exception as error:
                print(str(error))
            if response.ok:
                response_data = await response.json()
                planet_data = response_data["name"]
            else:
                planet_data = f"Unable to load planet with id {planet_id}"
    StarWarsData.planets.append(planet_data)


def run_example() -> None:
    start_time = time.perf_counter()
    loop = asyncio.get_event_loop()

    tasks = [loop.create_task(load_planet_data(planet_id)) for planet_id in range(1, 20)]
    loop.run_until_complete(asyncio.wait(tasks))

    end_time = time.perf_counter()
    print(StarWarsData.planets)
    print(f"Time: {end_time - start_time:.2f}")


if __name__ == "__main__":
    run_example()
