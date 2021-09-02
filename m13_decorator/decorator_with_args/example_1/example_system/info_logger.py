from collections.abc import Callable
from typing import Any, TypeVar, cast
from example_system.logger import Logger

F = TypeVar("F", bound=Callable[..., Any])


def info_logger(logger: Logger) -> Callable[[F], F]:
    def logger_decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.log(f"[INFO]: Running function {func.__name__}")
            return func(*args, **kwargs)

        return cast(F, wrapper)

    return logger_decorator
