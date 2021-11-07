import threading
from dataclasses import dataclass, field


@dataclass
class Account:
    holder: str
    money_amount: int
    money_lock: threading.Lock = field(default_factory=threading.Lock)

    def __str__(self) -> str:
        return f"Konto należy do: {self.holder}, Stan konta: {self.money_amount}"
