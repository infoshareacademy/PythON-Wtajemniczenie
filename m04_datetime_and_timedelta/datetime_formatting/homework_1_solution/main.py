from new_movies import actions, movies_directory


def run_example():
    user = actions.login()
    actions.select_datetime_preferences(user)
    movie_for_today = movies_directory.available_movies[0]
    actions.rent_movie(user, movie_for_today)
    actions.watch_movie(user, movie_for_today)
    actions.cinema_movies_schedule(user)


if __name__ == "__main__":
    run_example()
