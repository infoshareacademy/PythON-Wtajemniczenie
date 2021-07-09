import csv
import os
import random
from dataclasses import dataclass
from datetime import date

from new_movies.game import Game
from new_movies.movie import Movie, AgeRate

MIN_VOTERS = 3
MAX_VOTERS = 10

MIN_RATE = 1
MAX_RATE = 5

RELEASE_YEAR_FROM = 1980
RELEASE_YEAR_TO = 2020


@dataclass
class MovieData:
    name: str
    category: str


def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def generate_random_date(year_from: int, year_to: int) -> date:
    year = random.randint(year_from, year_to)
    month = random.randint(1, 12)

    months_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_30_days = [4, 6, 9, 11]
    if month in months_31_days:
        max_day = 31
    elif month in months_30_days:
        max_day = 30
    elif is_leap_year(year):
        max_day = 29
    else:
        max_day = 28

    day = random.randint(1, max_day)

    return date(year=year, month=month, day=day)


def generate_random_movies(movies_number: int) -> list[Movie]:
    generator_directory = os.path.dirname(os.path.abspath(__file__))
    movies_file_path = os.path.join(generator_directory, "random_movies_data.csv")

    with open(movies_file_path) as movies_data_file:
        movies_reader = csv.DictReader(movies_data_file)
        movies_data = [
            MovieData(name=movie_row["name"], category=movie_row["category"])
            for movie_row in movies_reader
        ]

    movies = []
    for _ in range(movies_number):
        movie_index = random.randrange(0, len(movies_data))
        movie_data = movies_data.pop(movie_index)
        release_date = generate_random_date(RELEASE_YEAR_FROM, RELEASE_YEAR_TO)
        movie = Movie(
            name=movie_data.name,
            category=movie_data.category,
            release_date=release_date,
            age_rate=AgeRate.ORANGE,
        )
        movies.append(movie)

    return movies


def generate_random_games() -> list[Game]:
    generator_directory = os.path.dirname(os.path.abspath(__file__))
    games_data_file_path = os.path.join(generator_directory, "random_movies_data.csv")

    with open(games_data_file_path) as games_data_file:
        games_reader = csv.DictReader(games_data_file)
        return [Game(name=game_row["name"]) for game_row in games_reader]
