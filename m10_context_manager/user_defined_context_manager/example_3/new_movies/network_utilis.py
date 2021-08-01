from types import TracebackType
from typing import Optional, Type

from new_movies import logger


class RemoteServiceError(Exception):
    pass


class ErrorHandling:
    def __enter__(self) -> None:
        return None

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if exc_type:
            logger.log_error(str(exc_type))
        if exc_type is BrokenPipeError:
            raise RemoteServiceError("Connection interrupted")
        if exc_type is ConnectionError:
            raise RemoteServiceError("Unable to connect")
        if exc_type is TimeoutError:
            raise RemoteServiceError("Timeout exceeded")
