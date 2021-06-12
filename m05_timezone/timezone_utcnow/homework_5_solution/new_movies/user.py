from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List
from zoneinfo import ZoneInfo

from new_movies import datetime_utils
from new_movies.datetime_preferences import DatetimePreference
from new_movies.rented_movie import RentedMovie


class Role(Enum):
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"
    USER = "USER"


@dataclass
class User:
    first_name: str
    last_name: str
    login: str
    birth_date: date
    credits_left: int
    role: Role
    rented_movies: List[RentedMovie]
    datetime_preferences: DatetimePreference = DatetimePreference.EUROPE
    timezone: ZoneInfo = ZoneInfo("Europe/Warsaw")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return datetime_utils.full_years_between_dates(date.today(), self.birth_date)
