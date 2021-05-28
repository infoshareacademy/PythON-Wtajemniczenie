from dataclasses import dataclass, field
from datetime import date, datetime


@dataclass
class Book:
    title: str
    author: str
    release_date: date
    # added_at_datetime: datetime = field(default_factory=datetime.today)
    added_at_datetime: datetime = field(default_factory=datetime.now)

    def __str__(self):
        return f'"{self.title}" - {self.author} ({self.release_date})'
