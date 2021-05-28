from new_movies.exceptions import UserNotFound
from new_movies.user import User, Role

available_users = [
    User(
        first_name="Mikołaj",
        last_name="Lewandowski",
        login="Mikolaj",
        credits_left=5,
        role=Role.USER,
        rented_movies=[],
    )
]


def find_user_by_login(login):
    lower_case_login = login.lower()
    for user in available_users:
        if lower_case_login == user.login.lower():
            return user
    raise UserNotFound()
