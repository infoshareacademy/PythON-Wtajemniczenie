from new_movies.movie import Movie
from new_movies.movie_service import MovieService
from new_movies.network_utilis import ErrorHandling, RemoteServiceError


def load_available_movies() -> list[Movie]:
    movies: list[Movie] = []
    try:
        with ErrorHandling():
            movie_service = MovieService()
            for _ in range(4):
                movie_name = movie_service.get_movie()
                movies.append(Movie(movie_name))
    except RemoteServiceError as error:
        print(error)
    return movies
