from new_movies.actions import cinema as cinema_actions
from new_movies.actions import movie as movie_actions
from new_movies.actions import user as user_actions
from new_movies import movies_directory


def run_example():
    user = user_actions.login()
    user_actions.select_datetime_preferences(user)
    movie_for_today = movies_directory.available_movies[0]
    movie_actions.rent_movie(user, movie_for_today)
    movie_actions.watch_movie(user, movie_for_today)
    cinema_actions.cinema_movies_schedule(user)


if __name__ == "__main__":
    run_example()
