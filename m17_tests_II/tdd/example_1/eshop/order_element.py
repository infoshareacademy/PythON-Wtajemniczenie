class OrderElement:
    def __init__(self, product: str, quantity: int, price: int) -> None:
        self.product = product
        self.quantity = quantity
        self.price = price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OrderElement):
            return NotImplemented
        return (
            self.quantity == other.quantity
            and self.product == other.product
            and self.price == other.price
        )

    def __str__(self) -> str:
        return f"{self.product} x {self.quantity}"
