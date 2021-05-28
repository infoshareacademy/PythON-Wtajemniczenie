from dataclasses import dataclass
from datetime import time, datetime, date
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


@dataclass
class MovieShowDatetime:
    movie: Movie
    showdatetime: datetime

    @staticmethod
    def from_movie_showtime_and_date(movie_showtime, show_date):
        showtime = movie_showtime.showtime
        showdatetime = datetime(
            year=show_date.year,
            month=show_date.month,
            day=show_date.day,
            hour=showtime.hour,
            minute=showtime.minute,
            second=showtime.second,
            microsecond=showtime.microsecond,
        )
        return MovieShowDatetime(movie=movie_showtime.movie, showdatetime=showdatetime)


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


def sort_weekly_schedule(schedule):
    return {
        weekday: sorted(showtime, key=lambda movie_showtime: movie_showtime.showtime)
        for weekday, showtime in schedule.items()
    }


def get_movies_showtime_by_weekday(weekday):
    sorted_schedule = sort_weekly_schedule(weekly_schedule)
    return sorted_schedule[weekday]


def generate_february_week_schedule(schedule):
    february_21 = date(year=2021, month=2, day=21)

    result = {}
    for weekday, showtimes in schedule.items():
        particular_weekday_in_february = february_21.replace(day=february_21.day + weekday.value)
        result[weekday] = [
            MovieShowDatetime.from_movie_showtime_and_date(
                movie_showtime, particular_weekday_in_february
            )
            for movie_showtime in showtimes
        ]
    return result
