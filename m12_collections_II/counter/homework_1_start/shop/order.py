from __future__ import annotations


class Order:
    def __init__(self) -> None:
        # TODO: Init empty order
        pass

    def add_element(self, product_name: str, quantity: int = 1) -> None:
        # TODO
        pass

    def remove_element(self, product_name: str, quantity: int = 1) -> None:
        # TODO
        pass

    def merge_orders(self, order_to_merge: Order) -> None:
        # TODO
        pass

    @property
    def total_sum(self) -> int:
        # TODO use product_price to get product price by product name
        pass

    @property
    def products(self) -> list[str]:
        # TODO return list of unique products in order
        pass

    def __str__(self) -> str:
        # TODO: all elements with numbers and prices + total sum
        pass
