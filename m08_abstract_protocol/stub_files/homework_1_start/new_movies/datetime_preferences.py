from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class DateAndTimeFormat:
    date_format: str
    time_format: str

    @property
    def datetime_format(self) -> str:
        return f"{self.date_format} {self.time_format}"

    def __str__(self) -> str:
        return self.datetime_format


class DatetimePreference(Enum):
    USA = DateAndTimeFormat(date_format="%m/%d/%Y", time_format="%H:%M:%S")
    EUROPE = DateAndTimeFormat(date_format="%d.%m.%Y", time_format="%H:%M:%S")
    ISO = DateAndTimeFormat(date_format="%Y-%m-%d", time_format="%H:%M:%S")
    UK = DateAndTimeFormat(date_format="%d/%m/%Y", time_format="%I:%M:%S %p")

    def __str__(self) -> str:
        return f"Format {self.name}: {self.value}"

    @classmethod
    def ordered_instances(cls) -> list[DatetimePreference]:
        return [instance for instance in cls.__members__.values()]

    @classmethod
    def instance_by_index(cls, index: int) -> DatetimePreference:
        return cls.ordered_instances()[index]
