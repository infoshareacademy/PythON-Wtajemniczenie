from dataclasses import dataclass
from datetime import time, datetime, timedelta
from enum import Enum, auto
from zoneinfo import ZoneInfo

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
        showdatetime = datetime.combine(show_date, movie_showtime.showtime)
        return MovieShowDatetime(movie=movie_showtime.movie, showdatetime=showdatetime)


_pl_timezone = ZoneInfo("Europe/Warsaw")

_weekly_schedule_template = {
    Weekday.MONDAY: [
        MovieShowtime(movies_directory.available_movies[0], time(15, 15, tzinfo=_pl_timezone)),
        MovieShowtime(movies_directory.available_movies[1], time(17, 15, tzinfo=_pl_timezone)),
    ],
    Weekday.TUESDAY: [
        MovieShowtime(movies_directory.available_movies[3], time(17, 15, tzinfo=_pl_timezone)),
        MovieShowtime(movies_directory.available_movies[2], time(15, 15, tzinfo=_pl_timezone)),
    ],
    Weekday.WEDNESDAY: [
        MovieShowtime(movies_directory.available_movies[4], time(15, 15, tzinfo=_pl_timezone)),
        MovieShowtime(movies_directory.available_movies[5], time(17, 15, tzinfo=_pl_timezone)),
    ],
    Weekday.THURSDAY: [
        MovieShowtime(movies_directory.available_movies[7], time(17, 15, tzinfo=_pl_timezone)),
        MovieShowtime(movies_directory.available_movies[6], time(15, 15, tzinfo=_pl_timezone)),
    ],
    Weekday.FRIDAY: [
        MovieShowtime(movies_directory.available_movies[10], time(19, 20, tzinfo=_pl_timezone)),
        MovieShowtime(movies_directory.available_movies[8], time(15, 15, tzinfo=_pl_timezone)),
        MovieShowtime(movies_directory.available_movies[9], time(17, 15, tzinfo=_pl_timezone)),
    ],
    Weekday.SATURDAY: [
        MovieShowtime(movies_directory.available_movies[11], time(18, 0, tzinfo=_pl_timezone))
    ],
    Weekday.SUNDAY: [
        MovieShowtime(movies_directory.available_movies[12], time(13, 25, tzinfo=_pl_timezone)),
        MovieShowtime(movies_directory.available_movies[13], time(14, 50, tzinfo=_pl_timezone)),
    ],
}


weekly_schedule_template = {
    weekday: sorted(showtime, key=lambda movie_showtime: movie_showtime.showtime)
    for weekday, showtime in _weekly_schedule_template.items()
}


def schedule_for_week(date_from_week, schedule_template):
    weekday_number = date_from_week.isoweekday()
    offset_to_monday = weekday_number - Weekday.MONDAY.value
    monday_date = date_from_week - timedelta(days=offset_to_monday)
    result = {}
    for weekday in Weekday:
        offset_to_weekday = weekday.value - Weekday.MONDAY.value
        particular_date = monday_date + timedelta(days=offset_to_weekday)
        result[weekday] = [
            MovieShowDatetime.from_movie_showtime_and_date(movie_showtime, particular_date)
            for movie_showtime in schedule_template.get(weekday, [])
        ]
    return result
