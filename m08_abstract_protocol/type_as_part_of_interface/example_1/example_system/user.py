from dataclasses import dataclass
from enum import Enum, auto


class PaymentMethodType(Enum):
    CREDIT_CARD = auto()
    E_TRANSFER = auto()
    MOBILE = auto()


@dataclass
class PaymentMethod:
    payment_type: PaymentMethodType
    global_identifier: str


@dataclass
class User:
    name: str
    payment_methods: list[PaymentMethod]

    @property
    def default_payment_method(self) -> PaymentMethod:
        return self.payment_methods[0]
