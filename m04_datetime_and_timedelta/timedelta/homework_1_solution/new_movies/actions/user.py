from new_movies import users_directory, permissions
from new_movies.datetime_preferences import DatetimePreference
from new_movies.exceptions import UserNotFound, ActionNotAllowed


def login():
    while True:
        user_login = input("Type in your login: ")
        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            print("There is no user with such login - try again")


def select_datetime_preferences(user):
    print("Available formats:")
    for option_index, datetime_preference in enumerate(DatetimePreference):
        print(f"{option_index}) {datetime_preference}")

    selected_option = int(input("Select an option: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(selected_option)


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()
