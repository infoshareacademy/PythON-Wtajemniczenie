from new_movies import movies_ranking
from new_movies.random_data_utility import random_generator


def run_example():
    some_movies = random_generator.generate_random_movies(movies_number=15)
    movies_ranking.print_top_movies(some_movies)


if __name__ == "__main__":
    run_example()
