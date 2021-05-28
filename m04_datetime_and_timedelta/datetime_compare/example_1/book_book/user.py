from dataclasses import dataclass

from book_book.datetime_preferences import DatetimePreference


@dataclass
class User:
    login: str
    datetime_preferences: DatetimePreference = DatetimePreference.EUROPE
