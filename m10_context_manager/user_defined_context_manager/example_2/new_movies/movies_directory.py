from new_movies.movie import Movie
from new_movies.movie_service import MovieServiceA, MovieServiceB
from new_movies.movie_service_connection import MovieServiceConnection


def load_available_movies() -> list[Movie]:
    with MovieServiceConnection(MovieServiceB()) as movies_service:
        movies: list[Movie] = []
        for _ in range(4):
            movie_name = movies_service.get_movie()
            movies.append(Movie(movie_name))
        return movies
