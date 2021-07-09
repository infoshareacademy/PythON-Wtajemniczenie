from datetime import date

from new_movies.exceptions import UserNotFound
from new_movies.user import User, Role

available_users = [
    User(
        first_name="Mikołaj",
        last_name="Lewandowski",
        login="Mikolaj",
        birth_date=date(year=1980, month=1, day=1),
        credits_left=5,
        role=Role.USER,
        rented_movies=[],
        rented_games=[],
    )
]


def find_user_by_login(login):
    lower_case_login = login.lower()
    for user in available_users:
        if lower_case_login == user.login.lower():
            return user
    raise UserNotFound()
