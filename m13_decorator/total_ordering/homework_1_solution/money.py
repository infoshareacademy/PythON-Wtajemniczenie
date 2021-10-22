from functools import total_ordering
from typing import Any, cast


@total_ordering
class Money:
    def __init__(self, dollars: int, cents: int) -> None:
        self.dollars = dollars
        self.cents = cents

    def as_cents(self) -> int:
        return self.dollars * 100 + self.cents

    def __eq__(self, other: Any) -> bool:
        if self.__class__ != other.__class__:
            return NotImplemented
        return cast(bool, self.as_cents() == other.as_cents())

    def __gt__(self, other: Any) -> bool:
        if self.__class__ != other.__class__:
            return NotImplemented
        return cast(bool, self.as_cents() >= other.as_cents())


def run_example() -> None:
    computer_price = Money(dollars=1999, cents=0)
    book_price = Money(dollars=10, cents=99)
    other_book_price = Money(dollars=10, cents=99)

    print(computer_price < book_price)
    print(computer_price <= book_price)
    print(computer_price > book_price)
    print(computer_price >= book_price)
    print(computer_price == book_price)
    print(other_book_price == book_price)
    print(other_book_price != book_price)


if __name__ == "__main__":
    run_example()
