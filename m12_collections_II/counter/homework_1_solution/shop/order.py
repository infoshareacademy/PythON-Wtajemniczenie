from __future__ import annotations

from collections import Counter

from shop import products_directory


class Order:
    def __init__(self) -> None:
        self.elements: Counter[str] = Counter()

    def add_element(self, product_name: str, quantity: int = 1) -> None:
        self.elements[product_name] += quantity

    def remove_element(self, product_name: str, quantity: int = 1) -> None:
        self.elements[product_name] -= quantity
        if self.elements[product_name] < 1:
            del self.elements[product_name]

    def merge_orders(self, order_to_merge: Order) -> None:
        self.elements += order_to_merge.elements

    @property
    def total_sum(self) -> int:
        result = 0
        for element, quantity in self.elements.items():
            result += quantity * products_directory.product_price(element)
        return result

    @property
    def products(self) -> list[str]:
        return list(self.products)

    def __str__(self) -> str:
        results = [
            f"{element} x {quantity} -> {products_directory.product_price(element)}"
            for element, quantity in self.elements.items()
        ]
        results.append(f"Total: {self.total_sum}")
        return "\n".join(results)
