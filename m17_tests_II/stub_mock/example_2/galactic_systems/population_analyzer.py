from galactic_systems.swapi_client import SWAPIClient


class PopulationAnalyzer:
    def __init__(self, swapi_client: SWAPIClient) -> None:
        self.swapi_client = swapi_client

    def calculate_average_height(self) -> int:
        people = self.swapi_client.load_people()
        height_sum = sum(person.height for person in people)
        number_of_people = len(people)
        return int(height_sum / number_of_people)
