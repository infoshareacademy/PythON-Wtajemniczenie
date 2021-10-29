from galactic_systems.swapi_client import SWAPIClient


class VehiclesAnalyzer:
    def __init__(self) -> None:
        self.swapi_client = SWAPIClient()

    def calculate_average_speed(self) -> int:
        vehicles = self.swapi_client.load_vehicles()
        speed_sum = sum(vehicle.max_speed for vehicle in vehicles)
        number_of_vehicles = len(vehicles)
        if not number_of_vehicles:
            return 0
        return int(speed_sum / number_of_vehicles)
