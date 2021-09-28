from typing import Any


class OrderManagementClient:
    def __init__(self) -> None:
        self.connected = False

    def connect(self, token: str) -> None:
        self.connected = True

    def update_status(self, order_identifier: str, new_status: str) -> None:
        if not self.connected:
            raise Exception("No connection!")
        print(f"Zamówienie {order_identifier} zaktualizowano do statusu: {new_status}")

    def cancel(self, order_identifier: str) -> None:
        pass

    def create(self, order_details: Any) -> str:
        pass
