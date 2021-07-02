from datetime import datetime, date
from enum import Enum, IntEnum
from zoneinfo import ZoneInfo


class MovieAlreadySeen(ValueError):
    pass


class InvalidRateValue(ValueError):
    pass


class AgeRate(Enum):
    GREEN = 0
    YELLOW = 12
    ORANGE = 16
    RED = 18

#
# class AgeRate(IntEnum):
#     GREEN = 0
#     YELLOW = 12
#     ORANGE = 16
#     RED = 18


class Movie:

    MIN_ALLOWED_RATE = 1
    MAX_ALLOWED_RATE = 5

    def __init__(self, name: str, category: str, release_date: date, age_rate: AgeRate) -> None:
        self.name = name
        self.category = category
        self.release_date = release_date
        self.age_rate = age_rate
        self.added_at_datetime = datetime.now(tz=ZoneInfo("UTC"))
        self._rates = []
        self._viewers = []

        # self.name: str = name
        # self.category: str = category
        # self.release_date: date = release_date
        # self.age_rate: AgeRate = age_rate
        # self.added_at_datetime: date = datetime.now(tz=ZoneInfo("UTC"))
        # self._rates: list[int] = []
        # self._viewers: list[str] = []

        # reveal_type(self.name)
        # reveal_type(self.release_date)
        # reveal_type(self.age_rate)
        # reveal_type(self.added_at_datetime)
        # reveal_type(self._rates)
        # reveal_type(self._viewers)

    def __str__(self) -> str:
        return f"{self.name} - {self.category} Movie, rate: {self.rate:.2f} ({self.release_date})"

    @property
    def rate(self) -> float:
        if len(self._viewers):
            return sum(self._rates) / len(self._viewers)
        return 0

    def vote(self, viewer_name: str, rate: int) -> None:
        if viewer_name in self._viewers:
            raise MovieAlreadySeen()
        if not self.MIN_ALLOWED_RATE <= rate <= self.MAX_ALLOWED_RATE:
            raise InvalidRateValue()

        self._viewers.append(viewer_name)
        self._rates.append(rate)

    def is_age_appropriate_to_watch(self, age: int) -> bool:
        return self.age_rate.value <= age

