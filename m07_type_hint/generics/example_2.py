import random
from typing import TypeVar, Generic

T = TypeVar("T")


class Randomizer(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_random_element(self) -> T:
        return random.choice(self.items)


def run_example() -> None:
    randomizer = Randomizer[int]()
    randomizer.add(4)
    randomizer.add(7)
    randomizer.add(5)
    random_element = randomizer.get_random_element()
    print(random_element)
    reveal_type(random_element)


if __name__ == "__main__":
    run_example()
