from collections.abc import Callable
from typing import TypeVar, Any

F = TypeVar("F", bound=Callable[..., Any])


def log_info(message: str) -> None:
    print(f"[INFO]: {message}")
