from new_movies import actions
from new_movies.random_data_utility import random_generator
from new_movies.user import User, Role


def run_example() -> None:
    some_movies = random_generator.generate_random_movies(movies_number=15)
    standard_user = User(
        first_name="Mikołaj",
        last_name="Lewandowski",
        credits_left=5,
        role=Role.USER,
        rented_movies=[],
    )

    actions.rent_movie(standard_user, some_movies[0])
    actions.rent_movie(standard_user, some_movies[1])
    actions.watch_movie(standard_user, some_movies[0])
    actions.watch_movie(standard_user, some_movies[1])


if __name__ == "__main__":
    run_example()
