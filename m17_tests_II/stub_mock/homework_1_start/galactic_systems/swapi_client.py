import requests
from requests import RequestException, Timeout

from galactic_systems.logger import log_error
from galactic_systems.vehicle import Vehicle


class IntegrationError(Exception):
    pass


class SWAPIClient:

    PEOPLE_URL = "https://swapi.dev/api/vehicles/"

    def load_vehicles(self) -> list[Vehicle]:
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
            Vehicle(
                name=vehicle_data["name"],
                model=vehicle_data["model"],
                max_speed=int(vehicle_data["max_atmosphering_speed"]),
            )
            for vehicle_data in results.json()["results"]
        ]
