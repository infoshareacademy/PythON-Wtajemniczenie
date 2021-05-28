from dataclasses import dataclass, field
from datetime import date, datetime


@dataclass
class Book:
    title: str
    author: str
    release_date: date
    added_at_datetime: datetime = field(default_factory=datetime.now)

    def __str__(self):
        return f'"{self.title}" - {self.author} ({self.release_date})'

    def info_with_date_format(self, date_and_time_format):
        release_date_formatted = self.release_date.strftime(date_and_time_format.date_format)
        added_at_datetime_formatted = self.added_at_datetime.strftime(date_and_time_format.datetime_format)
        return f'"{self.title}" - {self.author} ({release_date_formatted}) [{added_at_datetime_formatted}]'
