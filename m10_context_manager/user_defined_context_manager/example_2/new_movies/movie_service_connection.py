from types import TracebackType
from typing import Optional, Type

from new_movies import logger
from new_movies.movie_service import MovieService


class MovieServiceConnection:
    def __init__(self, movie_service: MovieService) -> None:
        self.movie_service = movie_service

    def __enter__(self) -> MovieService:
        self.movie_service.connect()
        return self.movie_service

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> None:
        if exc_type:
            logger.log_error(f"Something went wrong: {exc_val}")
        self.movie_service.close()
