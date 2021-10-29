from unittest.mock import patch

from galactic_systems.swapi_client import SWAPIClient
from galactic_systems.vehicle import Vehicle
from galactic_systems.vehicles_analyzer import VehiclesAnalyzer


@patch.object(SWAPIClient, "load_vehicles")
def test_calculate_average_speed(load_vehicles_mock):
    vehicles = [
        Vehicle(name="Test-1", model="Test", max_speed=10),
        Vehicle(name="Test-2", model="Test", max_speed=30),
        Vehicle(name="Test-3", model="Test", max_speed=50),
    ]
    load_vehicles_mock.return_value = vehicles
    population_analyzer = VehiclesAnalyzer()

    assert population_analyzer.calculate_average_speed() == 30


@patch.object(SWAPIClient, "load_vehicles")
def test_calculate_average_speed_returns_0_when_no_vehicles(load_vehicles_mock):
    vehicles = []
    load_vehicles_mock.return_value = vehicles
    population_analyzer = VehiclesAnalyzer()

    assert population_analyzer.calculate_average_speed() == 0
