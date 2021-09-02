from new_movies.movie import Movie
from new_movies.random_data_utility import random_generator


def watch_movie() -> None:
    movies = random_generator.generate_random_movies(movies_number=1)
    _start_streaming(movies[0])


def _start_streaming(movie: Movie) -> None:
    print(f"You are watching {movie}")
