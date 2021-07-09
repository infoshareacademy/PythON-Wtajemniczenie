from datetime import date
from typing import cast

from dateutil.relativedelta import relativedelta  # type: ignore


def full_years_between_dates(later: date, earlier: date) -> int:
    return cast(int, relativedelta(later, earlier).years)
