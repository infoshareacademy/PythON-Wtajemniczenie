from dataclasses import dataclass


@dataclass
class Order:
    identifier: str

    def total_amount(self) -> int:
        return 150
