from collections import deque


class CustomersQueue:

    def __init__(self) -> None:
        self.customers: deque[str] = deque()

    def queue_customer(self, customer: str) -> None:
        self.customers.append(customer)

    def queue_vip_customer(self, customer: str) -> None:
        self.customers.appendleft(customer)

    def deque_next_customer(self) -> str:
        return self.customers.popleft()

    def __str__(self) -> str:
        return "-".join(self.customers)

