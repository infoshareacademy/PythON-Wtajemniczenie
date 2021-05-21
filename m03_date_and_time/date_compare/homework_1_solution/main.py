from new_movies import actions
from new_movies.movies_directory import available_movies
from new_movies.user import User, Role


def run_example():
    standard_user = User(
        first_name="Mikołaj",
        last_name="Lewandowski",
        credits_left=5,
        role=Role.USER,
        rented_movies=[],
    )

    actions.rent_movie(standard_user, available_movies[0])
    actions.watch_movie(standard_user, available_movies[0])
    actions.watch_movie(standard_user, available_movies[0])
    actions.watch_movie(standard_user, available_movies[0])
    actions.watch_movie(standard_user, available_movies[0])
    actions.watch_movie(standard_user, available_movies[0])
    actions.watch_movie(standard_user, available_movies[0])


if __name__ == "__main__":
    run_example()
