import uuid
from typing import Any


def get_order_identifier_by_number(order_number: str) -> str:
    return str(uuid.uuid1())


def get_orders() -> list[Any]:
    ...


def load_order_details() -> Any:
    ...
