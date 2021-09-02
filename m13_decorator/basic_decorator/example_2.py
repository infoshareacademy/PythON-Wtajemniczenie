import random
from collections.abc import Callable
from typing import Any


def goodbye(func: Callable[[], Any]) -> Callable[[], Any]:
    def func_with_goodbye() -> Any:
        result = func()
        print("Goodbye!")
        print("---")
        return result

    return func_with_goodbye


@goodbye
def say_hello() -> None:
    print("Hello")


@goodbye
def random_number() -> int:
    print("Calculate some random value...")
    return random.randint(1, 100)


def run_example() -> None:
    say_hello()
    random_value = random_number()
    print(random_value)

    # reveal_type(random_number)


if __name__ == "__main__":
    run_example()
