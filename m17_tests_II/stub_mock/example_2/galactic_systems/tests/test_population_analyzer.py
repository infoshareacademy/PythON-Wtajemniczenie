from unittest.mock import MagicMock

from galactic_systems.person import Person
from galactic_systems.population_analyzer import PopulationAnalyzer
from galactic_systems.swapi_client import SWAPIClient


def test_calculate_average_height_real():
    population_analyzer = PopulationAnalyzer(swapi_client=SWAPIClient())

    assert population_analyzer.calculate_average_height() == 159


# def test_calculate_average_height_mock():
#     people = [
#         Person(name="Test-1", height=100, mass=100),
#         Person(name="Test-2", height=200, mass=150),
#         Person(name="Test-3", height=300, mass=200),
#     ]
#     swapi_client_mock = MagicMock()
#     swapi_client_mock.load_people = MagicMock(return_value=people)
#     population_analyzer = PopulationAnalyzer(swapi_client=swapi_client_mock)
#
#     assert population_analyzer.calculate_average_height() == 200


# def test_calculate_average_height_real_perf():
#     population_analyzer = PopulationAnalyzer(swapi_client=SWAPIClient())
#
#     for _ in range(10):
#         assert population_analyzer.calculate_average_height() == 159

#
# def test_calculate_average_height_mock_perf():
#     people = [
#         Person(name="Test-1", height=100, mass=100),
#         Person(name="Test-2", height=200, mass=150),
#         Person(name="Test-3", height=300, mass=200),
#     ]
#     swapi_client_mock = MagicMock()
#     swapi_client_mock.load_people = MagicMock(return_value=people)
#     population_analyzer = PopulationAnalyzer(swapi_client=swapi_client_mock)
#
#     for _ in range(10):
#         assert population_analyzer.calculate_average_height() == 200
