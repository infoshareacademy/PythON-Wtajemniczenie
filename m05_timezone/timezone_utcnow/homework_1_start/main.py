from new_movies import movies_directory
from new_movies.actions import user as user_actions
from new_movies.actions import movie as movie_actions


def run_example():
    user = user_actions.login()
    movie_to_rent = movies_directory.available_movies[0]
    movie_actions.rent_movie(user, movie_to_rent)
    movie_actions.watch_movie(user, movie_to_rent)


if __name__ == "__main__":
    run_example()
