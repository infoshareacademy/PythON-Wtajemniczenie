from typing import Optional

from new_movies import permissions
from new_movies.exceptions import (
    NoCreditsForMovieRent,
    ActionNotAllowed,
    MovieNotFound,
    ViewsLimitReached,
)
from new_movies.logger import logger
from new_movies.movie import Movie
from new_movies.rented_movie import RentedMovie
from new_movies.user import User


def rent_movie(user: User, movie: Movie) -> None:
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1


@logger
def watch_movie(user: User, movie: Movie) -> None:
    rented_movie = _get_rented_movie(user, movie)
    if not rented_movie:
        raise MovieNotFound()

    if rented_movie.views_left < 1:
        raise ViewsLimitReached()

    rented_movie.views_left -= 1
    _start_streaming(user, movie)


def _get_rented_movie(user: User, movie: Movie) -> Optional[RentedMovie]:
    for rented_movie in user.rented_movies:
        if rented_movie.movie == movie:
            return rented_movie
    return None


def _start_streaming(user: User, movie: Movie) -> None:
    print(f"User: {user} is watching {movie}")


def refresh_credits(acting_user: User, user_to_be_refreshed: User) -> None:
    if permissions.is_admin(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()
