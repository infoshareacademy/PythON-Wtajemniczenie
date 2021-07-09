from datetime import date

from dateutil.easter import easter


def is_easter(date_to_be_checked: date) -> bool:
    easter_in_particular_year = easter(year=date_to_be_checked.year)
    return easter_in_particular_year == date_to_be_checked
