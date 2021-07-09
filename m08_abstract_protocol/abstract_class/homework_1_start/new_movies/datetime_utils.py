from dateutil.relativedelta import relativedelta  # type: ignore


def full_years_between_dates(later, earlier):
    return relativedelta(later, earlier).years
