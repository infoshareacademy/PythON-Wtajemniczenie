def print_top_movies(movies, *, limit=10):
    movies_in_rate_order = sorted(movies, key=lambda single_movie: single_movie.rate, reverse=True)
    for index, movie in enumerate(movies_in_rate_order):
        if index == limit:
            break
        print(f"{index + 1}. {movie}")


def print_all_movies_ranking(movies):
    print_top_movies(movies, limit=len(movies))
