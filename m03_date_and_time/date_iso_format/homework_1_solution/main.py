from new_movies import movies_ranking, movies_directory, actions


def run_example():
    movies_ranking.print_all_movies_ranking(movies_directory.available_movies)
    actions.add_movie()
    movies_ranking.print_all_movies_ranking(movies_directory.available_movies)


if __name__ == "__main__":
    run_example()
