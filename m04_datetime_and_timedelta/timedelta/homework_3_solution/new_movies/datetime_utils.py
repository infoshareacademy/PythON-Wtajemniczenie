from dateutil.relativedelta import relativedelta


def full_years_between_dates(later, earlier):
    years = later.year - earlier.year
    if later.month > earlier.month:
        return years
    if later.month < earlier.month:
        return years - 1
    if later.day >= earlier.day:
        return years
    return years - 1


#
# def full_years_between_dates(later, earlier):
#     return relativedelta(later, earlier).years
