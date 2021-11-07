from dataclasses import dataclass


@dataclass
class Account:
    holder: str
    money_amount: int

    def __str__(self) -> str:
        return f"Konto należy do: {self.holder}, Stan konta: {self.money_amount}"
