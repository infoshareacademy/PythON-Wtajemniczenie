from collections.abc import Callable
from typing import TypeVar, Any, cast

F = TypeVar("F", bound=Callable[..., Any])


def log_info(message: str) -> None:
    print(f"[INFO]: {message}")


def logger(func: F) -> F:
    def wrapper() -> Any:
        log_info(f"Running function {func.__name__}")
        return func()

    return cast(F, wrapper)
