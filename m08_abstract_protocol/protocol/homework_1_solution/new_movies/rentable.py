from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from new_movies.user import User


class Rentable(typing.Protocol):
    def rent_by(self, user: User) -> None:
        ...
