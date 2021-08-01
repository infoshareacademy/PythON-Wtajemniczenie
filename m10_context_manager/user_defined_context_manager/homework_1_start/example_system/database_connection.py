import random


class NoConnectionError(Exception):
    pass


class DatabaseConnection:
    def __init__(self) -> None:
        self.queries_in_transaction: list[str] = []
        self.connected = False

    def connect(self) -> None:
        connection_id = random.randint(1, 100)
        print(20 * "-")
        print(f"Connection number {connection_id} established")
        self.queries_in_transaction = []
        self.connected = True

    def execute(self, query: str) -> None:
        if not self.connected:
            raise NoConnectionError()
        print(f"Executing: {query}")
        self.queries_in_transaction.append(query)

    def commit(self) -> None:
        if not self.connected:
            raise NoConnectionError()
        print("COMMITTING queries: ")
        for query in self.queries_in_transaction:
            print(query)

    def rollback(self) -> None:
        if not self.connected:
            raise NoConnectionError()
        print("ROLLBACK")

    def close(self) -> None:
        if not self.connected:
            raise NoConnectionError()
        print("Connection closed")
        print(20 * "-")
        self.connected = False
