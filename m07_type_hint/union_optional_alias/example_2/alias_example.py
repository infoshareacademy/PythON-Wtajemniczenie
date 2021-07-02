from datetime import datetime
from typing import Union

Datetime = datetime
NumberOrStr = Union[int, float, str]


def print_created_at(created_at: Datetime) -> None:
    print(created_at)


def print_value(value: NumberOrStr) -> None:
    print(value)


def run_example() -> None:
    print_created_at(datetime.now())
    # print_created_at(datetime.now().date())
    print_value(1)
    print_value(3.5)
    print_value("Text")
    # print_value(None)
