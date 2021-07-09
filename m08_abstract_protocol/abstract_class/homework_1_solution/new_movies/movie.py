from dataclasses import dataclass
from datetime import datetime, date
from enum import IntEnum
from zoneinfo import ZoneInfo

from new_movies.datetime_preferences import DateAndTimeFormat


class AgeRate(IntEnum):
    GREEN = 0
    YELLOW = 12
    ORANGE = 16
    RED = 18


class Movie:

    MIN_ALLOWED_RATE = 1
    MAX_ALLOWED_RATE = 5

    def __init__(self, name: str, category: str, release_date: date, age_rate: AgeRate) -> None:
        self.name = name
        self.category = category
        self.release_date = release_date
        self.age_rate = age_rate
        self.added_at_datetime = datetime.now(tz=ZoneInfo("UTC"))
        self._rates: list[int] = []
        self._viewers: list[str] = []

    def __str__(self) -> str:
        return f"{self.name} - {self.category} Movie, rate: {self.rate:.2f} ({self.release_date})"

    def info_with_date_format(self, date_and_time_format: DateAndTimeFormat) -> str:
        release_date_formatted = self.release_date.strftime(date_and_time_format.date_format)
        return (
            f"{self.name} - {self.category} Movie, rate: {self.rate:.2f} ({release_date_formatted})"
        )

    @property
    def rate(self) -> float:
        if len(self._viewers):
            return sum(self._rates) / len(self._viewers)
        return 0

    def is_age_appropriate_to_watch(self, age: int) -> bool:
        return self.age_rate.value <= age


@dataclass
class RentedMovie:
    movie: Movie
    views_left: int = 3
