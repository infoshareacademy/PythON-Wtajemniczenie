from datetime import datetime, timedelta

from new_movies import users_directory, permissions, configuration
from new_movies.datetime_preferences import DatetimePreference
from new_movies.exceptions import UserNotFound, ActionNotAllowed


def login():
    failed_login_attempt = 0
    last_attempt_datetime = None
    lock_time = timedelta()
    while True:
        user_login = input("Type in your login: ")

        if last_attempt_datetime is not None:
            login_attempts_interval = datetime.now() - last_attempt_datetime
            last_attempt_datetime = datetime.now()
            if login_attempts_interval < lock_time:
                failed_login_attempt += 1
                print("This attempt is ignored as you have exceeded auth failures limit.")
                print(f"Please wait {lock_time} before next attempt")
                continue
        last_attempt_datetime = datetime.now()

        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            failed_login_attempt += 1
            print("There is no user with such login - try again")
            if failed_login_attempt >= configuration.AUTH_FAILED_EXTENDED_LIMIT:
                lock_time = configuration.AUTH_FAILED_LOCK_TIME * 2
                print(f"Auth failures limit exceeded. You have to wait {lock_time}")
            elif failed_login_attempt >= configuration.AUTH_FAILED_LIMIT:
                lock_time = configuration.AUTH_FAILED_LOCK_TIME
                print(f"Auth failures limit exceeded. You have to wait {lock_time}")



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
