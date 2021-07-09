from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from zoneinfo import ZoneInfo


class AgeRate(IntEnum):
    GREEN = 0
    YELLOW = 12
    ORANGE = 16
    RED = 18


class Movie:

    MIN_ALLOWED_RATE = 1
    MAX_ALLOWED_RATE = 5

    def __init__(self, name, category, release_date, age_rate):
        self.name = name
        self.category = category
        self.release_date = release_date
        self.age_rate = age_rate
        self.added_at_datetime = datetime.now(tz=ZoneInfo("UTC"))
        self._rates = []
        self._viewers = []

    def __str__(self):
        return f"{self.name} - {self.category} Movie, rate: {self.rate:.2f} ({self.release_date})"

    def info_with_date_format(self, date_and_time_format):
        release_date_formatted = self.release_date.strftime(date_and_time_format.date_format)
        return (
            f"{self.name} - {self.category} Movie, rate: {self.rate:.2f} ({release_date_formatted})"
        )

    @property
    def rate(self):
        if len(self._viewers):
            return sum(self._rates) / len(self._viewers)
        return 0

    def is_age_appropriate_to_watch(self, age):
        return self.age_rate.value <= age


@dataclass
class RentedMovie:
    movie: Movie
    views_left: int = 3
