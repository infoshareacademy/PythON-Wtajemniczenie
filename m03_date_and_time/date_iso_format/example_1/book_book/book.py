from dataclasses import dataclass
from datetime import date


@dataclass
class Book:
    title: str
    author: str
    release_date: date

    def __str__(self):
        return f'"{self.title}" - {self.author} ({self.release_date})'
