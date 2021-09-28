class GreenProvider:
    def connect(self, api_key: str) -> None:
        return None

    def get_event_default_handler(self) -> None:
        ...

    def checkout_order(self) -> None:
        ...

    def pay_with_usd(self, currency_code: int, cents: int) -> None:
        print("Green Provider - zrealizowano płatność")

    def pay_with_pln(self, currency_code: int, amount: int) -> None:
        ...
