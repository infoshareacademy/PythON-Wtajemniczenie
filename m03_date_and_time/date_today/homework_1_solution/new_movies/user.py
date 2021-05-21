from dataclasses import dataclass
from enum import Enum
from typing import List

from new_movies.rented_movie import RentedMovie


class Role(Enum):
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"
    USER = "USER"


@dataclass
class User:
    first_name: str
    last_name: str
    credits_left: int
    role: Role
    rented_movies: List[RentedMovie]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
