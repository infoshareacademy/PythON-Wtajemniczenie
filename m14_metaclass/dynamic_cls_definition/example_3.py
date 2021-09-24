from typing import Any


# class Bike:
#
#     def __init__(self, owner: str, model: str) -> None:
#         self.owner = owner
#         self.model = model
#
#     def __str__(self) -> str:
#         return f"{self.owner} is owner of {self.model} bike"


def _bike__init__(self: Any, owner: str, model: str) -> None:
    self.owner = owner
    self.model = model


def _bike__str__(self: Any) -> str:
    return f"{self.owner} is owner of {self.model} bike"


Bike = type("Bike", (), {"__init__": _bike__init__, "__str__": _bike__str__})


def run_example() -> None:
    mikolaj_bike = Bike(owner="Mikołaj", model="Giant")
    print(mikolaj_bike)


if __name__ == "__main__":
    run_example()
