from dataclasses import dataclass
from datetime import time
from enum import Enum, auto

from new_movies import movies_directory
from new_movies.movie import Movie


class Weekday(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()


@dataclass
class MovieShowtime:
    movie: Movie
    showtime: time


weekly_schedule = {
    Weekday.MONDAY: [
        MovieShowtime(movies_directory.available_movies[0], time(15, 15)),
        MovieShowtime(movies_directory.available_movies[1], time(17, 15)),
    ],
    Weekday.TUESDAY: [
        MovieShowtime(movies_directory.available_movies[3], time(17, 15)),
        MovieShowtime(movies_directory.available_movies[2], time(15, 15)),
    ],
    Weekday.WEDNESDAY: [
        MovieShowtime(movies_directory.available_movies[4], time(15, 15)),
        MovieShowtime(movies_directory.available_movies[5], time(17, 15)),
    ],
    Weekday.THURSDAY: [
        MovieShowtime(movies_directory.available_movies[7], time(17, 15)),
        MovieShowtime(movies_directory.available_movies[6], time(15, 15)),
    ],
    Weekday.FRIDAY: [
        MovieShowtime(movies_directory.available_movies[10], time(19, 20)),
        MovieShowtime(movies_directory.available_movies[8], time(15, 15)),
        MovieShowtime(movies_directory.available_movies[9], time(17, 15)),
    ],
    Weekday.SATURDAY: [MovieShowtime(movies_directory.available_movies[11], time(18, 00))],
    Weekday.SUNDAY: [
        MovieShowtime(movies_directory.available_movies[12], time(13, 25)),
        MovieShowtime(movies_directory.available_movies[13], time(14, 50)),
    ],
}


def get_movies_showtime_by_weekday(weekday):
    return weekly_schedule[weekday]
