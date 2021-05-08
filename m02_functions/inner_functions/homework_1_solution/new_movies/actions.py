from new_movies import permissions
from new_movies.exceptions import (
    NoCreditsForMovieRent,
    ActionNotAllowed,
    MovieNotFound,
    ViewsLimitReached,
)
from new_movies.rented_movie import RentedMovie


def rent_movie(user, movie):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1


def watch_movie(user, movie):
    def get_rented_movie(user_with_movies, searching_movie):
        for rented_movie in user_with_movies.rented_movies:
            if rented_movie.movie == searching_movie:
                return rented_movie

    user_rented_movie = get_rented_movie(user, movie)
    if not user_rented_movie:
        raise MovieNotFound()

    if user_rented_movie.views_left < 1:
        raise ViewsLimitReached()

    user_rented_movie.views_left -= 1
    _start_streaming(user, movie)


def _start_streaming(user, movie):
    print(f"User: {user} is watching {movie}")

#
# def watch_movie(user, movie):
#     rented_movie = _get_rented_movie(user, movie)
#     if not rented_movie:
#         raise MovieNotFound()
#
#     if rented_movie.views_left < 1:
#         raise ViewsLimitReached()
#
#     rented_movie.views_left -= 1
#     _start_streaming(user, movie)
#
#
# def _get_rented_movie(user, movie):
#     for rented_movie in user.rented_movies:
#         if rented_movie.movie == movie:
#             return rented_movie


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()
