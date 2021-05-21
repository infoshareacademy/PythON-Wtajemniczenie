from dataclasses import dataclass, field
from datetime import date


@dataclass
class Book:
    title: str
    author: str
    release_date: date
    added_at_date: date = field(default_factory=date.today)
    # Bez default_factory otrzymamy zawsze taką samą datę
    # added_at_date: date = date.today()

    def __str__(self):
        return f'"{self.title}" - {self.author} ({self.release_date})'
