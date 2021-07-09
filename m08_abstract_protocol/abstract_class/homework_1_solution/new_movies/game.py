from dataclasses import dataclass, field
from datetime import datetime


class Game:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


@dataclass
class RentedGame:
    game: Game
    rented_at: datetime = field(default_factory=datetime.now)
