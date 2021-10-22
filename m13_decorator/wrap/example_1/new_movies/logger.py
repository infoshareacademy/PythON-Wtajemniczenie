import functools
from collections.abc import Callable
from typing import TypeVar, Any, cast

F = TypeVar("F", bound=Callable[..., Any])


def log_info(message: str) -> None:
    print(f"[INFO]: {message}")


def logger(func: F) -> F:
    # @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        log_info(f"Running function {func.__name__}")
        return func(*args, **kwargs)

    return cast(F, wrapper)
