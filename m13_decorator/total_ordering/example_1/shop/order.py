from dataclasses import dataclass
from functools import total_ordering
from typing import Any, cast


@dataclass
class OrderElement:
    name: str
    value: int


# @total_ordering
class Order:
    def __init__(self, client_name: str) -> None:
        self.client_name = client_name
        self.elements: list[OrderElement] = []

    def add_element(self, element: OrderElement) -> None:
        self.elements.append(element)

    @property
    def overall_value(self) -> int:
        return sum([element.value for element in self.elements])

    # def __eq__(self, other: Any) -> bool:
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return cast(bool, self.overall_value == other.overall_value)
    #
    # def __gt__(self, other: Any) -> bool:
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return cast(bool, self.overall_value >= other.overall_value)
