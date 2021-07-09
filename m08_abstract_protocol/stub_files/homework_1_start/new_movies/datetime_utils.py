from datetime import date

from dateutil.relativedelta import relativedelta


def full_years_between_dates(later: date, earlier: date) -> int:
    return relativedelta(later, earlier).years
