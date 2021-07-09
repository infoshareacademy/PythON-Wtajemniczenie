from dataclasses import dataclass
from typing import Protocol


@dataclass
class PaymentDTO:
    identifier: str
    amount: int


@dataclass
class TransactionResult:
    success: bool
    context_info: str


class PaymentClient(Protocol):

    def pay(self, payment_data: PaymentDTO) -> TransactionResult:
        ...
