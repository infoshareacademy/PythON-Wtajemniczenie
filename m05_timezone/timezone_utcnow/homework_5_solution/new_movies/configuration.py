from datetime import date, timedelta

UNLIMITED_WATCHING_START_DATE = date(year=2021, month=2, day=1)
UNLIMITED_WATCHING_END_DATE = date(year=2021, month=4, day=30)

AUTH_FAILED_LIMIT = 2
AUTH_FAILED_EXTENDED_LIMIT = 4
AUTH_FAILED_LOCK_TIME = timedelta(seconds=5)
