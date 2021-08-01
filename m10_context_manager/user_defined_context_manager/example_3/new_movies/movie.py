from dataclasses import dataclass


@dataclass
class Movie:
    name: str

    def __str__(self) -> str:
        return self.name
