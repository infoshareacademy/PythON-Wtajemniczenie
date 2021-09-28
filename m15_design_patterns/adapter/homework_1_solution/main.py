from new_movie.movies_directory import get_movies_data
from new_movie.ui_lib_wrapper import UILibWrapper


def run_example() -> None:
    movies_data = get_movies_data()
    ui_lib = UILibWrapper(window_header="Filmy")
    ui_lib.print_movies_list(movies_data)


if __name__ == "__main__":
    run_example()
