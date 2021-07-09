from __future__ import annotations

import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:
    from new_movies.user import User


class Rentable(ABC):
    @abstractmethod
    def rent_by(self, user: User) -> None:
        ...
