class GoldProvider:
    def __init__(self, login: str, password: str) -> None:
        self.connection = self._connect(login, password)

    def _connect(self, login: str, password: str) -> None:
        return None

    def balance_account(self) -> None:
        ...

    def load_account_details(self) -> None:
        ...

    def pay_with_usd(self, currency_code: int, dollars: int, cents: int) -> None:
        print("Gold Provider - zrealizowano płatność")

    def pay_with_pln(self, currency_code: int, amount: int) -> None:
        ...

    def is_available(self) -> bool:
        return True
