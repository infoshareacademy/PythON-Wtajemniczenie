from datetime import date
from typing import Optional

class relativedelta:

    years: int

    def __init__(
        self,
        dt1: Optional[date] = ...,
        dt2: Optional[date] = ...,
        years: Optional[int] = ...,
        months: Optional[int] = ...,
        days: Optional[int] = ...,
        leapdays: Optional[int] = ...,
        weeks: Optional[int] = ...,
        hours: Optional[int] = ...,
        minutes: Optional[int] = ...,
        seconds: Optional[int] = ...,
        microseconds: Optional[int] = ...,
        year: Optional[int] = ...,
        month: Optional[int] = ...,
        day: Optional[int] = ...,
        weekday: Optional[int] = ...,
        yearday: Optional[int] = ...,
        nlyearday: Optional[int] = ...,
        hour: Optional[int] = ...,
        minute: Optional[int] = ...,
        second: Optional[int] = ...,
        microsecond: Optional[int] = ...,
    ) -> None: ...
