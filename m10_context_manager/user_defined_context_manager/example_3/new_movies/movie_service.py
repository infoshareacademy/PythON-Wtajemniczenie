import random


class MovieService:

    def get_movie(self) -> str:
        movie_number = random.randint(1, 100)
        if movie_number % 9 == 0:
            raise ConnectionError()
        if movie_number % 10 == 0:
            raise TimeoutError()
        if movie_number % 11 == 0:
            raise BrokenPipeError()
        return f"Movie({movie_number})"
