from new_movies.actions import user as user_actions
from new_movies.rentable import Rentable
from new_movies.rental_directory import available_movies, available_games


def run_example() -> None:
    user = user_actions.login()
    user_actions.select_timezone_preferences(user)

    elements_to_rent: list[Rentable] = [available_movies[0], available_movies[1], available_games[0]]
    for element_to_rent in elements_to_rent:
        element_to_rent.rent_by(user)


if __name__ == "__main__":
    run_example()
