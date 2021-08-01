from contextlib import contextmanager
from typing import Iterator

from new_movies import logger


class RemoteServiceError(Exception):
    pass


@contextmanager
def error_handling() -> Iterator[None]:
    try:
        yield
    except BrokenPipeError:
        logger.log_error("BrokenPipeError")
        raise RemoteServiceError("Connection interrupted")
    except ConnectionError:
        logger.log_error("ConnectionError")
        raise RemoteServiceError("Unable to connect")
    except TimeoutError:
        logger.log_error("TimeoutError")
        raise RemoteServiceError("Timeout exceeded")
    except Exception as error:
        logger.log_error(f"Other error: {error}")
