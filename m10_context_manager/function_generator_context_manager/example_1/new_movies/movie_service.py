import random
from contextlib import contextmanager
from typing import Iterator

from new_movies import logger


class MovieService:
    def connect(self) -> None:
        print("Connecting...")

    def get_movie(self) -> str:
        movie_number = random.randint(1, 100)
        if movie_number % 10 == 0:
            raise ValueError("Ops!")
        return f"Movie({movie_number})"

    def close(self) -> None:
        print("Closing...")


@contextmanager
def movie_service_connection() -> Iterator[MovieService]:
    movie_service = MovieService()
    movie_service.connect()
    try:
        yield movie_service
    except Exception as error:
        logger.log_error(f"Something went wrong: {error}")
        raise error
    finally:
        movie_service.close()
