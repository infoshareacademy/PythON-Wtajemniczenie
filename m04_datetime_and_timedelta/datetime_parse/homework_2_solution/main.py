from new_movies.actions import cinema as cinema_actions
from new_movies.actions import movie as movie_actions
from new_movies.actions import user as user_actions


def run_example():
    user = user_actions.login()
    user_actions.select_datetime_preferences(user)
    movie_actions.add_movie(user)
    cinema_actions.cinema_movies_schedule(user)


if __name__ == "__main__":
    run_example()
