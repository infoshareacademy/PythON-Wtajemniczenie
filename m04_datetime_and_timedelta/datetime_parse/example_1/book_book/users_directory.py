from book_book.exceptions import UserNotFound
from book_book.user import User

available_users = [User(login="Mikolaj")]


def find_user_by_login(login):
    lower_case_login = login.lower()
    for user in available_users:
        if lower_case_login == user.login.lower():
            return user
    raise UserNotFound()
