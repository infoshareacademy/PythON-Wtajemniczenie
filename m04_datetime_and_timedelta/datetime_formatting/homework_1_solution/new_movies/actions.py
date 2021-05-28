from datetime import date, time, datetime

from new_movies import permissions, movies_directory, cinema_schedule, users_directory
from new_movies.cinema_schedule import Weekday
from new_movies.configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
from new_movies.datetime_preferences import DatetimePreference
from new_movies.exceptions import (
    NoCreditsForMovieRent,
    ActionNotAllowed,
    MovieNotFound,
    ViewsLimitReached,
    UserNotFound,
)
from new_movies.movie import Movie
from new_movies.rented_movie import RentedMovie


def login():
    while True:
        user_login = input("Type in your login: ")
        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            print("There is no user with such login - try again")


def select_datetime_preferences(user):
    print("Available formats:")
    for option_index, datetime_preference in enumerate(DatetimePreference):
        print(f"{option_index}) {datetime_preference}")

    selected_option = int(input("Select an option: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(selected_option)


def rent_movie(user, movie):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1


def watch_movie(user, movie):
    rented_movie = _get_rented_movie(user, movie)
    if not rented_movie:
        raise MovieNotFound()

    if _unlimited_watching_promo():
        _watch_movie_during_unlimited_promo(user, rented_movie)
    else:
        _watch_movie_during_standard_period(user, rented_movie)


def _get_rented_movie(user, movie):
    for rented_movie in user.rented_movies:
        if rented_movie.movie == movie:
            return rented_movie


def _unlimited_watching_promo():
    return UNLIMITED_WATCHING_START_DATE <= date.today() <= UNLIMITED_WATCHING_END_DATE


def _watch_movie_during_unlimited_promo(user, rented_movie):
    _start_streaming(user, rented_movie.movie)


def _watch_movie_during_standard_period(user, rented_movie):
    if rented_movie.views_left < 1:
        raise ViewsLimitReached()

    rented_movie.views_left -= 1
    _start_streaming(user, rented_movie.movie)


def _start_streaming(user, movie):
    datetime_format = user.datetime_preferences.value
    print(f"User: {user} is watching {movie.info_with_date_format(datetime_format)}")


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()


def add_movie():
    print("Adding new movie")
    print("Provide movie's data")
    name = input("Title: ")
    category = input("Category: ")
    release_date_input = input("Release date (in YYYY-MM-DD format): ")
    release_date = date.fromisoformat(release_date_input)
    new_movie = Movie(name, category, release_date)
    movies_directory.add_movie(new_movie)


def cinema_movies_schedule(user):
    datetime_format = user.datetime_preferences.value
    cinema_datetime_input = input("When would you like to visit the cinema? (YYYY-MM-DD hh:mm): ")
    cinema_datetime = datetime.fromisoformat(cinema_datetime_input)
    cinema_time = cinema_datetime.time()
    weekday_number = cinema_datetime.isoweekday()
    weekday = Weekday(weekday_number)
    movies_at_weekday = cinema_schedule.get_movies_showtime_by_weekday(weekday)
    print("This day you can watch:")
    for movie_showtime in movies_at_weekday:
        if cinema_time <= movie_showtime.showtime:
            showtime_formatted = movie_showtime.showtime.strftime(datetime_format.time_format)
            movie_info_formatted = movie_showtime.movie.info_with_date_format(datetime_format)
            print(f"{showtime_formatted} {movie_info_formatted}")
