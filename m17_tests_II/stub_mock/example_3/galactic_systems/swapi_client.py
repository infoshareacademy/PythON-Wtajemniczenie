import requests
from requests import RequestException, Timeout

from galactic_systems.logger import log_error
from galactic_systems.person import Person


class IntegrationError(Exception):
    pass


class SWAPIClient:

    PEOPLE_URL = "https://swapi.dev/api/people/"

    def load_people(self) -> list[Person]:
        try:
            results = requests.get(self.PEOPLE_URL)
        except Timeout:
            log_error("Timeout when connecting with SWAPI")
            raise IntegrationError("Timeout")
        except RequestException as error:
            log_error(f"General error when working with SWAPI: {error}")
            raise IntegrationError("General error")

        if not results.ok:
            log_error(f"Error in response from SWAPI, code: {results.status_code}")
            raise IntegrationError(f"Response status: {results.status_code}")

        return [
            Person(
                name=person_data["name"],
                height=int(person_data["height"]),
                mass=int(person_data["mass"]),
            )
            for person_data in results.json()["results"]
        ]
