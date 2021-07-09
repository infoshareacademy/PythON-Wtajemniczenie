from __future__ import annotations

import typing
from dataclasses import dataclass, field
from datetime import datetime

from new_movies.exceptions import NoCreditsForRent
from new_movies.rentable import Rentable

if typing.TYPE_CHECKING:
    from new_movies.user import User


class Game(Rentable):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def rent_by(self, user: User) -> None:
        if user.credits_left < 2:
            raise NoCreditsForRent()
        user.credits_left -= 2
        user.rented_games.append(RentedGame(game=self))
        print(f"Rented game: {self}")



@dataclass
class RentedGame:
    game: Game
    rented_at: datetime = field(default_factory=datetime.now)
