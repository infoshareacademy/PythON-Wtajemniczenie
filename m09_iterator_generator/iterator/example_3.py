from __future__ import annotations

import time


class NamesServerClient:
    def __init__(self, host_address: str) -> None:
        pass

    def get_names(self, page_number: int) -> list[str]:
        time.sleep(3)
        return ["Mikołaj", "Alicja", "Jakub"]


class NamesIterator:
    def __init__(self, host_address: str) -> None:
        self.names_server_client = NamesServerClient(host_address)
        self.current_page_number = 0
        self.buffered_names: list[str] = []

    def __iter__(self) -> NamesIterator:
        return self

    def __next__(self) -> str:
        if not self.buffered_names:
            self.current_page_number += 1
            self.buffered_names = self.names_server_client.get_names(self.current_page_number)
        return self.buffered_names.pop()


def run_example() -> None:
    names_iterator = NamesIterator("www.random-names-server...")
    print(next(names_iterator))
    print(next(names_iterator))
    print(next(names_iterator))
    print(next(names_iterator))
    print(next(names_iterator))


if __name__ == "__main__":
    run_example()
