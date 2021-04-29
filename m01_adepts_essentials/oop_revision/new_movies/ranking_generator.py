def movie_sorting_key(movie):
    return movie.rate


class RankingGenerator:
    @staticmethod
    def generate_ranking(movies):
        movies_in_rate_order = sorted(
            movies, key=lambda single_movie: single_movie.rate, reverse=True
        )
        # movies_in_rate_order = sorted(movies, key=movie_sorting_key, reverse=True)
        for index, movie in enumerate(movies_in_rate_order):
            print(f"{index + 1}. {movie}")


def generate_ranking(movies):
    movies_in_rate_order = sorted(movies, key=lambda single_movie: single_movie.rate, reverse=True)
    for index, movie in enumerate(movies_in_rate_order):
        print(f"{index + 1}. {movie}")
