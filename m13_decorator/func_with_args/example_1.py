from collections.abc import Callable
from typing import Any, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def talkative(func: F) -> F:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Will run a func!")
        result = func(*args, **kwargs)
        print(f"Hey! Result is: {result}")
        print("Bye bye!")
        return result

    return cast(F, wrapper)


@talkative
def multiply_by_two(number: int) -> int:
    return number * 2


# multiply_by_two = talkative(multiply_by_two)


def run_example() -> None:
    results = multiply_by_two(5)
    print(results)


if __name__ == "__main__":
    run_example()
