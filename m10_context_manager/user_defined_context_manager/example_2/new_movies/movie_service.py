import random
from typing import Protocol


class MovieService(Protocol):
    def connect(self) -> None:
        ...

    def get_movie(self) -> str:
        ...

    def close(self) -> None:
        ...


class MovieServiceA:
    def connect(self) -> None:
        print("Connecting...")

    def get_movie(self) -> str:
        movie_number = random.randint(1, 100)
        return f"Movie-AAA({movie_number})"

    def close(self) -> None:
        print("Closing...")


class MovieServiceB:
    def connect(self) -> None:
        print("Connecting...")

    def get_movie(self) -> str:
        movie_number = random.randint(1, 100)
        return f"Movie-BBB({movie_number})"

    def close(self) -> None:
        print("Closing...")
