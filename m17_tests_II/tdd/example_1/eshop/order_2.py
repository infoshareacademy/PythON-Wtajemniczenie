from __future__ import annotations

from eshop.order_element import OrderElement


class Order:
    def __init__(self, client_first_name: str, client_last_name: str) -> None:
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self._order_elements: list[OrderElement] = []

    def add_element(self, product: str, quantity: int, price: int) -> None:
        new_element = OrderElement(product, quantity, price)
        self._order_elements.append(new_element)

    @property
    def elements(self) -> list[OrderElement]:
        return self._order_elements

    def __repr__(self) -> str:
        return (
            f"Order {self.client_first_name} {self.client_last_name} {len(self.elements)} item(s)"
        )

    def __eq__(self, other: object) -> bool:
        # if self.__class__ != other.__class__:
        #     return NotImplemented

        if not isinstance(other, Order):
            return NotImplemented

        if self.client_first_name != other.client_first_name:
            return False
        if self.client_last_name != other.client_last_name:
            return False

        if len(self.elements) != len(other.elements):
            return False

        for element in self.elements:
            if element not in other.elements:
                return False

        return True
