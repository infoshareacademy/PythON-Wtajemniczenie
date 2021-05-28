from dataclasses import dataclass
from datetime import time, datetime, date, timedelta
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
        showdatetime = datetime.combine(show_date, movie_showtime.showtime)
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


sorted_schedule = sort_weekly_schedule(weekly_schedule)


def get_movies_showtime_by_weekday(weekday):
    sorted_schedule = sort_weekly_schedule(weekly_schedule)
    return sorted_schedule[weekday]


def generate_february_week_schedule(schedule):
    february_21 = date(year=2021, month=2, day=21)
    return schedule_for_week(february_21, schedule)


def schedule_for_week(date_from_week, schedule):
    weekday_number = date_from_week.isoweekday()
    offset_to_monday = weekday_number - Weekday.MONDAY.value
    monday_date = date_from_week - timedelta(days=offset_to_monday)
    result = {}
    for weekday in Weekday:
        offset_to_weekday = weekday.value - Weekday.MONDAY.value
        particular_date = monday_date + timedelta(days=offset_to_weekday)
        result[weekday] = [
            MovieShowDatetime.from_movie_showtime_and_date(movie_showtime, particular_date)
            for movie_showtime in schedule.get(weekday, [])
        ]
    return result


