from unittest.mock import patch

from galactic_systems.person import Person
from galactic_systems.population_analyzer import PopulationAnalyzer
from galactic_systems.swapi_client import SWAPIClient


def test_calculate_average_height():
    people = [
        Person(name="Test-1", height=100, mass=100),
        Person(name="Test-2", height=200, mass=150),
        Person(name="Test-3", height=300, mass=200),
    ]

    with patch.object(SWAPIClient, "load_people") as load_people_mock:
        load_people_mock.return_value = people
        population_analyzer = PopulationAnalyzer()

        assert population_analyzer.calculate_average_height() == 200


@patch.object(SWAPIClient, "load_people")
def test_calculate_average_height_mock_decorator(load_people_mock):
    people = [
        Person(name="Test-1", height=100, mass=100),
        Person(name="Test-2", height=200, mass=150),
        Person(name="Test-3", height=300, mass=200),
    ]
    load_people_mock.return_value = people
    population_analyzer = PopulationAnalyzer()

    assert population_analyzer.calculate_average_height() == 200


@patch("galactic_systems.swapi_client.SWAPIClient.load_people")
def test_calculate_average_height_patch(load_people_mock):
    people = [
        Person(name="Test-1", height=100, mass=100),
        Person(name="Test-2", height=200, mass=150),
        Person(name="Test-3", height=300, mass=200),
    ]
    load_people_mock.return_value = people
    population_analyzer = PopulationAnalyzer()

    assert population_analyzer.calculate_average_height() == 200
